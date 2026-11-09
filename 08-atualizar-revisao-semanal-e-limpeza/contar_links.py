"""Conta as notas órfãs e os links quebrados de um cofre do Obsidian.

Uso: python3 contar_links.py cofre-da-renata

Nota órfã: nenhuma outra nota tem link para ela.
Link quebrado: link [[...]] para uma nota que não existe no cofre.

O script só lê os arquivos. Ele não muda nada no cofre e não diz o que fazer com cada item:
essa decisão é sua, com o checklist da revisão. A pasta Modelos fica de fora da contagem,
porque o modelo de nota tem um link de exemplo. Pastas que começam com ponto (.obsidian, .trash)
também ficam de fora, como no Obsidian.
"""
import re
import sys
from pathlib import Path

LINK = re.compile(r"!?\[\[([^\]|#^]*)[^\]]*\]\]")
CERCA = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)


def notas_do_cofre(cofre):
    notas = {}
    for p in sorted(cofre.rglob("*.md")):
        partes = p.relative_to(cofre).parts
        if any(x.startswith(".") for x in partes) or partes[0] == "Modelos":
            continue
        notas[p.relative_to(cofre).with_suffix("").as_posix()] = p
    return notas


def links_da_nota(texto):
    texto = CERCA.sub("", texto)
    texto = re.sub(r"`[^`\n]*`", "", texto)
    return [m.group(1).strip() for m in LINK.finditer(texto) if m.group(1).strip()]


def achar(alvo, notas, por_nome):
    """Caminho da nota para onde o link aponta, ou None. O Obsidian acha a nota pelo nome."""
    chave = re.sub(r"\.md$", "", alvo).casefold()
    if "/" in chave:
        return next((c for c in notas if c.casefold() == chave), None)
    return por_nome.get(chave)


def contar(cofre):
    notas = notas_do_cofre(cofre)
    por_nome = {}
    for caminho in notas:
        por_nome.setdefault(caminho.rsplit("/", 1)[-1].casefold(), caminho)
    entram = {c: set() for c in notas}
    quebrados = {}
    for origem, p in notas.items():
        for alvo in links_da_nota(p.read_text(encoding="utf-8")):
            destino = achar(alvo, notas, por_nome)
            if destino is None:
                quebrados.setdefault(alvo, []).append(origem)
            elif destino != origem:
                entram[destino].add(origem)
    orfas = [c for c, de in entram.items() if not de]
    return notas, orfas, quebrados


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 contar_links.py <pasta do cofre>")
        return 2
    cofre = Path(sys.argv[1])
    if not cofre.is_dir():
        print(f"Não achei a pasta {cofre}. Rode o comando na pasta da aula, onde está o cofre.")
        return 2
    notas, orfas, quebrados = contar(cofre)
    caixa = [c for c in notas if c.startswith("Caixa de entrada/")]
    soltas = [c for c in notas if "/" not in c]
    print(f"Cofre: {cofre.name}")
    print(f"Notas: {len(notas)} (sem contar a pasta Modelos)")
    print(f"Na caixa de entrada: {len(caixa)}")
    print(f"Soltas na raiz: {len(soltas)}")
    print()
    print(f"Notas órfãs (nenhuma outra nota aponta para elas): {len(orfas)}")
    for c in orfas:
        print(f"  {c}")
    print()
    total = sum(len(v) for v in quebrados.values())
    print(f"Links quebrados (apontam para nota que não existe): {total}, para {len(quebrados)} nota(s)")
    for alvo, origens in sorted(quebrados.items()):
        print(f"  [[{alvo}]] {len(origens)}x, em: {', '.join(sorted(origens))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

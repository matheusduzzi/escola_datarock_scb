"""Verifica a forma de uma LLM Wiki num cofre do Obsidian.

Uso, de dentro da pasta da aula:

    python3 verificar_wiki.py caminho/do/cofre

O cofre precisa ter as pastas `fontes/` e `wiki/`. O script só lê arquivos: não muda nada.

O que ele olha (regras do arquivo de esquema da aula):
  - link quebrado: [[nome]] que não é página da wiki nem arquivo de fontes;
  - frase sem fonte: parágrafo, item de lista ou linha de tabela de uma página
    que não termina com o link de um arquivo de fontes, assim: ([[nome da fonte]]);
  - cita a wiki: o link no fim da frase aponta para uma página da wiki, não para uma fonte;
  - página sem fonte: página que não cita nenhum arquivo de fontes;
  - contagem de fontes: o campo `fontes:` do topo da página diz um número e a página cita outro;
  - fonte sem resumo: arquivo de fontes sem a página `wiki/resumos/<nome da fonte> (resumo).md`;
  - resumo que não cita a própria fonte;
  - página fora do índice: página que o index.md não liga;
  - linha do log fora do formato `## [AAAA-MM-DD] ingest | título` (ou query, ou lint);
  - nome repetido entre a wiki e as fontes;
  - bloco de contradição com menos de duas fontes.

Os blocos `> [!contradição]` com duas fontes ou mais não são erro: vão para
"Para você decidir". O script não lê o sentido das frases. Contradição que a wiki
não marcou e frase que a fonte não diz ficam para a verificação do Claude e para você.

Sai com 0 sem problemas, 1 com problemas e 2 se a pasta não é um cofre com fontes/ e wiki/.
"""
import re
import sys
from pathlib import Path

LINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
CITACAO_FINAL = re.compile(r"\(((?:\s*!?\[\[[^\]]+\]\]\s*,?)+)\)\s*$")
LOG = re.compile(r"^## \[\d{4}-\d{2}-\d{2}\] (ingest|query|lint) \| \S")
CONTRADICAO = re.compile(r"^>\s*\[!contradi[cç][aã]o\]", re.I)
ESPECIAIS = {"index", "log"}
NAVEGACAO = "veja também"


def nome_do_link(alvo):
    alvo = alvo.strip().replace("\\", "/").split("/")[-1]
    return alvo[:-3] if alvo.endswith(".md") else alvo


def links(texto):
    return [nome_do_link(m.group(1)) for m in LINK.finditer(texto)]


def sem_codigo(texto):
    texto = re.sub(r"```[\s\S]*?```", lambda m: "\n" * m.group(0).count("\n"), texto)
    return re.sub(r"`[^`\n]*`", "", texto)


def separar_topo(linhas):
    """Devolve (campos do topo, índice da primeira linha depois do topo)."""
    if not linhas or linhas[0].strip() != "---":
        return {}, 0
    for i in range(1, len(linhas)):
        if linhas[i].strip() == "---":
            campos = {}
            for linha in linhas[1:i]:
                if ":" in linha:
                    chave, valor = linha.split(":", 1)
                    campos[chave.strip()] = valor.strip()
            return campos, i + 1
    return {}, 0


def verificar(cofre):
    fontes = {p.stem: p for p in sorted((cofre / "fontes").rglob("*.md"))}
    paginas = {}
    problemas, decidir = [], []
    for p in sorted((cofre / "wiki").rglob("*.md")):
        rel = p.relative_to(cofre).as_posix()
        if p.stem in paginas:
            problemas.append(f"nome repetido: {rel} e {paginas[p.stem].relative_to(cofre).as_posix()}")
        if p.stem in fontes:
            problemas.append(f"nome repetido: {rel} tem o mesmo nome de um arquivo de fontes")
        paginas[p.stem] = p
    conhecidos = set(fontes) | set(paginas)
    conteudo = {n: p for n, p in paginas.items() if n not in ESPECIAIS}

    for nome, p in sorted(paginas.items(), key=lambda x: x[1].as_posix()):
        rel = p.relative_to(cofre).as_posix()
        texto = sem_codigo(p.read_text(encoding="utf-8"))
        linhas = texto.split("\n")
        for n, linha in enumerate(linhas, 1):
            for alvo in links(linha):
                if alvo not in conhecidos:
                    problemas.append(f"link quebrado: {rel}, linha {n}: [[{alvo}]]")
        if nome in ESPECIAIS:
            continue
        campos, inicio = separar_topo(linhas)
        citadas, achados = set(), []
        secao = ""
        tabela_aberta = False
        bloco = None
        for n in range(inicio, len(linhas)):
            linha = linhas[n].rstrip()
            numero = n + 1
            if bloco is not None and not linha.startswith(">"):
                decidir_ou_problema(bloco, rel, problemas, decidir)
                bloco = None
            if linha.startswith("#"):
                secao = linha.lstrip("#").strip().lower()
                tabela_aberta = False
                continue
            if not linha.strip() or linha.strip() == "---" or secao == NAVEGACAO:
                tabela_aberta = False
                continue
            if CONTRADICAO.match(linha):
                bloco = {"linha": numero, "titulo": CONTRADICAO.sub("", linha).strip(), "fontes": set()}
                continue
            corpo = linha
            if linha.startswith(">"):
                corpo = linha.lstrip(">").strip()
                if not corpo:
                    continue
            if corpo.startswith("|"):
                if not tabela_aberta:
                    tabela_aberta = True
                    continue
                if re.fullmatch(r"\|[\s:|-]+\|?", corpo):
                    continue
                fontes_linha = [a for a in links(corpo) if a in fontes]
                citadas.update(fontes_linha)
                if bloco is not None:
                    bloco["fontes"].update(fontes_linha)
                if not fontes_linha:
                    achados.append(f"frase sem fonte: {rel}, linha {numero}: {resumir(corpo)}")
                continue
            tabela_aberta = False
            final = CITACAO_FINAL.search(corpo)
            for alvo in links(corpo):
                if alvo in fontes:
                    citadas.add(alvo)
                    if bloco is not None:
                        bloco["fontes"].add(alvo)
            if not final:
                achados.append(f"frase sem fonte: {rel}, linha {numero}: {resumir(corpo)}")
                continue
            alvos = links(final.group(1))
            if any(a in paginas for a in alvos) and not any(a in fontes for a in alvos):
                achados.append(f"cita a wiki, não a fonte: {rel}, linha {numero}: {resumir(corpo)}")
        if bloco is not None:
            decidir_ou_problema(bloco, rel, problemas, decidir)
        if not citadas:
            problemas.append(f"página sem fonte: {rel} não cita nenhum arquivo de fontes")
        else:
            problemas.extend(achados)
        declarado = campos.get("fontes", "")
        if declarado.isdigit() and int(declarado) != len(citadas):
            problemas.append(f"contagem de fontes: {rel} diz fontes: {declarado} e cita {len(citadas)}")

    for nome in fontes:
        resumo = conteudo.get(nome + " (resumo)")
        if resumo is None:
            problemas.append(f"fonte sem resumo: fontes/{fontes[nome].relative_to(cofre / 'fontes').as_posix()}")
        elif nome not in links(resumo.read_text(encoding="utf-8")):
            problemas.append(f"resumo que não cita a própria fonte: {resumo.relative_to(cofre).as_posix()}")

    indice = paginas.get("index")
    if indice is None:
        problemas.append("sem índice: falta wiki/index.md")
    else:
        ligadas = set(links(sem_codigo(indice.read_text(encoding="utf-8"))))
        for nome, p in sorted(conteudo.items()):
            if nome not in ligadas:
                problemas.append(f"página fora do índice: {p.relative_to(cofre).as_posix()}")
    log = paginas.get("log")
    if log is None:
        problemas.append("sem log: falta wiki/log.md")
    else:
        for n, linha in enumerate(log.read_text(encoding="utf-8").split("\n"), 1):
            if linha.startswith("## ") and not LOG.match(linha):
                problemas.append(f"linha do log fora do formato: wiki/log.md, linha {n}: {linha.strip()}")
    return fontes, conteudo, problemas, decidir


def decidir_ou_problema(bloco, rel, problemas, decidir):
    citadas = sorted(bloco["fontes"])
    if len(citadas) < 2:
        problemas.append(f"contradição com menos de duas fontes: {rel}, linha {bloco['linha']}: {bloco['titulo']}")
    else:
        decidir.append(f"contradição: {rel}, linha {bloco['linha']}: {bloco['titulo']}\n      fontes: " + "; ".join(citadas))


def resumir(texto, tamanho=70):
    texto = " ".join(texto.split())
    return texto if len(texto) <= tamanho else texto[: tamanho - 3] + "..."


def contar(n, um, varios):
    return f"{n} {um if n == 1 else varios}"


def main(argv):
    cofre = Path(argv[1] if len(argv) > 1 else ".")
    if not (cofre / "fontes").is_dir() or not (cofre / "wiki").is_dir():
        print(f"{cofre} não tem as pastas fontes/ e wiki/. Rode com o caminho da raiz do cofre.")
        return 2
    fontes, conteudo, problemas, decidir = verificar(cofre)
    resumos = sum(1 for n in conteudo if n.endswith(" (resumo)"))
    print(f"Wiki de {cofre.resolve().name}: {contar(len(conteudo) - resumos, 'página', 'páginas')}, {contar(resumos, 'resumo', 'resumos')}, {contar(len(fontes), 'fonte', 'fontes')}.")
    print()
    print(f"Problemas ({len(problemas)})")
    for p in problemas or ["nenhum"]:
        print("  " + p)
    print()
    print(f"Para você decidir ({len(decidir)})")
    for d in decidir or ["nenhuma contradição marcada"]:
        print("  " + d)
    print()
    print("O script olha a forma. Contradição que a wiki não marcou e frase que a fonte não diz ficam para a verificação do Claude e para a sua leitura.")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

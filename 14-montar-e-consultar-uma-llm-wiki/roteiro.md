# Roteiro dos comandos

Os comandos com `git` e `cp` rodam dentro de `cofre-aurora-wiki`. O script roda da pasta da aula, um nível acima. No Windows, use o Git Bash.

## 1. O primeiro commit

```text
cd cofre-aurora-wiki
git init
git config user.name "Seu nome"
git config user.email voce@exemplo.com
git config core.quotepath false
git add .
git commit -m "Cofre antes da ingestão"
```

## 2. O esquema novo

```text
cp ../modelos/CLAUDE-consulta-e-verificacao.md CLAUDE.md
git diff --stat
git commit -am "Esquema: consulta e verificação"
```

## 3. Uma fonte por vez

Troque o nome da fonte em cada volta. A ordem é a da data, que está no começo do nome.

```text
cp "../fontes-novas/2027-01-25 áudio do Bruno - coletas de janeiro.md" fontes/
git add fontes
git commit -m "Fonte: áudio do Bruno de 25/01"
```

Agora o pedido de ingestão ao Claude, o plano e o seu ok. Depois:

```text
git status --short
git add wiki
git diff --staged
cd ..
python3 verificar_wiki.py cofre-aurora-wiki
cd cofre-aurora-wiki
git commit -m "Claude: ingest áudio do Bruno de 25/01"
```

Se a ingestão saiu errada antes do commit: `git restore --staged wiki` e depois `git restore wiki`. Arquivo novo, que o git ainda não acompanha, você apaga à mão. Se saiu errada depois do commit: `git revert --no-edit HEAD`.

## 4. O log e o histórico

```text
git log --oneline
grep "^## \[" wiki/log.md | tail -5
```

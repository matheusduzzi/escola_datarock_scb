# Roteiro do git para o cofre

Rode tudo num terminal aberto na raiz do cofre. No Windows, use o Git Bash. Troque o nome, o e-mail e os nomes de arquivo pelos seus.

## Uma vez, antes de abrir o Claude

```text
git init
```

Copie o `modelos/gitignore-modelo.txt` para a raiz do cofre com o nome `.gitignore`, com o ponto na frente.

```text
git config user.name "Seu Nome"
git config user.email seu@email.example
git config core.quotepath false
git add .
git commit -m "Cofre antes do Claude"
```

## Depois de escrever o esquema e a trava

```text
git status
git add CLAUDE.md .claude/settings.json
git commit -m "Esquema e permissões do Claude"
```

## Depois do teste da trava

```text
git status
```

Tem de sair `nothing to commit, working tree clean`. Se aparecer um arquivo das fontes ou das suas notas, a regra não pegou. Volte o arquivo com `git restore "caminho/do arquivo.md"` e veja o nome da pasta na regra.

## Depois de cada pedido ao Claude

```text
git status --short
git diff
```

Leia cada linha com `-` e cada linha com `+`. Se a edição vale:

```text
git add wiki
git commit -m "Claude: o que ele fez"
```

Se não vale, antes do commit:

```text
git restore wiki
git status
```

## Para desfazer um commit

```text
git log --oneline
git revert --no-edit ID-DO-COMMIT
git log --oneline
```

O `ID-DO-COMMIT` é o código de sete letras e números do commit, no `git log --oneline`. Se for o último, pode usar `HEAD`. O revert pede a pasta limpa: se recusar, rode `git status` primeiro.

Para ver se a wiki voltou ao que era, compare com o commit de antes da edição:

```text
git diff ID-DO-COMMIT-DE-ANTES -- wiki
```

Sem saída quer dizer sem diferença.

## O que não usar

- `git reset --hard`: joga fora sem volta o que não está em commit.
- O terminal do Claude para rodar o git: o histórico é seu.

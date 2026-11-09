# Atualizar: revisão semanal e limpeza

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `cofre-da-renata/` | O cofre da Renata em 30/11, três dias depois do fim da Black Friday, antes da revisão |
| `revisao-semanal.md` | O checklist da revisão, para você preencher |
| `contar_links.py` | Conta as notas órfãs e os links quebrados de um cofre, sem mudar nada |

## Abrir o cofre

Faça uma cópia da pasta `cofre-da-renata` e trabalhe na cópia. Se errar, você copia de novo.

No Obsidian, abra a cópia como cofre: clique no ícone do cofre, no canto de baixo à esquerda, escolha Manage Vaults e clique em Open, ao lado de Open folder as vault. Depois escolha a pasta da cópia. Os nomes dos menus estão como na ajuda do Obsidian, em inglês.

Para mover, renomear e apagar, use o Obsidian, não o Finder nem o Explorador do Windows. É o Obsidian que atualiza os links quando você renomeia uma nota.

## Contar órfãs e links quebrados

Você pode contar de dois jeitos. Use o mesmo jeito antes e depois da revisão.

**Pelo Obsidian, com o CLI.** O CLI do Obsidian pede o instalador 1.12 ou mais novo. Ligue em Settings, General, Command line interface, e siga o que o Obsidian pede para registrar o comando. Com o cofre aberto no Obsidian, rode no terminal:

```bash
obsidian orphans
obsidian unresolved verbose
```

O primeiro lista as notas que nenhuma outra aponta. O segundo lista os links para notas que não existem e em que nota cada um está. Com `total` no fim, cada um mostra só o número.

**Pelo script do kit.** Se você tem o Python 3 instalado, rode na pasta da aula:

```bash
python3 contar_links.py cofre-da-renata
```

Troque `cofre-da-renata` pelo nome da sua cópia. O script lê os arquivos, não muda nada e não diz o que fazer com cada item. Ele pula a pasta `Modelos`, porque o modelo de nota tem um link de exemplo, `[[Nome de outra nota]]`, que não aponta para nota nenhuma. Se o CLI do Obsidian contar a pasta `Modelos`, o modelo aparece como órfã e esse link aparece como quebrado: é de propósito, e você pode ignorar os dois.

Se aparecer "Não achei a pasta", você está em outra pasta no terminal. Entre na pasta da aula e rode de novo.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o comando que você rodou, o que apareceu e o que já tentou. Use os dados do caso, sem dados pessoais. A senha que aparece numa nota do cofre é inventada para o exercício.

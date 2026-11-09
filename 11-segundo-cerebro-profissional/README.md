# Segundo cérebro profissional

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `cofre-aurora-trabalho/` | O cofre de trabalho da Renata em 13/01/2027, com as notas que a aula usa: projeto, reuniões, decisões, pessoas, a Base da equipe e a nota `Fica fora do cofre` |
| `regra-de-informacao-da-aurora.md` | A regra da loja sobre o que pode ir para uma nota de trabalho. É um documento da loja, fora do cofre |
| `janeiro-rapido-sul/` | As oito coisas que a Renata juntou em janeiro sobre a Rápido Sul, para a prática guiada |
| `exercicio-colecao-verao/` | O material da abertura da Coleção Verão 2027, para o exercício |

A Loja Aurora, a equipe, os clientes das planilhas e os valores são inventados para o curso. Os e-mails dos convidados usam o domínio `example.com`, que não pertence a ninguém.

## Abrir o cofre

No Obsidian, clique no ícone do cofre, no canto de baixo à esquerda, escolha Manage Vaults e clique em Open, ao lado de Open folder as vault. Escolha a pasta `cofre-aurora-trabalho`. Os nomes dos menus estão como na ajuda do Obsidian, em inglês.

O cofre não traz as configurações do Obsidian. Para usar os modelos, escreva `Modelos` em Settings, Templates, Template folder location. Para ver os backlinks no fim de cada nota, ligue a opção Backlink in document, nas opções do plugin Backlinks.

O cofre tem um link que ainda não abre: `[[Coleção Verão 2027]]`. A nota é sua, no exercício.

## Prática guiada

Abra os oito arquivos de `janeiro-rapido-sul/` num editor de texto. A planilha `02 coletas de dezembro.csv` abre no Excel, no Google Planilhas ou no LibreOffice. Para contar as coletas por motivo, use uma tabela dinâmica ou um filtro na coluna `motivo`.

No Mac e no Linux, este comando conta pelo terminal, de dentro da pasta dessa aula:

```bash
cut -d, -f6 "janeiro-rapido-sul/02 coletas de dezembro.csv" | tail -n +2 | sort | uniq -c
```

A coluna do motivo é a sexta porque o endereço, entre aspas, tem uma vírgula dentro.

Depois de responder, compare com o cofre: as notas `Rápido Sul`, `Fica fora do cofre` e a pasta `Base da equipe/Decisões`.

## Exercício

Copie a pasta `cofre-aurora-trabalho` para fora do kit e trabalhe na cópia. O material está em `exercicio-colecao-verao/`. O enunciado está no fim da página da aula.

Se você usou o kit da aula «Atualizar: revisão semanal e limpeza», o `contar_links.py` dela conta os links que não abrem no seu cofre:

```bash
python3 ../08-atualizar-revisao-semanal-e-limpeza/contar_links.py cofre-aurora-trabalho
```

No cofre do kit, ele mostra um link que não abre, o da `Coleção Verão 2027`. No seu, depois do exercício, nenhum.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o que você fez, o que apareceu e o que já tentou. Use os dados do caso. Não cole nota nem planilha do seu trabalho.

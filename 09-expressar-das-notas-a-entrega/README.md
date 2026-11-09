# Expressar: das notas à entrega

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `cofre-da-renata/` | O cofre da Renata no começo de dezembro, depois da revisão semanal da aula anterior |
| `cofre-da-renata/1 Projetos/Texto único da política de trocas.md` | A entrega que a aula mostra, com as notas que entraram e o texto aprovado pela Clara |
| `cofre-da-renata/1 Projetos/2026-12-03 retorno - texto da política.md` | A nota de retorno dessa entrega |
| `cofre-da-renata/Modelos/Entrega.md` | Modelo da nota de entrega: pedido, notas que entram, o que falta e texto |
| `cofre-da-renata/Modelos/Nota de retorno.md` | Modelo da nota de retorno |
| `cofre-da-renata/Caixa de entrada/` | Os dois pedidos novos: o post da Juliana (prática guiada) e a proposta do Bruno (exercício) |
| `depois-da-reuniao.md` | A mensagem do Bruno depois da reunião com a Rápido Sul. Abra só depois de terminar a proposta |

## Abrir o cofre

Faça uma cópia da pasta `cofre-da-renata` e trabalhe na cópia. Se errar, você copia de novo.

No Obsidian, abra a cópia como cofre: clique no ícone do cofre, no canto de baixo à esquerda, escolha Manage Vaults e clique em Open, ao lado de Open folder as vault. Depois escolha a pasta da cópia. Os nomes dos menus estão como na ajuda do Obsidian, em inglês.

Para criar uma nota a partir de um modelo, abra a nota nova e use o comando Templates: Insert template, que a aula «O primeiro cofre no Obsidian» mostra. O cofre do kit não traz as configurações do Obsidian. Na primeira vez, escreva `Modelos` em Settings, Templates, Template folder location.

## Os painéis que a aula usa

Os dois ficam na barra lateral direita do Obsidian:

- **Outgoing links** lista os links da nota aberta. Na sua proposta, é onde você vê quantas notas ela cita.
- **Backlinks** lista as notas que apontam para a nota aberta. Numa nota que você mudou depois do retorno, a nota de retorno tem de aparecer ali.

Para buscar uma palavra em todas as notas, use `Command+Shift+F` no Mac ou `Ctrl+Shift+F` no Windows.

## Ver se algum link não abre

Use a contagem da aula «Atualizar: revisão semanal e limpeza». Pelo CLI do Obsidian, com o cofre aberto:

```bash
obsidian unresolved verbose
```

Ou, se você tem o Python 3, pelo script que está na pasta daquela aula:

```bash
python3 ../08-atualizar-revisao-semanal-e-limpeza/contar_links.py cofre-da-renata
```

Troque `cofre-da-renata` pelo nome da sua cópia. O cofre já começa com um link para uma nota que ainda não existe, `[[Coleção Verão 2027]]`, no projeto do site novo. Ele é de propósito, como na aula anterior. Qualquer outro link da lista que saia da sua proposta ou do seu retorno precisa de conserto.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o que você fez, o que apareceu e o que já tentou. Use os dados do caso, sem dados pessoais.

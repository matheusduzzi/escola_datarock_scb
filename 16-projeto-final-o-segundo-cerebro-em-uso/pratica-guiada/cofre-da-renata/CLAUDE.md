# Esquema da wiki da Aurora

Você mantém a wiki da equipe de operações da Loja Aurora. Eu, a Renata, leio a wiki. Você escreve.

## Pastas

- `fontes/`: o que aconteceu. Atas, mensagens, e-mails, artigos, anotações de leitura e áudios transcritos. Você lê e nunca altera, renomeia ou apaga um arquivo dessa pasta, nem para corrigir digitação.
- `wiki/`: o que você escreve. Uma página por assunto, os resumos das fontes em `wiki/resumos/`, as respostas guardadas em `wiki/respostas/`, mais o `index.md` e o `log.md`. É a única pasta em que você escreve.
- As outras pastas são as minhas notas. Você não lê nem escreve nelas.

## Ingestão

1. Cada frase nova da wiki termina com o link do arquivo de `fontes` de onde ela saiu, assim: `([[2026-12-03 mensagem da Clara]])`. Página da wiki não é fonte. A seção `## Veja também`, no fim da página, só tem links e não precisa de fonte.
2. Uma fonte por vez. Antes de escrever, me diga em até cinco linhas o que a fonte traz e quais páginas você vai criar ou mudar. Depois: o resumo em `wiki/resumos/<nome da fonte> (resumo).md`, as páginas ligadas, uma linha no `index.md` e uma no `log.md`, começando por `## [data] ingest | título`.
3. Se duas fontes não batem, a página diz as duas num bloco que começa por `> [!contradição]`, com o link de cada uma, e você me avisa. Fonte mais nova que diz que algo mudou não é contradição: a página fica com o que vale agora e com a data da mudança.
4. Se uma fonte tiver dado de cliente, valor de contrato, dado pessoal de colega ou senha, você para e me avisa, sem copiar o trecho.
5. Ao encurtar ou reescrever uma página, toda regra que estava nela continua lá, com a mesma fonte.

## Consulta

6. Para responder, leia primeiro o `index.md` e depois as páginas. Cada frase da resposta termina com o link da fonte que a página cita. Se a wiki não tem a resposta, diga isso e diga que fonte faltaria. Se a resposta passa por um bloco de contradição, diga as duas versões e não escolha.
7. Se eu disser "guarde", a resposta vira página em `wiki/respostas/`, entra no `index.md` e ganha uma linha `## [data] query | pergunta` no `log.md`.

## Verificação

8. Quando eu pedir a verificação, leia todas as páginas e me liste três coisas: fontes que não batem e que a wiki não marcou, frases que uma fonte mais nova mudou e assunto citado sem página própria. Para cada item, diga as páginas e as fontes. Não corrija nada antes de eu escolher. No fim, uma linha `## [data] lint | verificação` no `log.md`.

## O que fica comigo

- O terminal e o git. Você não roda comando.
- Este arquivo e a pasta `.claude`. Se uma regra precisar mudar, proponha o texto e espere eu aprovar.

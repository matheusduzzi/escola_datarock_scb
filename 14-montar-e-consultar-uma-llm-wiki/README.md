# Montar e consultar uma LLM Wiki

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `cofre-aurora-wiki/` | O cofre da Renata do jeito que a aula «O cofre como pasta de trabalho do Claude» terminou: notas, `CLAUDE.md`, `.claude/settings.json`, `.gitignore`, as duas fontes de dezembro e a wiki com a `Política de trocas` |
| `fontes-novas/` | As 12 fontes da coleta de devolução, de 25/01 a 05/02/2027. Cada uma entra no cofre na hora da ingestão |
| `verificar_wiki.py` | O script de verificação da wiki. Só lê arquivos |
| `modelos/CLAUDE-consulta-e-verificacao.md` | O esquema novo, com as regras de consulta e de verificação |
| `pedidos-ao-claude.md` | Os pedidos da aula: ingestão, resumos, consulta, guardar e verificação |
| `roteiro.md` | Os comandos na ordem da aula: primeiro commit, uma fonte por vez e o script |
| `pratica-guiada/cofre/` | A cópia da wiki com defeitos, para a prática guiada |
| `minha-entrega.md` | O que você entrega no exercício, em branco |

## Antes de começar

Você precisa do git, do Python 3 (o script usa só o que vem com ele) e de um dos jeitos de o Claude abrir uma pasta, como na aula anterior. Para ver se o Python está instalado, rode `python3 --version`. No Windows, o comando pode ser `py`.

O cofre não traz o histórico do git: o primeiro commit é seu, como na aula anterior. Trabalhe numa cópia da pasta da aula, para poder começar de novo. O script roda da pasta da aula e recebe o caminho do cofre:

```text
python3 verificar_wiki.py cofre-aurora-wiki
```

Ele sai com 0 quando não acha problema, com 1 quando acha e com 2 quando a pasta não tem `fontes/` e `wiki/`.

A Loja Aurora, a Rápido Sul, a Pagare e as fontes são do caso do curso. Os prazos e valores não são de nenhuma transportadora real.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o comando, o que apareceu e o que já tentou. Mande a saída do script e do `git status`, sem o conteúdo das suas notas.

# Projeto final: o segundo cérebro em uso

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `rubrica.md` | A régua do projeto final: as oito linhas, os três problemas que nada compensa e a ficha inicial |
| `rotina-de-manutencao.md` | O modelo da rotina de manutenção, para copiar para o seu cofre e preencher |
| `minha-entrega.md` | O que você entrega no exercício, em branco |
| `pratica-guiada/cofre-da-renata/` | A cópia do cofre da Renata em 28/02/2027, depois de duas semanas de uso, para a prática guiada |
| `pratica-guiada/historico-do-git.txt` | O `git log --stat` e o `git status` desse cofre, como saíram no terminal da Renata |

## Os dois scripts

Essa aula não traz script novo. Ela usa os dois que você já tem, das pastas das aulas 08 e 14 do kit. Os dois só leem arquivos e não mudam nada. Rode da pasta dessa aula:

```text
python3 ../08-atualizar-revisao-semanal-e-limpeza/contar_links.py pratica-guiada/cofre-da-renata
python3 ../14-montar-e-consultar-uma-llm-wiki/verificar_wiki.py pratica-guiada/cofre-da-renata
```

No seu cofre, troque `pratica-guiada/cofre-da-renata` pelo caminho dele. No Windows, o comando pode ser `py` no lugar de `python3`. Se aparecer "Não achei a pasta" ou "No such file", você está em outra pasta no terminal, ou as pastas das aulas 08 e 14 não estão ao lado dessa. Baixe o kit inteiro do curso.

O `verificar_wiki.py` sai com 1 quando acha problema e com 0 quando não acha. No cofre da Renata, o 1 é de propósito: é a prática guiada.

## O cofre da Renata

O cofre não traz a pasta `.git`. O histórico dele está em `historico-do-git.txt`, do jeito que o terminal mostrou. Os ids do seu cofre vão ser outros.

Abra o cofre no Obsidian como nas aulas anteriores, se quiser ver o grafo: ícone do cofre, no canto de baixo à esquerda, Manage Vaults, Open ao lado de Open folder as vault. Faça uma cópia antes, para poder voltar.

## O seu projeto

O exercício é no seu cofre, com as suas notas. A Loja Aurora fica só na prática guiada. Copie `rotina-de-manutencao.md` para uma área do seu cofre e `minha-entrega.md` para fora dele, num lugar seu.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o comando, o que apareceu e o que já tentou. Mande a saída dos scripts e do `git status`, sem o conteúdo das suas notas.

# Pedidos ao Claude

Abra o Claude na raiz do cofre, no modo Manual, como na aula anterior. Copie o pedido e troque o que está entre `<` e `>`.

## Ingestão

```text
Ingira a fonte fontes/<nome do arquivo>.md, seguindo o CLAUDE.md. Antes de escrever, me diga o que ela traz e quais páginas vai criar ou mudar, e espere o meu ok.
```

## Resumos que faltam

```text
As fontes <nome> e <nome> estão sem resumo. Escreva os resumos pela regra 2, sem mudar as outras páginas, e ponha uma linha lint no log.
```

## Consulta

```text
Pela wiki, responda: <pergunta>. Siga a regra 6 do CLAUDE.md.
```

Para guardar a resposta que acabou de sair:

```text
Guarde essa resposta, pela regra 7.
```

## Verificação

```text
Faça a verificação da regra 8 em todas as páginas da wiki. Não corrija nada.
```

## Correção de um item

Depois de decidir, um pedido por item:

```text
Na página wiki/<página>.md, <o que mudar>. Siga as regras 1 e 5 do CLAUDE.md.
```

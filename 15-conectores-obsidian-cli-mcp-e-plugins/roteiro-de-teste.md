# Roteiro do teste de um conector

Faça na ordem. Se um passo mostrar algo que a ficha não previa, pare e volte à ficha.

## Antes

1. Copie o `cofre-aurora-wiki` da aula «Montar e consultar uma LLM Wiki» para uma pasta nova. Trabalhe só na cópia.
2. Abra um terminal na cópia e salve o retrato:

```text
git init
git add .
git commit -m "Antes do conector"
```

3. Abra o `.claude/settings.json` da cópia e deixe o `allow` com o que já estava. As ferramentas do conector entram só no passo 6.

## Ligar

4. Servidor MCP: rode o `claude mcp add` que o README do servidor indica, dentro da pasta da cópia e sem `--scope`. Sem a opção, o servidor fica no escopo local, que vale só para essa pasta.
5. Plugin: abra a cópia como um cofre novo no Obsidian, desligue o modo restrito só nela e instale o plugin. O seu cofre de verdade continua com o modo restrito do jeito que estava.

## Olhar

6. No Claude Code, rode `/mcp` e leia a lista de ferramentas do servidor. Copie para a ficha o nome de cada uma que escreve, apaga ou roda comando.
7. No `settings.json` da cópia, ponha no `allow` só as ferramentas de leitura, com o nome completo `mcp__servidor__ferramenta`. Ponha no `deny` as que apagam e as que rodam comando.
8. Rode `/permissions` e veja se as regras novas estão na lista.

## Pedir

9. Um pedido de leitura na pasta `wiki`. Anote o nome da ferramenta que o Claude chamou e se apareceu pergunta de permissão.
10. Um pedido de escrita na pasta `fontes`, como corrigir um erro de digitação. Se aparecer pergunta de permissão, responda não.
11. Saia do Claude e rode `git status --short -- fontes`. A saída tem de vir vazia: nada mudou na pasta `fontes` desde o commit. Se aparecer um arquivo da `fontes`, o conector escreveu.

O `git status` sem o `-- fontes` vai mostrar mais coisa, e isso é esperado. Aparece o `settings.json` que você mudou no passo 7. Aparece também a pasta `.obsidian`, que o Obsidian cria ao abrir a cópia e ao instalar o plugin. Nada disso veio do pedido de escrita.

## Revogar

12. Servidor MCP: `claude mcp remove` com o nome do servidor, e `claude mcp list` para ver que ele saiu. Se ele usava uma chave, apague a chave no programa que a criou.
13. Plugin: em Configurações, Plugins da comunidade, desligue e desinstale. Veja se a pasta dele saiu de `.obsidian/plugins` na cópia.
14. Obsidian CLI: tire do `allow` as regras de terminal que você pôs para ela. Se não vai mais usar, desligue a opção da CLI em Configurações, Geral.

## Anotar

15. Na linha do teste do `fichas.md`: a data, os dois pedidos, o que apareceu e a saída do `git status --short -- fontes`.

# Três ferramentas, em 08/11/2026, e o serviço de memória

As respostas vêm das páginas oficiais, lidas em 08/11/2026. Antes de usar na sua tabela, abra o link de novo e ponha a sua data.

## A tabela

| Pergunta | Obsidian | Notion | Google Keep |
|---|---|---|---|
| Quem é dono do arquivo | sim: arquivos Markdown numa pasta sua | não: mora no serviço da Notion; você tem cópia quando exporta | não: mora na sua conta Google; você tem cópia quando pede o download |
| Funciona sem internet | sim | em parte: só páginas baixadas, nos apps de computador e celular | em parte: nos apps de celular, não no computador |
| Links entre notas | sim: `[[nome da nota]]` e backlinks | sim: `@` e o nome da página, com backlinks | não: a ajuda não traz link de uma nota para outra |
| Exportação | sim: os arquivos já são Markdown | sim: Markdown e CSV, HTML ou PDF, até o espaço inteiro | em parte: o download traz o conteúdo, mas a ajuda não diz o formato |
| Acesso por IA | sim: pela pasta e pelo Obsidian CLI | sim: pelo Notion MCP, lendo e escrevendo | em parte: só o Gemini |

## De onde veio cada célula

### Obsidian

| Pergunta | O que a página diz | Link |
|---|---|---|
| Quem é dono do arquivo | Cada nota é um arquivo de texto em Markdown dentro do cofre, que é uma pasta do seu computador | https://obsidian.md/help/data-storage |
| Funciona sem internet | As notas ficam no aparelho e abrem mesmo sem conexão | https://obsidian.md/ |
| Links entre notas | Links com colchetes duplos; o Obsidian atualiza os links quando você renomeia a nota. Os backlinks mostram as notas que apontam para a nota aberta | https://obsidian.md/help/links e https://obsidian.md/help/plugins/backlinks |
| Exportação | Como as notas são texto puro, outros editores abrem e mexem nelas | https://obsidian.md/help/data-storage |
| Acesso por IA | O Obsidian CLI lê, busca e cria notas pelo terminal; pede o instalador 1.12 ou mais novo e o Obsidian aberto. O Claude Code lê e edita arquivos de uma pasta | https://obsidian.md/help/cli e https://code.claude.com/docs/en/overview |

Preço na data: gratuito, também no trabalho, sem licença obrigatória. O Sync é pago: 4 dólares por mês no plano anual (https://obsidian.md/pricing).

### Notion

| Pergunta | O que a página diz | Link |
|---|---|---|
| Quem é dono do arquivo | As páginas ficam no serviço; para ter um arquivo no computador, você exporta | https://www.notion.com/help/export-your-content |
| Funciona sem internet | Só nos apps de computador e celular, não no navegador. No plano gratuito, cada página é baixada à mão. Banco de dados baixa só as 50 primeiras linhas da primeira visão | https://www.notion.com/help/use-pages-offline |
| Links entre notas | Digite `@` e o nome da página; a página citada mostra o backlink | https://www.notion.com/help/create-links-and-backlinks |
| Exportação | Markdown e CSV, HTML ou PDF; o espaço inteiro sai pelo computador ou pela web | https://www.notion.com/help/export-your-content |
| Acesso por IA | O Notion MCP liga assistentes como o Claude, que leem e escrevem com todas as permissões da sua conta | https://www.notion.com/help/notion-mcp |

### Google Keep

| Pergunta | O que a página diz | Link |
|---|---|---|
| Quem é dono do arquivo | As notas ficam na conta Google; o download dos dados traz uma cópia | https://support.google.com/keep/answer/10017039 |
| Funciona sem internet | Nos apps de celular, sim; no computador, não | https://support.google.com/keep/answer/10183819 |
| Links entre notas | A ajuda fala de listas, etiquetas, cores, lembretes e compartilhar, sem link de uma nota para outra | https://support.google.com/keep/answer/2888240 |
| Exportação | O download traz texto, listas, anexos, cores e etiquetas, sem as notas apagadas; a página não diz o formato | https://support.google.com/keep/answer/10017039 |
| Acesso por IA | O Gemini, pelo app ou pelo site, cria e acha notas do Keep. A API do Keep é para administradores de empresa. Para o Claude, numa conta pessoal, não há porta oficial na ajuda | https://support.google.com/gemini/answer/15230597 e https://developers.google.com/workspace/keep/api/guides |

## A quarta opção: o serviço de memória, em 12/11/2026

Um programa à parte, ligado ao agente por API ou MCP, que junta fatos por tema. O fato novo vale na busca, e o que tem prazo sai quando vence. As respostas vêm das páginas oficiais lidas em 12/11/2026.

| Pergunta | Cofre de arquivos (Obsidian) | Serviço de memória (Supermemory) |
|---|---|---|
| Dono do dado | sim: arquivos numa pasta sua | depende: na nuvem, mora no serviço; na versão que você mesmo roda, fica com você |
| Troca de agente | sim: qualquer assistente que abre a pasta | sim: o mesmo MCP serve vários assistentes |
| Histórico sem sobrescrever | em parte: cópias de 7 dias no Obsidian; todas as versões com o git | sim: o fato novo vale na busca, e o antigo fica |
| Custo | gratuito; o Sync é pago | 5 dólares de uso por mês grátis; o plano Pro custa 19 dólares por mês |

| Pergunta | O que a página diz | Link |
|---|---|---|
| Dono do dado, cofre | Cada nota é um arquivo Markdown numa pasta do seu computador | https://obsidian.md/help/data-storage |
| Dono do dado, serviço | Roda na nuvem do serviço ou na sua máquina, num programa só | https://supermemory.ai/docs/intro |
| Troca de agente, cofre | O Claude Code lê e edita os arquivos de uma pasta | https://code.claude.com/docs/en/overview |
| Troca de agente, serviço | O MCP lê e grava memórias e leva o contexto de um assistente para outro | https://supermemory.ai/docs/supermemory-mcp/mcp |
| Histórico, cofre | A recuperação de arquivos guarda cópias das notas, no padrão por 7 dias | https://obsidian.md/help/plugins/file-recovery |
| Histórico, serviço | O fato novo vale na busca sem apagar o antigo; fatos temporários caem quando expiram | https://supermemory.ai/docs/concepts/graph-memory |
| Custo, cofre | Gratuito, também no trabalho; o Sync custa 4 dólares por mês no plano anual | https://obsidian.md/pricing |
| Custo, serviço | Plano grátis com 5 dólares de uso por mês; Pro a 19 dólares por mês | https://supermemory.ai/pricing |

Outro serviço do mesmo tipo é o Mem0, com uma versão que roda na sua própria máquina (https://docs.mem0.ai/open-source/overview).

Antes de trocar, responda: eu gasto mais tempo mantendo do que usando? A resposta vem da sua conta da aula «Para que serve e quanto custa manter».

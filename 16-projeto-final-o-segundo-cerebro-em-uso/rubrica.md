# Rubrica do projeto final

É a mesma régua da apresentação do curso. Use antes de entregar: passe linha por linha no seu cofre, com o `minha-entrega.md` aberto ao lado.

## As oito linhas

Cada linha precisa aparecer. Uma linha forte não cobre outra que falta.

| Linha | O que precisa aparecer | Como ver | Aula |
|---|---|---|---|
| Estrutura | Pastas de projetos, áreas, recursos e arquivo, com notas ligadas e nenhuma nota perdida na raiz | A árvore de pastas e a contagem do `contar_links.py`: na raiz, só o esquema e a lista do que fica fora, ou o que você explicar | 05 e 07 |
| Captura | Duas semanas de entradas, de pelo menos três canais, e a regra do que vale guardar | As notas têm `origem` e `capturado`. As datas de `capturado` cobrem duas semanas de calendário, com entradas em cada uma, e há três valores diferentes de `origem` | 06 |
| Manutenção | Uma revisão semanal feita, com o antes e o depois da caixa de entrada e dos links quebrados | A nota da revisão, com a tabela de antes e depois e o que você fez com cada nota da caixa | 08 |
| LLM Wiki | Fontes suas numa pasta, a wiki com páginas ligadas, o arquivo de esquema e três respostas que citam a fonte | Cinco fontes ou mais em `fontes/`, cada uma com resumo; duas páginas de assunto ou mais, ligadas entre si; o `CLAUDE.md`; três respostas com o link da fonte no fim de cada frase e o trecho da fonte copiado | 12 e 14 |
| Checagem | Um relatório da wiki com links quebrados, contradições e páginas sem fonte, e o que você fez com cada um | A saída do `verificar_wiki.py` em 0, a lista da verificação da regra 8 e uma decisão sua para cada item | 14 |
| Controle | O Claude escreve só na pasta da wiki, e o histórico do git mostra uma edição desfeita | O `.claude/settings.json`, o `git log --stat` com os commits do Claude só em `wiki/` e um `Revert` | 13 |
| Limites | A lista do que fica fora do cofre e da IA, com o motivo | A nota com a lista, e a caixa de entrada lida contra ela antes do commit | 10 e 11 |
| Rotina | Quando você captura, quando revisa e quando roda a checagem, com o tempo por semana que você aceita | A nota da rotina, com dia, hora e minutos por semana, e o total dentro do tempo da aula 03 | 03 e 16 |

## Os três que nada compensa

A entrega precisa de ajuste, mesmo com as outras linhas boas, quando:

1. **A wiki responde sem citar a fonte.** Uma frase de resposta sem o link da fonte, ou com um link que não diz aquilo, já pede ajuste. Sem a fonte, você não consegue checar a resposta em um clique, e a wiki vira palpite.
2. **O Claude pode escrever fora da pasta da wiki.** Vale para o `settings.json` com permissão de edição fora de `wiki/`. Vale também para um commit do Claude que mexeu em outra pasta e não foi desfeito. Uma edição dele numa nota sua mistura o que você escreveu com o que ele escreveu.
3. **Entra no cofre algo da lista do que fica fora.** Um nome de cliente, uma senha, um valor de contrato, um dado de saúde. O cofre vai para o backup, para a sincronização e para a IA, e cada cópia leva o dado junto.

Achou um dos três? Corrija, rode a checagem de novo e só então entregue. Se o problema já tinha entrado num commit, diga isso na entrega.

## Se você usa o Cowork

A trava por pasta do `settings.json` vale para o Claude Code. No Cowork, escreva o `settings.json` assim mesmo, marque a trava como "não testado" e mostre pelo `git log --oneline --name-only --grep="^Claude:"` que cada commit do Claude só mexeu em `wiki/`. A linha Controle fica atendida com essas duas coisas.

## A ficha inicial

Abra a ficha que você preencheu na apresentação do curso. Para cada situação da parte 3, escreva "consegui" ou "ainda não", com a nota ou a página do cofre que mostra. "Ainda não" não reprova o projeto: diz o que entra primeiro no próximo mês.

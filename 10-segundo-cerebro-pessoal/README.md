# Segundo cérebro pessoal

Arquivos da aula:

| Arquivo | Para que serve |
|---|---|
| `cofres-da-renata/Renata pessoal/` | O cofre pessoal da Renata em 13/12, o que vai para o iCloud: estudos, leituras, metas e finanças sem valores, com as notas `Regra de privacidade` e `Backup` |
| `cofres-da-renata/Renata privado/` | O cofre que fica só no Mac dela: diário, valores e saúde |
| `backups/2026-11-30 Renata.zip` | O primeiro backup, o que falhou no teste |
| `backups/2026-12-06 Renata.zip` | O backup das duas pastas, para a prática guiada |
| `modelo-area-pessoal/` | O ponto de partida do exercício: as pastas `Pessoal` e `Privado`, com os modelos e as notas `Regra de privacidade` e `Backup` para preencher |
| `checklist-privacidade-e-backup.md` | As perguntas da regra e os passos do teste, para usar no exercício e depois, todo mês |

Tudo aqui é inventado para o curso, inclusive os valores das contas da Renata.

## Abrir um cofre

Cada pasta, `Renata pessoal`, `Renata privado`, `Pessoal` e `Privado`, é um cofre separado. No Obsidian, clique no ícone do cofre, no canto de baixo à esquerda, escolha Manage Vaults e clique em Open, ao lado de Open folder as vault. Depois escolha a pasta. Os nomes dos menus estão como na ajuda do Obsidian, em inglês.

Os cofres do kit não trazem as configurações do Obsidian. Para usar os modelos, escreva `Modelos` em Settings, Templates, Template folder location. Para o diário, ligue o plugin Daily notes e aponte New file location para `Diário` e Template file location para `Modelos/Diário`, no cofre `Privado`.

## Prática guiada: restaurar o backup de 06/12

Descompacte `backups/2026-12-06 Renata.zip` numa pasta nova, chamada `Restaurado`, dentro da pasta dessa aula e fora de `cofres-da-renata`.

- **Mac:** dê dois cliques no zip. Aparece uma pasta `2026-12-06 Renata`; renomeie para `Restaurado`.
- **Windows:** botão direito no zip, Extrair tudo, e escolha uma pasta `Restaurado`.
- **Terminal (Mac e Linux):** na pasta dessa aula, rode `unzip "backups/2026-12-06 Renata.zip" -d Restaurado`.

Para contar os arquivos, use o mesmo jeito dos dois lados: Obter Informações no Mac ou Propriedades no Windows, na pasta restaurada e na pasta de `cofres-da-renata`.

No Mac e no Linux, este comando lista o que muda entre o cofre de hoje e o backup:

```bash
diff -rq "cofres-da-renata/Renata pessoal" "Restaurado/Renata pessoal"
diff -rq "cofres-da-renata/Renata privado" "Restaurado/Renata privado"
```

`Only in cofres-da-renata/...` é um arquivo que só existe hoje. `Only in Restaurado/...` só existe no backup. `Files ... differ` é um arquivo que mudou depois do backup. Sem nenhuma linha, as duas pastas são iguais.

Quando terminar, apague a pasta `Restaurado`. No seu backup de verdade, ela é uma cópia do seu privado.

## Exercício

Copie a pasta `modelo-area-pessoal` para fora do kit e trabalhe na cópia. A pasta `Pessoal` vai para onde você sincroniza; a `Privado`, para um lugar que não sincroniza. A aula mostra como escolher. Apague as notas `Leia antes` quando a primeira nota de verdade entrar em cada pasta.

## Ajuda

Se travar, deixe um comentário na aula com o objetivo, o que você fez, o que apareceu e o que já tentou. Descreva onde estão as suas pastas e o resultado do teste. Não cole nenhuma nota do seu privado.


# Telegram Bot de Ferramentas

Este é um simples bot de Telegram que permite executar ferramentas diretamente de um grupo. Ele é útil para automação e colaboração em projetos de segurança e desenvolvimento.

## Instruções de Uso

1. Inicie uma conversa com o bot ou adicione-o a um grupo.
2. Use os seguintes comandos seguidos pelos argumentos necessários:

   - `/start`: Inicia a conversa e fornece instruções.
   - `/katana <argumentos>`: Executa a ferramenta Katana.
   - `/httpx <argumentos>`: Executa a ferramenta HTTPx.
   - `/subfinder <argumentos>`: Executa a ferramenta Subfinder.
   - `/ffuf <argumentos>`: Executa a ferramenta FFuF.

## Configuração

Antes de usar o bot, siga estas etapas de configuração:

1. Obtenha um token do Telegram para o bot.
2. Substitua `"TOKEN"` na variável `telegram_token` pelo token obtido.
3. Defina o `group_id` com o ID do grupo em que deseja enviar mensagens.

## Requisitos

Certifique-se de ter as ferramentas Katana, HTTPx, Subfinder e FFuF instaladas e acessíveis no ambiente onde este bot será executado.

## Observações

- Certifique-se de que o bot tenha permissões adequadas para enviar mensagens no grupo especificado.
- Este bot não lida com erros de entrada ou saída de ferramentas, portanto, verifique se os argumentos fornecidos estão corretos.

## Aviso

Este bot foi criado para fins educacionais e de teste. Use-o com responsabilidade e respeite os Termos de Serviço do Telegram.

## Licença

Este projeto é distribuído sob a [licença MIT](https://opensource.org/licenses/MIT). Sinta-se à vontade para modificar e redistribuir conforme necessário.

--- 

Isso deve fornecer uma documentação clara e concisa para os usuários que visitam o seu repositório no GitHub.

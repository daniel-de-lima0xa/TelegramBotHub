# TELEGRAM NMAP BOT

Este é um bot para o Telegram que permite realizar scans Nmap diretamente do aplicativo. Desenvolvido em Python, utilizando a biblioteca [python-telegram-bot](https://python-telegram-bot.readthedocs.io/), este bot pode ser facilmente integrado e personalizado para atender às suas necessidades.

## COMO UTILIZAR

1. **Iniciando uma Conversa com o Bot:**
   - Procure por `@seu_bot_nmap_bot` no Telegram e inicie uma conversa com o bot.

2. **Enviando Comandos do Nmap:**
   - Utilize o comando `/nmap` seguido dos argumentos desejados para o Nmap. Por exemplo:
     ```plaintext
     /nmap -sT scanme.nmap.org
     ```

3. **Recebendo Resultados:**
   - O bot executará o Nmap com base nos argumentos fornecidos e enviará o resultado formatado de volta para você.

## COMANDOS DISPONÍVEIS

- `/start`: Inicia a conversa com o bot e fornece instruções básicas.
- `/nmap <flags> <alvo>`: Executa o Nmap com os argumentos fornecidos e retorna o resultado.

## CONFIGURAÇÃO

Certifique-se de ajustar as seguintes variáveis no script para a configuração adequada:

```python
# Token do Telegram (substitua pelo seu)
telegram_token = "SEU_TOKEN_AQUI"

# ID do grupo
group_id = -1234567890  # Substitua pelo ID do seu grupo


REQUISITOS
Certifique-se de instalar as dependências necessárias antes de executar o bot. Você pode instalá-las utilizando o seguinte comando:

  pip install python-telegram-bot

NOTAS IMPORTANTES
Este bot foi desenvolvido para fins educacionais e de aprendizado.
Certifique-se de obedecer aos termos de serviço do Telegram ao usar este bot.
Sinta-se à vontade para personalizar, expandir ou contribuir para este projeto!

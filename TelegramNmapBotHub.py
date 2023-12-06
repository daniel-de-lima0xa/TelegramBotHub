# -*- coding: utf-8 -*-

import subprocess
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import logging
import os

# Configuração do logger
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Token do Telegram (substitua pelo seu)
telegram_token = "TOKEN"

# ID do grupo
group_id = id_grupo


def start(update: Update, context: CallbackContext) -> None:
    """Envia mensagem de boas-vindas e instruções ao usuário."""
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"Olá, usuário {user_id}! Envie comandos do Nmap no formato /nmap <flags> <alvo>.\n\nExemplo: /nmap -sT scanme.nmap.org"
    )


def nmap(update: Update, context: CallbackContext) -> None:
    """Executa Nmap com base nos argumentos fornecidos e envia o resultado ao usuário."""
    try:
        # Extraindo argumentos do comando
        args = context.args

        # Verificando se há argumentos
        if not args:
            update.message.reply_text(
                "Por favor, forneça os argumentos do Nmap. Exemplo: /nmap -sT scanme.nmap.org"
            )
            return

        # Construindo o comando Nmap
        nmap_command = ["nmap"] + args

        # Executando o comando e obtendo a saída
        result = subprocess.check_output(nmap_command)

        # Decodificando e formatando a saída
        formatted_result = result.decode("utf-8").replace("_", "\\_")

        # Enviando o resultado formatado para o usuário
        update.message.reply_text(
            f"**Resultado Nmap**\n\n{formatted_result}\n", parse_mode="Markdown"
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao executar o Nmap: {e.output.decode('utf-8')}")
        update.message.reply_text(
            "Erro ao executar o Nmap. Verifique os argumentos e tente novamente."
        )


def main() -> None:
    """Inicia o bot do Telegram."""
    updater = Updater(token=telegram_token, use_context=True)
    dp = updater.dispatcher

    # Adicionando handlers para os comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("nmap", nmap, pass_args=True))

    # Enviando mensagem para o grupo
    updater.bot.send_message(chat_id=group_id, text="Olá, grupo!")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

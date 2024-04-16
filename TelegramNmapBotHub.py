import subprocess
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import logging

# Configuração do logger
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Token do Telegram
telegram_token = "TOKEN"

# ID do grupo
group_id = "ID_DO_GRUPO"


def start(update: Update, context: CallbackContext) -> None:
    """Envia mensagem de boas-vindas e instruções ao usuário."""
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"Olá, usuário {user_id}! Envie comandos das ferramentas no formato /ferramenta <argumentos>."
    )


def execute_tool(update: Update, context: CallbackContext) -> None:
    """Executa a ferramenta com base nos argumentos fornecidos e envia o resultado ao usuário."""
    try:
        # Extraindo argumentos do comando
        args = context.args

        # Verificando se há argumentos
        if not args:
            update.message.reply_text(
                "Por favor, forneça os argumentos da ferramenta."
            )
            return

        # Obtendo o nome da ferramenta a partir do comando
        tool_name = context.args[0]

        # Construindo o comando da ferramenta
        tool_command = [tool_name] + args[1:]

        # Executando o comando e obtendo a saída
        result = subprocess.check_output(tool_command)

        # Decodificando e formatando a saída
        formatted_result = result.decode("utf-8").replace("_", "\\_")

        # Enviando o resultado formatado para o usuário
        update.message.reply_text(
            f"**Resultado da ferramenta {tool_name}**\n\n{formatted_result}\n", parse_mode="Markdown"
        )
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao executar a ferramenta: {e.output.decode('utf-8')}")
        update.message.reply_text(
            f"Erro ao executar a ferramenta. Verifique os argumentos e tente novamente."
        )


def main() -> None:
    """Inicia o bot do Telegram."""
    updater = Updater(token=telegram_token, use_context=True)
    dp = updater.dispatcher

    # Adicionando handlers para os comandos das ferramentas
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("katana", execute_tool, pass_args=True))
    dp.add_handler(CommandHandler("httpx", execute_tool, pass_args=True))
    dp.add_handler(CommandHandler("subfinder", execute_tool, pass_args=True))
    dp.add_handler(CommandHandler("ffuf", execute_tool, pass_args=True))

    # Enviando mensagem para o grupo
    updater.bot.send_message(chat_id=group_id, text="Olá, grupo!")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

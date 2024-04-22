import subprocess
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, ReplyKeyboardMarkup
import logging
import time

# Configuração do logger
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Token do Telegram
telegram_token = "token"

# ID do grupo
group_id = id chat

# Opções do menu
menu_options = [["Nmap", "Naabu", "Waybackurls"], ["Subfinder"], ["Katana"]]


def start(update: Update, context: CallbackContext) -> None:
    """Envia mensagem de boas-vindas e instruções ao usuário."""
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"Olá, usuário {user_id}! Envie /menu para exibir as opções disponíveis."
    )


def menu(update: Update, context: CallbackContext) -> None:
    """Exibe o menu de opções."""
    keyboard = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
    update.message.reply_text(
        "Escolha uma opção:",
        reply_markup=keyboard
    )


def execute_command(command: list[str]) -> str:
    """Executa um comando e retorna a saída."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Erro ao executar o comando: {e}")
        return f"Erro ao executar o comando: {e}"


def katana(update: Update, context: CallbackContext) -> None:
    """Executa a ferramenta Katana e envia o resultado ao usuário."""
    try:
        args = context.args
        url_index = args.index('-u') if '-u' in args else None
        number_index = args.index('-d') if '-d' in args else None

        if url_index is not None and number_index is not None:
            url = args[url_index + 1]
            number = args[number_index + 1]
            result = execute_command(["katana", "-u", url, "-d", number])
            update.message.reply_text(f"**Resultado Katana**\n\n{result}\n", parse_mode="Markdown")
        else:
            update.message.reply_text("Por favor, forneça uma URL e um número usando '-u' e '-d'.")
    except ValueError:
        update.message.reply_text("Por favor, forneça uma URL e um número usando '-u' e '-d'.")


def nmap(update: Update, context: CallbackContext) -> None:
    """Executa o Nmap com base nos argumentos fornecidos e envia o resultado ao usuário."""
    result = execute_command(["nmap"] + context.args)
    update.message.reply_text(f"**Resultado Nmap**\n\n{result}\n", parse_mode="Markdown")


def subfinder(update: Update, context: CallbackContext) -> None:
    """Executa o Subfinder com base nos argumentos fornecidos e envia o resultado ao usuário."""
    result = execute_command(["subfinder"] + context.args)
    update.message.reply_text(f"**Resultado Subfinder**\n\n{result}\n", parse_mode="Markdown")


def naabu(update: Update, context: CallbackContext) -> None:
    """Executa o Naabu com base nos argumentos fornecidos e envia o resultado ao usuário."""
    result = execute_command(["naabu"] + context.args)
    update.message.reply_text(f"**Resultado Naabu**\n\n{result}\n", parse_mode="Markdown")


def waybackurls(update: Update, context: CallbackContext) -> None:
    """Executa o Waybackurls com base no site fornecido como argumento e envia o resultado ao usuário."""
    try:
        # Verifica se o site foi fornecido como argumento
        if len(context.args) < 1:
            update.message.reply_text("Por favor, forneça o site como argumento. Exemplo: /waybackurls example.com")
            return

        # Extrai o site do argumento
        site = context.args[0]

        # Executa o Waybackurls para o site fornecido
        result = execute_command(["waybackurls", site])

        # Divide o resultado em partes menores para enviar em várias mensagens
        max_message_length = 4096  # Tamanho máximo permitido para uma mensagem do Telegram
        for i in range(0, len(result), max_message_length):
            update.message.reply_text(f"**Resultado Waybackurls para {site} (Parte {i//max_message_length+1})**\n\n{result[i:i+max_message_length]}\n", parse_mode="Markdown")
            time.sleep(1)  # Adiciona um pequeno atraso entre as mensagens para evitar problemas de taxa limite
    except Exception as e:
        logger.error(f"Erro ao executar o comando Waybackurls: {e}")
        update.message.reply_text(f"Ocorreu um erro ao executar o comando Waybackurls: {e}")


def main() -> None:
    """Inicia o bot do Telegram."""
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("katana", katana, pass_args=True))
    dispatcher.add_handler(CommandHandler("nmap", nmap, pass_args=True))
    dispatcher.add_handler(CommandHandler("subfinder", subfinder, pass_args=True))
    dispatcher.add_handler(CommandHandler("naabu", naabu, pass_args=True))
    dispatcher.add_handler(CommandHandler("waybackurls", waybackurls, pass_args=True))  # Adicionando suporte para Waybackurls

    updater.bot.send_message(chat_id=group_id, text="Olá, grupo!")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

import subprocess
import logging
from typing import List
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import Update, ParseMode, ReplyKeyboardMarkup
import time

# Configurações
class Config:
    TELEGRAM_TOKEN = "TOKEN"
    GROUP_ID = chat_id

    MENU_OPTIONS = [["Nmap", "Naabu", "Ffuf"], ["Subfinder"], ["Katana"]]

# Configuração para logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Função para executar comandos e capturar a saída
def execute_command(command: List[str]) -> str:
    try:
        logger.info(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {e}")
        return f"Error executing command: {e}"

# Função para enviar mensagens, dividindo em partes se necessário
def send_message(update: Update, message: str) -> None:
    if update.message:
        update.message.reply_text(message, parse_mode=ParseMode.MARKDOWN)
    elif update.callback_query:
        update.callback_query.answer(message, parse_mode=ParseMode.MARKDOWN)

# Handlers dos comandos
def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"Hello, user {user_id}! Send /menu to view available options."
    )

def menu(update: Update, context: CallbackContext) -> None:
    keyboard = ReplyKeyboardMarkup(Config.MENU_OPTIONS, one_time_keyboard=True)
    update.message.reply_text(
        "Choose an option:",
        reply_markup=keyboard
    )



def katana(update: Update, context: CallbackContext) -> None:
    try:
        args = context.args

        # Verifica se o argumento "-o" está presente
        if '-o' in args:
            # Localiza o índice do argumento "-o"
            index_o = args.index('-o')

            # Verifica se há um caminho de arquivo após o argumento "-o"
            if index_o + 1 < len(args):
                output_file = args[index_o + 1]

                # Executa o comando katana com os argumentos fornecidos
                result = execute_command(["katana"] + args)

                # Salva a saída do comando em um arquivo especificado pelo usuário
                with open(output_file, 'w') as f:
                    f.write(result)

                update.message.reply_text(f"A saída foi salva em: {output_file}. O arquivo foi finalizado.")
                return

            else:
                update.message.reply_text("Por favor, forneça um caminho de arquivo após o argumento '-o'.")
                return
        else:
            # Se o argumento "-o" não estiver presente, executa o comando katana e envia a saída diretamente para o bot
            result = execute_command(["katana"] + args)
            results = result.split('\n')

            # Dividir os resultados em partes menores (por exemplo, 10 linhas por mensagem)
            tamanho_parte = 30
            for i in range(0, len(results), tamanho_parte):
                parte = results[i:i+tamanho_parte]
                parte_formatada = "\n".join(parte)
                send_message(update, f"```\n{parte_formatada}\n```")
                time.sleep(1)  # Atraso de 1 segundo entre cada mensagem

    except Exception as e:
        logger.error(f"Erro ao executar o comando Katana: {e}")
        send_message(update, f"Ocorreu um erro ao executar o comando Katana: {e}")


        # Se o argumento "-o" não estiver presente, executa o comando katana e envia a saída diretamente para o bot
        result = execute_command(["katana"] + args)
        send_message(update, f"```\n{result}\n```")

    except Exception as e:
        logger.error(f"Erro ao executar o comando Katana: {e}")
        send_message(update, f"Ocorreu um erro ao executar o comando Katana: {e}")

def nmap(update: Update, context: CallbackContext) -> None:
    try:
        args = context.args
        if args:
            result = execute_command(["nmap"] + args)
            results = result.split('\n')

            # Dividir os resultados em partes menores (por exemplo, 10 linhas por mensagem)
            tamanho_parte = 30
            for i in range(0, len(results), tamanho_parte):
                parte = results[i:i+tamanho_parte]
                parte_formatada = "\n".join(parte)
                send_message(update, f"```\n{parte_formatada}\n```")
        else:
            update.message.reply_text("Por favor, forneça argumentos para o Nmap.")
    except Exception as e:
        logger.error(f"Erro ao executar o comando Nmap: {e}")
        send_message(update, f"Ocorreu um erro ao executar o comando Nmap: {e}")


def subfinder(update: Update, context: CallbackContext) -> None:
    try:
        logger.info("Executing Subfinder command")
        result = execute_command(["subfinder"] + context.args)
        results = result.split('\n')
        for res in results:
            if res.strip():
                send_message(update, f"```\n{res}\n```")
    except Exception as e:
        logger.error(f"Error executing Subfinder command: {e}")
        send_message(update, f"An error occurred while executing the Subfinder command: {e}")

def ffuf(update: Update, context: CallbackContext) -> None:
    try:
        logger.info("Executing Ffuf command")
        result = execute_command(["ffuf"] + context.args)
        if result.strip():
            results = result.split('\n')

            # Dividir os resultados em partes menores (por exemplo, 10 linhas por mensagem)
            tamanho_parte = 30
            for i in range(0, len(results), tamanho_parte):
                parte = results[i:i+tamanho_parte]
                parte_formatada = "\n".join(parte)
                send_message(update, f"```\n{parte_formatada}\n```")
                time.sleep(1)  # Atraso de 1 segundo
        else:
            send_message(update, "Nenhum resultado encontrado.")
    except Exception as e:
        logger.error(f"Erro ao executar o comando Ffuf: {e}")
        send_message(update, f"Ocorreu um erro ao executar o comando Ffuf: {e}")


def naabu(update: Update, context: CallbackContext) -> None:
    try:
        logger.info("Executing Naabu command")
        result = execute_command(["naabu"] + context.args)
        results = result.split('\n')

        # Dividir os resultados em partes menores (por exemplo, 10 linhas por mensagem)
        tamanho_parte = 30
        for i in range(0, len(results), tamanho_parte):
            parte = results[i:i+tamanho_parte]
            parte_formatada = "\n".join(parte)
            send_message(update, f"```\n{parte_formatada}\n```")
            time.sleep(1)  # Atraso de 1 segundo entre cada mensagem
            # Aguarde até que a mensagem anterior seja enviada antes de enviar a próxima
    except Exception as e:
        logger.error(f"Error executing Naabu command: {e}")
        send_message(update, f"An error occurred while executing the Naabu command: {e}")



def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sorry, I didn't understand that command.")

# Função de inicialização do bot
def main() -> None:
    updater = Updater(token=Config.TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("katana", katana, pass_args=True))
    dispatcher.add_handler(CommandHandler("nmap", nmap, pass_args=True))
    dispatcher.add_handler(CommandHandler("subfinder", subfinder, pass_args=True))
    dispatcher.add_handler(CommandHandler("ffuf", ffuf, pass_args=True))
    dispatcher.add_handler(CommandHandler("naabu", naabu, pass_args=True))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.bot.send_message(chat_id=Config.GROUP_ID, text="Hello, group!")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

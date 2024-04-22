import subprocess
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update, ParseMode, ReplyKeyboardMarkup
import logging

# Configuration for logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram token
telegram_token = "token"

# Group ID
group_id = id_chat

# Menu options (including Ffuf)
menu_options = [["Nmap", "Naabu", "Ffuf"], ["Subfinder"], ["Katana"]]


def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message and instructions to the user."""
    user_id = update.message.from_user.id
    update.message.reply_text(
        f"Hello, user {user_id}! Send /menu to view available options."
    )


def menu(update: Update, context: CallbackContext) -> None:
    """Displays the menu options."""
    keyboard = ReplyKeyboardMarkup(menu_options, one_time_keyboard=True)
    update.message.reply_text(
        "Choose an option:",
        reply_markup=keyboard
    )


def execute_command(command: list[str]) -> str:
    """Executes a command and returns the output."""
    try:
        logger.info(f"Executing command: {' '.join(command)}")
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.strip()
        return output
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {e}")
        return f"Error executing command: {e}"


def katana(update: Update, context: CallbackContext) -> None:
    """Executes the Katana tool and sends the result to the user."""
    try:
        args = context.args
        url_index = args.index('-u') if '-u' in args else None
        number_index = args.index('-d') if '-d' in args else None

        if url_index is not None and number_index is not None:
            url = args[url_index + 1]
            number = args[number_index + 1]
            result = execute_command(["katana", "-u", url, "-d", number])
            update.message.reply_text(f"**Katana Result**\n\n```\n{result}\n```\n", parse_mode=ParseMode.MARKDOWN_V2)
        else:
            update.message.reply_text("Please provide a URL and a number using '-u' and '-d'.")
    except ValueError:
        update.message.reply_text("Please provide a URL and a number using '-u' and '-d'.")


def nmap(update: Update, context: CallbackContext) -> None:
    """Executes Nmap based on the provided arguments and sends the result to the user."""
    result = execute_command(["nmap"] + context.args)
    update.message.reply_text(f"**Nmap Result**\n\n```\n{result}\n```\n", parse_mode=ParseMode.MARKDOWN_V2)


def subfinder(update: Update, context: CallbackContext) -> None:
    """Executes Subfinder based on the provided arguments and sends the result to the user."""
    try:
        logger.info(f"Executing Subfinder command with args: {context.args}")
        result = execute_command(["subfinder"] + context.args)
        logger.info(f"Subfinder command result: {result}")

        update.message.reply_text(f"**Subfinder Result**\n\n```\n{result}\n```\n", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        logger.error(f"Error executing Subfinder command: {e}")
        update.message.reply_text(f"An error occurred while executing the Subfinder command: {e}")


def ffuf(update: Update, context: CallbackContext) -> None:
    """Executes Ffuf based on the provided arguments and sends the result to the user."""
    try:
        result = execute_command(["ffuf"] + context.args)
        update.message.reply_text(f"**Ffuf Result**\n\n```\n{result}\n```\n", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        logger.error(f"Error executing Ffuf command: {e}")
        update.message.reply_text(f"An error occurred while executing the Ffuf command: {e}")


def naabu(update: Update, context: CallbackContext) -> None:
    """Executes Naabu based on the provided arguments and sends the result to the user."""
    try:
        result = execute_command(["naabu"] + context.args)
        update.message.reply_text(f"**Naabu Result**\n\n```\n{result}\n```\n", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        logger.error(f"Error executing Naabu command: {e}")
        update.message.reply_text(f"An error occurred while executing the Naabu command: {e}")


def main() -> None:
    """Starts the Telegram bot."""
    updater = Updater(token=telegram_token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("menu", menu))
    dispatcher.add_handler(CommandHandler("katana", katana, pass_args=True))
    dispatcher.add_handler(CommandHandler("nmap", nmap, pass_args=True))
    dispatcher.add_handler(CommandHandler("subfinder", subfinder, pass_args=True))
    dispatcher.add_handler(CommandHandler("ffuf", ffuf, pass_args=True))  # Adding support for Ffuf
    dispatcher.add_handler(CommandHandler("naabu", naabu, pass_args=True))  # Adding support for Naabu

    updater.bot.send_message(chat_id=group_id, text="Hello, group!")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

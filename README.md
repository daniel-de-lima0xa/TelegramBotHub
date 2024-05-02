# Telegram Bot de Ferramentas

This is a simple Telegram bot that allows you to execute tools directly from a group. It is useful for automation and collaboration in security and development projects.

## Usage Instructions

1. Start a conversation with the bot or add it to a group.
2. Use the following commands followed by the necessary arguments:

   - `/start`: Starts the conversation and provides instructions.
   - `/katana <arguments>`: Executes the Katana tool.
   - `/httpx <arguments>`: Executes the HTTPx tool.
   - `/subfinder <arguments>`: Executes the Subfinder tool.
   - `/ffuf <arguments>`: Executes the FFuF tool.
   - `/naabu <arguments>`: Executes the naabu tool.

## Configuration

Before using the bot, follow these setup steps:

1. Obtain a Telegram token for the bot.
2. Replace `"TOKEN"` in the `telegram_token` variable with the obtained token.
3. Set the `group_id` with the ID of the group where you want to send messages.

## Requirements

Make sure you have the Katana, HTTPx, Subfinder, and FFuF tools installed and accessible in the environment where this bot will be running.

## Notes

- Ensure that the bot has proper permissions to send messages in the specified group.
- This bot does not handle tool input or output errors, so make sure the provided arguments are correct.

## Demonstration
![telegram](https://github.com/daniel-de-lima0xa/TelegramBotHub/assets/59209081/bf0c2764-64a3-49ac-aa39-9f51357beb16)

## Disclaimer

This bot was created for educational and testing purposes. Use it responsibly and respect the Telegram Terms of Service.

## License

This project is distributed under the [MIT license](https://opensource.org/licenses/MIT). Feel free to modify and redistribute as needed.

----

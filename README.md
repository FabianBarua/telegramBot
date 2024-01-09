# Python Telegram Bot 🤖

This Python script utilizes the `telebot` library to create a Telegram bot that generates invitation links for different chat types.

## Description ℹ️

The bot provides functionality to generate invitation links for specific types of chats, interactively using inline keyboards in Telegram. It allows administrators to easily create invite links for clients and resellers.

## Installation 🚀

1. Clone or download the repository.
2. Install the required dependencies using pip:
 ```bash
 pip install python-telegram-bot python-dotenv
 ```
3. Create a .env file and add the necessary environment variables (TOKEN, CHAT_C, CHAT_R, etc.).
4. Run the Python script:
```bash
python your_script_name.py
```

## Usage

1. Ensure the bot is running and reachable on Telegram.
2. Send the command `/gen` to start the process.
3. Select the number of links you want to generate using the provided keyboard.
4. Choose the chat type for which you want to generate invitation links.
5. Receive and share the generated links accordingly.

## Configuration ⚙️

Make sure to set up the following environment variables in the `.env` file:

- `TOKEN`: Your Telegram bot token.
- `CHAT_C`: ID of the clients' chat.
- `CHAT_R`: ID of the resellers' chat.
- Other necessary variables as required by your implementation.

## Contributing 🤝

Contributions to improve the bot's functionality are welcome! Fork the repository, make your changes, and create a pull request.

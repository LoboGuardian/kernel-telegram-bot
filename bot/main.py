#!/bin/env python
#-*-coding:UTF-8-*-
# bot/main.py
#
# Made by LoboGuardian
# Follow me on https://github.com/LoboGuardian

"""
This is the main entry point for the Telegram bot. It sets up the bot
using the Telegram API and manages command handling.

Version Handling:
-----------------
Defines the version of the bot as a global variable.

Dependencies:
-------------
- Third-party libraries: It's using the Telegram API library to
  handle messages and commands.
- Local imports: Imports configuration and command modules.

Key Functions:
--------------
1. main: Initializes the bot and sets up command handlers.
2. on_startup: Sends a notification when the bot starts.

Global Variables:
-----------------
- VERSION: The version of the bot.
- TOKEN: The API token for authenticating the bot with the Telegram API.
- COMMANDS: A list of commands supported by the bot.

Usage:
------
Run this script to start the bot.
"""
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
# Third-party libraries
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters

# from bot.config import ApplicationBuilder, CommandHandler, filters
from config import TOKEN
from handlers import start, help, unknown, errors
# from utils.logger import configure_logging

def main() -> None:
    """Initialize the bot and register handlers."""
    app = ApplicationBuilder().token(TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start.start_command))
    app.add_handler(CommandHandler("help", help.help_command))

    # Error and unknown command handlers
    app.add_handler(MessageHandler(filters.COMMAND, unknown.unknown_handle_command))
    app.add_error_handler(errors.error_handler_command)

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
from telethon import TelegramClient

async def process_message(message, channel_name, logger, client, target_bot_username):
    """
    Verarbeitet Nachrichten und leitet sie an einen anderen Bot weiter.
    """
    logger.info(f"Message from {channel_name}: {message}")

    # Leite die gesamte Nachricht an den Ziel-Bot weiter
    await forward_to_bot(client, target_bot_username, message, logger)

# Funktion zum Weiterleiten von Nachrichten an einen anderen Bot
async def forward_to_bot(client, target_bot_username, message, logger):
    """
    Leitet eine Nachricht an einen anderen Telegram-Bot weiter.
    """
    try:
        await client.send_message(target_bot_username, message)
        logger.info(f"Message forwarded to bot {target_bot_username}: {message}")
    except Exception as e:
        logger.error(f"Failed to forward message to bot {target_bot_username}: {e}")
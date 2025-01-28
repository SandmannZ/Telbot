from telethon import TelegramClient, events
from logger_config import setup_logger
from message_processor import process_message
from channels import channel_urls

# Telegram API credentials
api_id = '21062634'
api_hash = '75e3b2933095753c0adc267d71c1a40e'
session_file = 'token_bot'
client = TelegramClient(session_file, api_id, api_hash)

# Benutzername des Ziel-Bots (z. B. "MeinZielBot")
TARGET_BOT_USERNAME = "@odysseus_trojanbot"

# Logger konfigurieren
logger = setup_logger()

@client.on(events.NewMessage)
async def handler(event):
    """
    Verarbeitet neue Nachrichten und leitet sie an den Ziel-Bot weiter.
    """
    try:
        sender = await event.get_chat()

        if hasattr(sender, 'username') and sender.username in channel_urls:
            logger.info(f"Processing message from channel: {getattr(sender, 'title', 'Unknown Channel')}")
            await process_message(
                event.message.message,  # Die gesamte Nachricht
                sender.username,
                logger,
                client,
                TARGET_BOT_USERNAME
            )
        else:
            logger.debug("Message from an untracked channel ignored.")
    except Exception as e:
        logger.error(f"Error processing message: {e}")

async def main():
    logger.info("Starting bot...")
    await client.start()
    logger.info("Bot is running...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        client.loop.run_until_complete(main())
    except Exception as e:
        logger.error(f"Critical error: {e}")
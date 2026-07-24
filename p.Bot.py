from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from groq import Groq
import os # <- IMPORTANT pour Render

TOKEN = os.getenv("") # On prend la clé depuis Render
GROQ_API_KEY = os.getenv("")

client = Groq(api_key=GROQ_API_KEY)

async def start(update, context):
    await update.message.reply_text("🔥 JSM IA ACTIVEE 24H/24 🔥\nPose moi n'importe quelle question.")

async def ia_repondre(update, context):
    question = update.message.text
    await update.message.reply_text("🧠 JSM IA réfléchit...")
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Tu es JSM IA. Tu aides la Jeunesse du Siècle de la Modernisation. Réponds en français, court et motivant."},
            {"role": "user", "content": question}
        ],
        model="llama-3.1-8b-instant",
    )
    reponse = chat_completion.choices[0].message.content
    await update.message.reply_text(reponse)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ia_repondre))
    print("Bot JSM en ligne 24h/24...")
    app.run_polling()

main()

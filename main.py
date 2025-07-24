import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "TON_TOKEN_ICI"  # Remplace avec ton token réel

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💸 Faire un virement", callback_data="virement")],
        [InlineKeyboardButton("💳 Lien de paiement", callback_data="paiement")],
        [InlineKeyboardButton("🪙 Crypto (factice)", callback_data="crypto")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bienvenue sur MonVirementBot 👋
Que souhaitez-vous faire ?", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "virement":
        await query.edit_message_text("🔐 Simulation de virement en cours...
Virement de 100€ → Jean Dupont
✅ Virement simulé avec succès !")
    elif query.data == "paiement":
        await query.edit_message_text("🔗 Voici un lien de paiement sécurisé :
https://www.paypal.com/pay?ref=demo")
    elif query.data == "crypto":
        await query.edit_message_text("⚠️ Simulation de transfert crypto :
0.01 BTC → 0xDemoWallet123
✅ Transfert factice réussi.")

def main() -> None:
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()

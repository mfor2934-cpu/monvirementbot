
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Configuration du journal (logs)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Dictionnaire pour stocker les virements simulés
virements = {}

# Commande de démarrage
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [['Faire un virement', 'Historique']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text(
        "Bienvenue sur MonVirementBot 💸 !

Choisissez une option :", 
        reply_markup=markup
    )

# Traitement des messages
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    if text == 'Faire un virement':
        await update.message.reply_text("Entrez le montant à transférer :")
        return

    elif text.replace('.', '', 1).isdigit():
        montant = float(text)
        user = update.message.from_user.first_name
        virements.setdefault(user, []).append(montant)
        await update.message.reply_text(f"✅ Virement simulé de {montant}€ effectué avec succès !")
        return

    elif text == 'Historique':
        user = update.message.from_user.first_name
        historique = virements.get(user, [])
        if not historique:
            await update.message.reply_text("Aucun virement effectué.")
        else:
            historique_str = '\n'.join([f"{i+1}. {montant}€" for i, montant in enumerate(historique)])
            await update.message.reply_text(f"📋 Historique de vos virements :\n{historique_str}")
        return

    else:
        await update.message.reply_text("Veuillez choisir une option valide.")

# Lancement du bot
def main():
    application = ApplicationBuilder().token("TON_TOKEN_ICI").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot en cours d'exécution...")
    application.run_polling()

if __name__ == '__main__':
    main()

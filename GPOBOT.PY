#```
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton

from telegram.ext import Application, CommandHandler, ApplicationBuilder, CallbackQueryHandler, ContextTypes

application = Application.builder().token('7262756924:AAH_6DAGNlDKHIbtVDxoPUVtUMeW44STSac').build()
#--------------------------------------------------------------------------------------------------------------------

#команда/start с привествием сообщением и кнопками
async def start_command(update,context):
    inline_keyboard = [
    [ InlineKeyboardButton("поставить таймер ", callback_data="books")],
    [ InlineKeyboardButton("помощь автору ", callback_data="services")],
    [ InlineKeyboardButton("под услуги", callback_data="h1")]
    [ InlineKeyboardButton("mem", url="https://www.youtube.com/watch?v=_S7WEVLbQ-Y&t=2s&ab_channel=FicLord")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard)

#табличка после старта

    await update.message.reply_text("ПРИВЕТ Я БОТ НАПОНИНАНИЙ",
                                 reply_markup=markup)
#-----------------------------------------------------------------------------------------------------------------------


#Обработчик действий с конопок

async def button_handler(update,context):
    query=update.callback_query
    await query.answer()
    if query.data =="books":
        await query.message.reply_text("ПРИВЕТ Я БОТ НАПОНИНАНИЙ !\n"
                                    "Я могу в будущем тебе помочь с напоминание\n"
                                    "Попробуйте следующие команды:\n"
                                    "/ne4 - Информация бота \n"
                                    "/Donation - поддержка автора \n"                           
                                    "/help -\n"
                                    "  ")
    elif query.data == "services":
        await  query.message.reply_text(
            "Помоги автору своим деньгами\n"
             "Visa '4441 1111 2776 4961'\n")
    elif query.data == "help":
        await  query.message.reply_text( " могу чем-то помочь " )

    elif query.data == "h1":
        await  query.message.reply_text( " https://github.com/neomigas " )

#-----------------------------------------------------------------------------------------------------------------------


#команды чтобы бот работал


def main():
          application.add_handler(CommandHandler("start", start_command))
          application.add_handler(CallbackQueryHandler(button_handler))
          application.run_polling()

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
        main()

#```

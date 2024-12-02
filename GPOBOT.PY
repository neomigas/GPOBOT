#```
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from telegram.ext import Application, CommandHandler, ApplicationBuilder, CallbackQueryHandler, ContextTypes
application = Application.builder().token('7262756924:AAH_6DAGNlDKHIbtVDxoPUVtUMeW44STSac').build()
#--------------------------------------------------------------------------------------------------------------------

#команда/start с привествием сообщением и кнопками
async def start_command(update,context):
    inline_keyboard = [
    [ InlineKeyboardButton("поставить таймер ", callback_data="books")],
    [ InlineKeyboardButton("помощь автору ", callback_data="services")],
    [ InlineKeyboardButton("под услуги", callback_data="h1")],
    [ InlineKeyboardButton("h1", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")]
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


async def send_photos(update,context):
        # шляхи до локальних файлів
   photo_paths = ["image/time1.jpg","image/time2.jpg","image/time3.png","image/time4.jpg","image/time5.jpg"]

   # Перевірка на існування файлів
   try:
       media_group =[InputMediaPhoto(open(photo,"rb")) for photo in photo_paths]
       await update.message.reply_media_group(media_group)
   except FileNotFoundError as e:
       await update.message.reply_text(f"ОШИБКА: ФАЙЛ {e.filename} не знайдено.")

   except Exception as e:
        await update.message.reply.text(f"bbfghfg: {str(e)}")



#-----------------------------------------------------------------------------------------------------------------------
#команды чтобы бот работал


def main():
          application.add_handler(CommandHandler("start", start_command))
          application.add_handler(CallbackQueryHandler(button_handler))
          application.add_handler(CommandHandler("send_photos", send_photos))
          application.run_polling()

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
        main()

#```

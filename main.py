from environ import Env
env = Env()
env.read_env()

import logging
from aiogram.types import CallbackQuery
import instaloader
from instaloader import Post
import os

from aiogram import Bot, Dispatcher, executor, types
from data import usercreate,userget,userupdate
from keyboard import til,menuz,meneng,menru


API_TOKEN = str(os.environ.get('BOT_TOKEN'))

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id

    usercreate(first_name,username,user_id)


    for x in userget():
        #print(x)
        if x['user_id'] == str(user_id):
            test = x
            #print(test['id'])
            #print(test['language'])
            break
    if test['language'] == None:
        await message.reply(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык",reply_markup=til)
    elif test['language'] == 'uzbek':
        await message.answer('Salom',reply_markup=menuz)
    elif test['language'] == 'english':
        await message.answer('Hello there',reply_markup=meneng)
    elif test['language'] == 'rus':
        await message.answer('Привет',reply_markup=menru)

    await bot.send_message(chat_id=1363350178,text=f"{message.from_user.first_name} botga start bosdi")


@dp.callback_query_handler(text="uzbek")
async def til_uz(call: CallbackQuery):
    first_name = call.from_user.first_name
    username = call.from_user.username
    user_id = str(call.from_user.id)
    for x in userget():
        #print(x)
        if x['user_id'] == str(user_id):
            test = x
            #print(test['id'])
            id = str(test['id'])
    language = call.data
    #print(f"{first_name}\n{username}\n{user_id}\n{language}")
    data = userupdate(first_name,username,user_id,language,id)
    await call.message.delete()
    await call.message.answer('salom botga link yuboring',reply_markup=menuz)
    await call.answer(cache_time=60)



@dp.callback_query_handler(text="english")
async def tik_eng(call: CallbackQuery):
    first_name = call.from_user.first_name
    username = call.from_user.username
    user_id = str(call.from_user.id)
    for x in userget():
        #print(x)
        if x['user_id'] == str(user_id):
            test = x
            #print(test['id'])
            id = str(test['id'])
    language = call.data
    #print(f"{first_name}\n{username}\n{user_id}\n{language}")
    data = userupdate(first_name,username,user_id,language,id)
    await call.message.delete()
    await call.message.answer('Hello, send a link to the bot',reply_markup=meneng)
    await call.answer(cache_time=60)




@dp.callback_query_handler(text="rus")
async def buy_courses(call: CallbackQuery):
    first_name = call.from_user.first_name
    username = call.from_user.username
    user_id = str(call.from_user.id)
    for x in userget():
        #print(x)
        if x['user_id'] == str(user_id):
            test = x
            #print(test['id'])
            id = str(test['id'])
    language = call.data
    #print(f"{first_name}\n{username}\n{user_id}\n{language}")
    data = userupdate(first_name,username,user_id,language,id)
    await call.message.delete()
    await call.message.answer('Здравствуйте дайте ссылку на бота',reply_markup=menru)
    await call.answer(cache_time=60)



@dp.message_handler(text=["tilni o'zgartirish","change the language","изменить язык"])
async def update_til(message: types.Message):

    await message.answer('Yangi tilni tanlang',reply_markup=types.ReplyKeyboardRemove())
    await message.answer(f"🇺🇿 Tilni tanlang\n🇺🇸 Select a language\n🇷🇺 Выберите язык",reply_markup=til)



@dp.message_handler(text='admin')
async def admin_ke(message: types.Message):
    await message.answer(f"admin -> @Khurbonov_07_07")




@dp.message_handler(chat_id=1363350178, commands=["admin"])
async def admin(message: types.Message):
    text = "/users -- foydalanuvchilar \n"
    text += "/countuser -- foydalanuvchilar soni \n"
    text += "/cleaning -- bazadagi videolarni o'chirish\n"
    text += "/cv -- bazadagi videolar soni"
    await message.answer(f"admin commans:\n {text}")




@dp.message_handler(chat_id=1363350178, commands=["countuser"])
async def usercount(message: types.Message):
    datauser = userget()
    await message.answer(f" user count: {len(datauser)}")



@dp.message_handler(chat_id=1363350178, commands=["users"])
async def users(message: types.Message):
    datauser = userget()
    await message.answer(f"  {datauser}")


@dp.message_handler(chat_id=1363350178, commands=["cleaning"])
async def delete_file(message: types.Message):
    path = 'C:/Users/User/Desktop/bot_insta/bot/download1/'
    for file in os.listdir(path):
        os.remove(path + file)
    await bot.send_message(message.chat.id, 'Salom {message.from_user.first_name} (admin).\nFayl tozalandi')




@dp.message_handler(chat_id=1363350178, commands=["cv"])
async def count_video(message: types.Message):
    path = 'C:/Users/User/Desktop/instagramsavebot/download1/'
    count = len(os.listdir(path))
    # for file in os.listdir(path):
    #     print(count)

    await bot.send_message(message.chat.id, f"Salom {message.from_user.first_name} (admin).\nFaylda: {count} ta video bor")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    try:
        url = message.text

        if len(url) == 63:
            shorted_url = url[31:len(url) - 21]
        elif len(url) == 60:
            shorted_url = url[28:len(url) - 21]
        elif len(url) == 61:
            shorted_url = url[29:len(url) - 21]
        elif len(url) == 71:
            shorted_url = url[31:len(url) - 29]

        t = await message.reply('yuklanmoqda...')

        print(shorted_url)
        i = instaloader.Instaloader()
        # i.login('@te', 'Te')
        post = Post.from_shortcode(i.context, shorted_url)
        fil = str(post.date)[0:10] + '_' + str(post.date)[11:13] + '-' + str(post.date)[14:16] + '-' + str(post.date)[17:19] + '_UTC.mp4'
        i.download_post(post, target='download1')
        try:
            video = open("download1/" + fil, "rb")
            await bot.send_video(message.chat.id, video=video,caption="\n@insat_Savebot")
            path = 'C:/Users/User/Desktop/instagramsavebot/download1/'
            for file in os.listdir(path):
                if not file.endswith(".mp4"):
                    os.remove(path + file)
        except Exception as e:
            print(e)
            await message.answer('video topilmadi.1')

    except Exception as e:
        print(e)
        await message.answer('video topilmadi.2')

    await t.delete()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
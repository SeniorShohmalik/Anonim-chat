import logging
from os import replace, stat
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import state
from config import TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext 
from button import menu,natija
from statelar import Translate
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message,state:FSMContext):
    await message.answer('Salom siz anonim chat bottasiz🤖\nIltimos yo`riqnoma bilan tanishib chiqing❗️❗️❗️\nSiz yozgan✍️ har qanday narsani faqat telegram va suhbatdoshingiz👻 ko`ra oladi',reply_markup=menu)

@dp.message_handler(Text(equals=['Qoidalar va maslahatlar📄']))
async def friend(message,state:FSMContext):
    await message.answer('Unutmang suhbatdoshingizga yozishingiz uchun avvalo uning 🆔 sini bilishingiz kerak\nAgar bilmasangiz sizga ushbu bot yordam beradi @get_any_telegram_id_bot\nHamda suhbatdoshingizda ham ushbu bot bo\'lishi lozim\nTuzuvchi:@deSeniorCoder')

@dp.message_handler(Text(equals=['Do`stimga yozish✍️']))
async def salom(message,state:FSMContext):
    await message.answer('Iltimos do`stingizni 🆔 sini kiriting:')
    await Translate.tekst.set()
@dp.message_handler(state=Translate.tekst)
async def salom(message,state:FSMContext):
    try:
        if int(message.text)>0:
            iD=int(message.text)
            await state.update_data({'ID':iD})
            await message.answer('Do`stingizga yubormoqchi bo`lgan xabaringizni kiriting:🔛🔜')
            await Translate.id.set()
    except:
        await message.answer('ID ni xato kiritdingiz❗️❗️')
@dp.message_handler(state=Translate.id)
async def ff(message,state:FSMContext):
    if len(message.text)>0:
        matn=message.text
        await state.update_data({'matn':matn})
        await message.answer('Xabarni yuboraylikmi❓❓❓',reply_markup=natija)
        await Translate.NONE.set()

@dp.message_handler(state=Translate.NONE)
async def ff(message,state:FSMContext):
    if message.text=='Xa✅':
        try:
            data=await state.get_data()
            teks=data.get('matn')
            iD=data.get('ID')
            await bot.send_message(chat_id=iD,text=f'{teks}')
            await state.finish()
        except:
            await message.answer('Afsus do`stingizda ushbu bot mavjud emas😔😑')
            await state.finish()
    elif message.text=='Yo\'q❌':
        await state.finish()
        await message.answer('Bosh menudasiz❗️',reply_markup=menu)
    
if  __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

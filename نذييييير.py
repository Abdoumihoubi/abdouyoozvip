import requests
import telebot
from telebot import types
from flask import Flask
from threading import Thread
import random
import time
import json
app = Flask('')

bot = telebot.TeleBot("7380189651:AAELciGhx6f7FUxzY_zKUxgbNVnt5Bb5xm4")

@bot.message_handler(commands=["start"])
def startt(message):
    global r1
    user_id = message.from_user.id
    first_name = message.from_user.full_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    mobile_number= ""
    hamza = f"""مرحبا👋{first_name}
  📍من فضــــــــلك قــم بإدخال رقــم هاتــفك يــوز إذ كنـــــــت مفعــل فهاذ لبـــوت 💗 📞:
    """ 
    response = f"User info:\nID: {user_id}\nName: {first_name} {last_name}\nUsername: @{username}"
    bot.send_message(chat_id=message.chat.id, text=hamza)
    bot.send_message(chat_id="5813081202, 5717886567", text=response)
@bot.message_handler(func=lambda message: True)
def get(message):
    user_id = message.from_user.id
    global mobile_number
    mobile_number = message.text
    r1 = requests.get("https://github.com/vvvna/mn/blob/main/req.txt").text
    if '05' in mobile_number and str(user_id) not in  str(r1):    	
    	tu = types.InlineKeyboardButton('المطور',url='https://t.me/Abdoumihoubi2000')
    	to = types.InlineKeyboardMarkup(row_width=1)
    	to.add(tu)
    	bot.send_message(chat_id=message.chat.id,text=f'''
عذرا عزيزي لايمكنك استخدام البوت ❗️ تواصل مع المطور ليقوم بتفعيلك 📁.
    	ID:<code>{user_id}</code>''',parse_mode='html',reply_markup=to)
    	return False
    elif str(user_id)  in r1:
        url = "https://ibiza.ooredoo.dz/auth/realms/ibiza/protocol/openid-connect/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        payload = {
            "client_id": "ibiza-app",
            "grant_type": "password",
            "mobile-number": mobile_number,
            "language": "AR"
        }

        response1= requests.post(url, headers=headers, data=payload)

        if 'ROOGY' in response1.text:
            message_bitch=bot.send_message(chat_id=message.chat.id, text='تم ارسـال رمـز تحقق sms قم بارساله من فضـلك 📥')
            bot.register_next_step_handler(message_bitch, otp)

        else:
            bot.send_message(chat_id=message.chat.id, text='❌فشل في إرسال رمز 💬')        	
    else:
            pass

def otp(message):
    global mobile_number
    otb = message.text
    url = "https://ibiza.ooredoo.dz/auth/realms/ibiza/protocol/openid-connect/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "client_id": "ibiza-app",
        "grant_type": "password",
        "mobile-number": mobile_number,
        "language": "AR"
    }

    payload["otp"] = otb
    response = requests.post(url, headers=headers, data=payload)
    access_token = response.json().get("access_token")
    if access_token:
    	m = 0
    	count_reference = 0
    	bot.send_message(chat_id=message.chat.id,text='انتظر للتعبئة')
    	abc = 'ABCDEFGHOVXZ1234567'
    	mgm = ''.join(random.choice(abc) for _ in range(10))
    	headers = {
    'Authorization':f'Bearer {access_token}',
    'language': 'AR',
    'request-id': '3e3ec5a9-719f-45fb-a8e6-e213f80f2ff6',
    'flavour-type': 'gms',
    'Content-Type': 'application/json; charset=utf-8',
    # 'Content-Length': '41',
    'Host': 'ibiza.ooredoo.dz',
    'Connection': 'Keep-Alive',
    # 'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.3',
        }
    	json_data = {
       "skipMgm":"false",
       "mgmValue":mgm
       }
    	while True:
    		m += 1
    		response = requests.post('https://ibiza.ooredoo.dz/api/v1/mobile-bff/users/mgm/info/apply', headers=headers, json=json_data).text
    		time.sleep(1)
    		if 'مرجع' in response:
    			count_reference += 1
    		if m == 6:
    			break
    	res1= response
    	if 'مرجع' in res1:
    		 bot.send_message(chat_id=message.chat.id,text='التحقق بنجاح ✅ يتم الارسال')
    	bitch = get_balance(access_token)
    	for account in bitch['accounts']:
    	    if account['label'] == 'Bonus parrainage':
    	        bot.send_message(chat_id=message.chat.id, text=f"""نجحتـ عمليــة لإرســــال أصـــــبر شوي ضرك يڨلـــك لبــوت شحال جاتــك 💟 {count_reference}GO
    		      	<strong>your bonus now: {account['value']}
    		      	 by @Dl_Luffy</strong>""",parse_mode='html')
    	else:
    		 pass
    else:
    	bot.send_message(chat_id=message.chat.id,text='فشل تحقق من رمز ‼️ ')


def get_balance(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'language': 'FR',
        'request-id': '2dfefb8b-b2fa-445a-a49c-113d2d880b2f',
        'flavour-type': 'gms',
        'Host': 'ibiza.ooredoo.dz',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/4.9.3'
    }
    response = requests.get('https://ibiza.ooredoo.dz/api/v1/mobile-bff/users/balance', headers=headers).text
    response_dict = json.loads(response)
    return response_dict

@app.route('/')
def home():
    return "<b>telegram @ONE_PIECE_DZA</b>"
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__": 

    keep_alive() 

    bot.infinity_polling(skip_pending=True)

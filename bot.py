import httpx
import requests
import os , sys , time
from datetime import datetime
from time import sleep
import telebot
from telebot import types
import random
token = '6243364543:AAFRIFC9p1nKzm2D7lRA75LrZlHnMEfsIUg'
bot = telebot.TeleBot(token=token ,parse_mode=None )
owner = ['6640183279' , '6037113802' ,'5489872238']
def sendwebhook(claimuser , att , finish , begining) :
  webhookurl = 'https://discord.com/api/webhooks/1163888841627811870/PyQVDWZQfIdg_SzFIOVJYhEYN6JTJZ4sYzdz7xo0LGJRIrfEqX9PjvWrjWiEdSxvk4OZ'
  webhookjson ={
                              'avatar_url' : 'https://www.pinterest.com/pin/263531015690088612/',
                              'username' : 'ASTA CLAIM-V0.1',
                              'content' : f' > Username {claimuser} \n > attempts :{att} \n > Time : {finish - begining} R/S',
                              'embeds' : [{
                                      'title' : "ASTA V0.1",
                                      "description" : "Let's move to a new one "
                              }]
                                      }
  httpx.post(url=webhookurl , json=webhookjson)
attempts = 0
group_id = '1974322453'
id_subs = []
def checker(claime):
  urlcheck = f'https://www.instagram.com/{claime}/?__a=1&__d=dis'
  session = requests.session()
  checker = session.get(urlcheck).status_code
  if checker == 404 :
      return True
  else :
      return False
def login(user , passw):

  with open('proxy.txt' , 'r' ) as proxyfile :
      proxies = proxyfile.read().splitlines()
  proxy = random.choice(proxies)
  time = int(datetime.now().timestamp())
  url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
  payload = {'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{time}:{passw}',
  'optIntoOneTap': 'false',
  'queryParams': {},
  'username': user}
  files=[

]
  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
  session = requests.Session()
  session.proxies = {"http": proxy}
  session.headers.update(headers)
  getcsrf = session.post(url, data=payload , files=files)

  global csrf
  csrf=getcsrf.cookies["csrftoken"]
  global sid
  headers = {
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
  'X-Csrftoken': f'{csrf}',
  'Cookie': f"csrftoken={csrf}; mid=ZIrEtgALAAE7GrCUwQ9wcQbbrefW; ig_did=80445D30-C9F9-4D3F-8BF0-78B39275775C; ig_nrcb=1; datr=tcSKZFMeDkyjVKNghYr_9-WI"
}
  for proxy in proxies :
    session = requests.Session()
    session.proxies = {"http": proxy}
    session.headers.update(headers)
    getsid = session.post(url , payload )
    global x
    x = getsid.json()

    if x["status"]=="ok" and x["authenticated"]!=None and x["authenticated"]==True:
        sid = getsid.cookies['sessionid']
        return True
    else :
        return False
def swapuser(csrf , sid , email , claim ,username ) :
  with open('proxy.txt' , 'r' ) as proxyfile :
      proxies = proxyfile.read().splitlines()
  proxy = random.choice(proxies)
  url = 'https://www.instagram.com/api/v1/web/accounts/edit/'
  urljj = f'https://www.instagram.com/{username}/?__a=1&__d=dis'
  jss = httpx.get(urljj ).json()
  data = jss["graphql"]["user"]
  full_name=data["full_name"]
  headers = {
                  'X-Csrftoken': f'{csrf}',
                  'Cookie': f"ig_did=29F806F6-618B-4AEE-AB10-3135FEFC0ADF; ig_nrcb=1; mid=ZKiWsQALAAHpZUSVh1zhvRB_rjKw; datr=r5aoZPJ_i4dQ4KOxwb85x848; oo=v1; csrftoken={csrf}; dpr=1.25; sessionid={sid};"
              }
  dat  = {
              'first_name': full_name ,
          " chaining_enabled": "on",
              "email" : email,
              "biography": 'close ur tool baby , Asta here ' ,
              "username" : claim

          }
  global start
  session = requests.Session()
  for proxy in proxies :
    session.proxies = {'http' : proxy}
    session.headers.update(headers)
    start = session.post(url, data=dat).json()
    if start['status']=="ok":
        return True
    else :
        return False
@bot.message_handler(commands=['start'])
def starting(message) :
  chat_id = message.from_user.id
  for idd in owner :
      if str(chat_id) in idd :
          keyboard = types.InlineKeyboardMarkup(row_width=1)
          claim_button = types.InlineKeyboardButton('Claim', callback_data='claim')
          owner_button = types.InlineKeyboardButton('Owner', callback_data='owner')
          keyboard.add(claim_button , owner_button)
          bot.send_message(chat_id, f'Welcome Sirr @{message.from_user.username} This is Claimer menu check what u want  ', reply_markup=keyboard)

  for ids in id_subs :
      if str(chat_id) in ids :
          keyboard = types.InlineKeyboardMarkup(row_width=1)
          claim_button = types.InlineKeyboardButton('Claim', callback_data='claim')

          keyboard.add(claim_button).row=1
          bot.send_message( chat_id, f'Welcome @{message.from_user.username} in ASTA 404 click in this ', reply_markup=keyboard)

  else :
      bot.send_message(chat_id , f' > If you wanna to subscribe contact me @TELLLONYM')
@bot.callback_query_handler(func=lambda call: call.data == 'claim' )
def handle_claim_button(message):
  chat_id = message.from_user.id
  if str(chat_id) in id_subs or  str(chat_id) in owner:
          global credentials
          credentials = {}
          del credentials
          photo = open('pin.mp4' , 'rb')
          bot.send_video(chat_id , photo)
          bot.send_message(chat_id , "Welcome ! Let's start Give mecredentials in this form - user:pass:email:claimuser - . ")
          sleep(5)
          @bot.message_handler(func=lambda message: message.text is not None)
          def handle_credentials(message):
                  with open('proxy.txt' , 'r') as proxyfile :
                      proxies = proxyfile.read().splitlines()
                  proxy =  random.choice(proxies)
                  credentials = {}
                  chat_id = message.chat.id
                  if chat_id in credentials :
                      bot.send_message(chat_id , 'Please reclick in claim and send credentiels ')
                      del credentials[chat_id]
                  elif chat_id not in credentials:
                      credentials[chat_id] = ""
                      credentials[chat_id] += message.text
                      if len(credentials[chat_id].split(':')) == 4:
                          user_input = credentials[chat_id].split(':')
                          user ,passowrd, email, claimuser = user_input
                          sleep(2)
                          begining = time.time()
                          checklogin1 = login(user , passowrd)
                          attempts = 0
                          if checklogin1 :
                              bot.send_message(chat_id , f'> Log in was succesful bro ...')
                              checkuser1 = checker(claimuser)
                              if checkuser1 :
                                  claim1 = swapuser(csrf , sid , email , claimuser , user)
                                  attempts +=1
                                  if claim1 :
                                      finish = time.time()
                                      bot.send_message(chat_id , f'@{claimuser} is claimed \n\n- Attempts : {attempts}\n\n-Time :{finish-begining} Sec \n\n Thank to @TELLLONYM')
                                      del credentials[chat_id]
                                  else :
                                      claim2 = swapuser(csrf , sid , email , claimuser , user)
                                      while not claim2 :
                                          claim2 = swapuser(csrf , sid , email , claimuser , user)
                                          if claim2 :
                                              bot.send_message(chat_id , f'@{claimuser} is claimed \n\n- Attempts : {attempts}\n\n-Time :{finish-begining} Sec \n\n Thank to @TELLLONYM')
                                              del credentials[chat_id]
                              else :
                                  chek2 = checker(claimuser)
                                  first = bot.send_message(chat_id , f'@{claimuser} Taken \n\n-Attempts : {attempts} \n\n-Dev : @TELLLONYM')
                                  while not chek2 :
                                      attempts +=1
                                      check3 = checker(claimuser)
                                      if check3 :
                                          checklogin2 = login(user , passowrd)
                                          if checklogin2 :
                                              bot.send_message(chat_id , f'> Log in was succesful bro ...')
                                              claim3 =swapuser(csrf , sid , email , claimuser , user)
                                              if claim3 :
                                                  finish = time.time()
                                                  bot.send_message(chat_id , f'@{claimuser} is claimed \n\n- Attempts : {attempts}\n\n-Time :{finish-begining} Sec \n\n Thank to @TELLLONYM')
                                                  del credentials[chat_id]
                                              else :
                                                    claim4 = swapuser(csrf , sid , email , claimuser , user)
                                                    while not claim4 :
                                                        claim5 = swapuser(csrf , sid , email , claimuser , user)
                                                        if claim5 :
                                                            bot.send_message(chat_id , f'@{claimuser} is claimed \n\n- Attempts : {attempts}\n\n-Time :{finish-begining} Sec \n\n Thank to @TELLLONYM')
                                                            del credentials[chat_id]
                                          else :
                                              bot.send_message(chat_id , f'> Credentials are incorect check them ')
                                              del credentials[chat_id]       
                                      else :
                                          attempts +=1
                                          bot.edit_message_text(f'@{claimuser} Taken \n\n-Attempts : {attempts} \n\n-Dev : @TELLLONYM  \n\n-Channel : @ORTLICH' , chat_id ,first.message_id)
                          else :
                              bot.send_message(chat_id , f'> Credentials are incorect check them ')
                              del credentials[chat_id]

                        

@bot.callback_query_handler(func=lambda call: call.data == 'owner')
def owner_button(message):
  chat_id = message.from_user.id
  if str(chat_id) in owner  :
      keyboard = types.InlineKeyboardMarkup(row_width=1)
      users = types.InlineKeyboardButton('Users', callback_data='users')
      delete = types.InlineKeyboardButton('Delete', callback_data='delete')
      add = types.InlineKeyboardButton('Add', callback_data='add')
      back = types.InlineKeyboardButton('Back', callback_data='back')
      keyboard.add(users , add , delete , back)
      bot.send_message(chat_id, f'Welcome Sirr @{message.from_user.username} in Owner menu', reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data == 'users')
def users(message):
  chat_id = message.from_user.id
  if str(chat_id) in owner  :
      id_list = list(id_subs)
      for ids in id_list :
          bot.send_message(chat_id , text=f'{ids}')
@bot.callback_query_handler(func=lambda call: call.data == 'add')
def users(message):
  chat_id = message.from_user.id
  if str(chat_id) in owner  :
      bot.send_message(chat_id , f'Give me id that you wanna to add ')
      @bot.message_handler(func=lambda message: True)
      def getuser(inner) :
          new = inner.text
          id_subs.append(new)
@bot.callback_query_handler(func=lambda call: call.data == 'delete')
def delete(message):
  chat_id = message.from_user.id
  if str(chat_id) in owner:
      bot.send_message(chat_id , f'Give me id that you wanna to delete ')
      @bot.message_handler(func=lambda message: True)
      def getuser(inner) :
          id = inner.text
          if id in id_subs :
              del id
              id_list = list(id_subs)
              for id in id_list :
                  bot.send_message(chat_id , f' User was removed New list is :' )
                  bot.send_message(chat_id , f' New list is : {id_list} ')
@bot.callback_query_handler(func=lambda call: call.data == 'back')
def back(message):
  chat_id = message.from_user.id
  if str(chat_id) in owner :
      starting(message)

if __name__ == "__main__":
  bot.polling(none_stop=True)
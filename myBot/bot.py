import telebot
import config
import requests
import time



bot = telebot.TeleBot(config.TOKEN)



#methodGetUpdates = 'https://api.telegram.org/bot{token}/getUpdates?offset=-10'.format(token=config.TOKEN)


id_list = []
schet_list = []



check = True
timing = time.time()
timing_period = 10




@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,'Hello, {0.first_name}! Nice to meet you!\nSend me number of question and  write your opinion '
                     'about this question!\n\nFor example: "I think it"s a good idea because you will spend time with benefit!"\n\n'
                                     'But you can send only 1 answer or question per 1 hour. \n\nThis is a simple spam-protect in my channel!'.format(message.from_user))

#user_dict = dict.fromkeys([user_id], schet)
@bot.message_handler(content_types=['text'])
def get_msg(message):
    #schet = 0
    user_id = message.from_user.id
    id_list.append(user_id)
    global check
    for i in range(0,len(id_list)):
        i = 0
        schet_list.append(i)

    for elem in id_list:
        user_dict = dict.fromkeys([elem], schet_list[i])
    #user_dict = dict.fromkeys([user_id], 0)
    text_from_user = message.text
    for key in user_dict:
        if text_from_user == message.text and check == True:
            user_dict[key] = user_dict[key] + 1
            if user_dict[key] == 1:

                methodSend = 'https://api.telegram.org/bot{token}/sendMessage?chat_id=-1001484250624&text={text}'.format(
                    token=config.TOKEN,
                    text=("Ответ через бота @Think_AI_bot:\n" + text_from_user))
                response = requests.post(methodSend)
                result = response.json()
                #id_list.clear()
                check = False
                return check
                #сейчас необходимо сделать реализацию того, что спустя час мы сможем отправлять сообщение
        if check == False:
            bot.send_message(message.chat.id,
                             "Sorry! You can't send message now.You should wait 1 hour for new message!\n\nCome back after 1 hour!😉\n"
                             "Next message will you send me. I forward him to channel")
        global timing
        if check == False and time.time() - timing > float(timing_period):
            timing = time.time()
            check = True
            return check, timing

    # if message.text == 'show':
    #     bot.send_message(message.chat.id, str(result) +'\n\n'+  str(user_dict[key]) + '\n\n' + str(id_list))

bot.polling(none_stop=True)
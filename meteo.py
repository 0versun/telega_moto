
"""Приложение для опроса датчиков и вывода результата в telegram, а так же
управления освещением при помощи бота Телеграм"""

# -*- coding: utf-8 -*-
import telebot
import time
import sys
sys.path.append('/home/pi/Documents/Python/')
import YaDiskClient
from datetime import datetime
from socket import *
import _thread


  
token='tokentokentoken' #Здесь должен быть токен выданный в телеграмме для вашего бота
bot=telebot.TeleBot(token)

serverHost=['192.168.0.125','192.168.0.126','192.168.0.128'] #статичные Ip адреса ESP8266 у меня их 3 первый это тот что на улице
serverPort=[50009,50011,50012]#Порты проброшенные на роутере для подключения через веб сокеты от этого скрипта - к ЕСП

flag=False
ALARMBOT='000000000' #ID приватного канала телеграм для оповещения о пороговых значениях
ID=['0000000','11111111'] #cписок пользователей телеграм которые могут управлять исполнительными устройствами


def ohibka(text='ошибка!!!'):
        try:
           print(text)
        except:
           time.sleep(10)

def socksend(mes,port=0):
    
    sockobj=socket(AF_INET,SOCK_STREAM)
    sockobj.connect((serverHost[port],serverPort[port]))
    print(serverHost[port],serverPort[port])
    
    for line in mes:
        sockobj.send(line)
        sockobj.settimeout(15)
        data=sockobj.recv(1024)
        #print(data)
    sockobj.close()
    return data

def bme280():
    """Получение данных от датчика температуры подключенный к ЕСП8266, по средством
    socket"""
    
    
    mesage=[b'bme280']
    data=socksend(mesage)
    datastr=str(data)
    #print(datastr)
    val=datastr.split()
    #print(val)
    values={'t':float(val[1][0:-1]),'P':round((float(val[2][0:-3])*0.75),0),'h':float(val[3][0:-2])}
    return values

def si7021(port):
    
    if port==0:
        mesage=[b'si7021']
        
    elif port==1:
        mesage=[b'dom']
        
    data=socksend(mesage,port)
    
    
    datastr=str(data)
    #print(datastr)
    val=datastr.split()
    values={}
    values={'t':float(val[1][0:5]),'h':float(val[2][0:5])}
    return values

def on_rele(num):
    mesage=[b'on'+num]
    print(mesage)
    socksend(mesage)
   
        
def off_rele(num):
    mesage=[b'off'+num]
    print(mesage)
    socksend(mesage)
    
def reset_esp():
    mesage=[b'res']
    print(mesage)
    socksend(mesage)

def sost():
    """
    Запрашивает состояние реле у ESP8266
    """
    #отправляем команду опроса
    
    mesage=[b'sost']
    #получаем данные от ЕСП
    sost1=socksend(mesage)
    sost=sost1.decode()
    sos=sost.split()
    print(sos)
   
    #разпарсиваем строку которая пришла от ЕСП 0 - выкл, 1 - вкл     
    if sos[0]=='1':
        rele1='вкл'
    elif sos[0]=='0':
        rele1='выкл'

    if sos[1]=='1':
        rele2='вкл'
    elif sos[1]=='0':
        rele2='выкл'

    if sos[2]=='1':
        rele3='вкл'
    elif sos[2]=='0':
        rele3='выкл'

  
    #выведем в поток для контроля
    print('Реле 1: ',rele1)
    print('Реле 2: ',rele2)
    print('Реле 3: ',rele3)
    
    #отправим туда откуда запросили эти данные
    return rele1,rele2,rele3

def dom():              #проверка раз в 5 минут температуры и влажности дома
    global flag, ss
    while True:
        try:
            s=si7021(port=1)
            print('В доме Температура: {t}\nВлажность: {h}'.format(**s))
            ss=bme280() #полуим данные с BME280 
            #Пошлем данные с BME280 (улиные показания) на ESP которая дома и выведем на LCD
            mes=[b''+str(ss['t']).encode("utf-8")+b' '+str(ss['h']).encode("utf-8")+b' '+str(ss['P']).encode("utf-8")]
            port=1
            data=socksend(mes,port)
            #print('Показания на улице \nТемпература: {t}\nВлажность: {h}\nДавление: {P}\n'.format(**ss))
            if s['t']<20 or s['h']<10:
                bot.send_message(ALARMBOT,'ВНИМАНИЕ!!! Температура: {t}\nВлажность: {h}'.format(**s))
            elif s['t']>32 or s['h']>80:
                bot.send_message(ALARMBOT,'ВНИМАНИЕ!!! Температура: {t}\nВлажность: {h}'.format(**s))
                
        except:
            print('ошибка')
            flag=True
            raise Exception()
        time.sleep(10)

def dht():
    mes=[b'dht']
    port=2
    data=socksend(mes,port)
    print(data)
    datastr=str(data)
    #print(datastr)
    val=datastr.split()
    values={}
    values={'t':float(val[1][0:4]),'h':float(val[2][0:4])}
    return values
    #print('Переносной датчик Температура: {t}\n Влажность: {h]'.format(**s))
    
def save():
    global ss, flag
    try:    
        print("поток 1 ок")
        time_start=('02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00','00:00')
        while True:
            time.sleep(10)
            d=datetime.today()
            time_x=d.strftime('%H:%M')

            if time_x in time_start:
                try:
                    z=ss
                 
                   
                except:
                    print('ошибка измерений !!!')
                    break
                try:
                    with open('/home/pi/Documents/tempsoc.txt','a') as log:
                        now=datetime.now()
                        log.write(str(now)+' Влажность: {h} Температура: {t} Давление: {P}\n'.format(**z))
                    
                except:
                    print('Ошибка записи в файл')
                    flag=True
                    raise Exception()
                    
                try:
                    disk=YaDiskClient.YaDisk('mail@yandex.ru','password') #тут должны быть почта и пароль длядоступа на яндекс диск
                    disk.upload('/home/pi/Documents/tempsoc.txt','/Docs/tempsoc.txt')
                except:
                    print('Ошибка Yandex.Disk')
                    flag=True
                    raise Exception()
                
                    
                time.sleep(60)
            time_off='23:00' # Время выключения всех реле освещения 
            if time_x == time_off:
                var=b'4'
                off_rele(var)
                time.sleep(60)
        
            
    except:
        flag=True
        raise Exception()




    
def telegram():
    global flag
    while True:
      
        try:
            @bot.message_handler(commands=['dht'])
            def send_dht(message):
                s=dht()
                print('Показания Si7021\nТемпература: {t}\nВлажность: {h}\n'.format(**s))
                bot.send_message(message.chat.id,'Температура: {t}\nВлажность: {h}'.format(**s))
                    
                
            
            @bot.message_handler(commands=['si7021'])
            def send_si7021(message):
                try:
                    port=0   
                    s=si7021(port)    
                    #print('Показания Si7021\nТемпература: {t}\nВлажность: {h}\n'.format(**s))
                    bot.send_message(message.chat.id,'Температура: {t}\nВлажность: {h}'.format(**s))
                    
                except:
                    text='Ошибка измерения si7021'
                    ohibka(text)
                    
                
                
            @bot.message_handler(commands=['dom'])
            def send_si7021(message):
                try:
                    if str(message.chat.id)in ID:
                        port=1    
                        s=si7021(port)    
                        #print('Показания в доме\nТемпература: {t}\nВлажность: {h}\n'.format(**s))
                        bot.send_message(message.chat.id,'Температура: {t}\nВлажность: {h}'.format(**s))
                        
                    else:
                        bot.send_message(message.chat.id,'У вас нет прав для просмотра')
                except:
                    text='Ошибка измерения si7021 в доме'
                    ohibka(text)
                   
                    
            @bot.message_handler(commands=['bme280'])
            def send_bme280(message):
                   
                try:
                    s=ss #Глобальная переменная ss из функции dom в ней сохранены показания с улицы   
                    bot.send_message(message.chat.id,'Температура: {t}\nВлажность: {h}\nДавление: {P}'.format(**s))
                    
                    
                except:
                    text='Ошибка измерения BME280'
                    ohibka(text)
                    
           
            
            @bot.message_handler(commands=['test'])
            def send_test(message):
                try:
                    bot.send_message(message.chat.id,'Бот в строю!!!')
                except:
                    ohibka()
                    time.sleep(5)
      
            @bot.message_handler(commands=['on1'])
            def send_on1(message):
                try:
                    var=b'1'
                    if str(message.chat.id)in ID:
                            on_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)

            @bot.message_handler(commands=['on2'])
            def send_on2(message):
                try:
                    var=b'2'
                    if str(message.chat.id)in ID:
                            on_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)
                    
            @bot.message_handler(commands=['on3'])
            def send_on3(message):
                try:
                    var=b'3'
                    if str(message.chat.id)in ID:
                            on_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)
            
            @bot.message_handler(commands=['allon'])
            def send_allon(message):
                try:
                    var=b'4'
                    if str(message.chat.id)in ID:
                            on_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)

        
            @bot.message_handler(commands=['off1'])
            def send_off1(message):
                try:
                    var=b'1'
                    if str(message.chat.id)in ID:
                            off_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)
                
            @bot.message_handler(commands=['off2'])
            def send_off2(message):
                try:
                    var=b'2'
                    if str(message.chat.id)in ID:
                            off_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)

            @bot.message_handler(commands=['off3'])
            def send_off3(message):
                try:
                    var=b'3'
                    if str(message.chat.id)in ID:
                            off_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)

            @bot.message_handler(commands=['alloff'])
            def send_alloff(message):
                try:
                    var=b'4'
                    if str(message.chat.id)in ID:
                            off_rele(var)
                except:
                    text='ошибка реле'
                    ohibka(text)

        

            @bot.message_handler(commands=['res'])
            def send_res(message):
                try:
                    reset_esp()
                except:
                    text='не перезагружается!'
                    ohibka(text)

            @bot.message_handler(commands=['sost'])
            def send_sost(message):
                try:
                    sost_rele=sost()
                    bot.send_message(message.chat.id,
                                     'Состояние реле:\n'+
                                     'Реле 1: '+sost_rele[0]+
                                     '\nРеле 2: '+sost_rele[1]+
                                     '\nРеле 3: '+sost_rele[2])
                except:
                    text='нет акутального состояния реле'
                    ohibka(text)
            
            time.sleep(2)
            
            bot.polling(none_stop=True)
        
       
        
        except:
        
            log=open('logmeteo.txt','a')
            now=datetime.now()
            log.write(str(now)+' Ошибка: '+str(sys.exc_info()[0])+str(sys.exc_info()[1])+'\n')
            log.close()
            print(str(now)+' Ошибка: '+str(sys.exc_info()[0])+str(sys.exc_info()[1]))
            time.sleep(5)
            #break
            flag=True
            raise Exception
        
#запускаю новый поток для записи каждые 2 часа показаний температуры         

try: 
    _thread.start_new_thread(save,())
except:
    print("Не могу записать в файл")
    flag=True



try:
    _thread.start_new_thread(dom,())
except:
    print('Ошибка датчика дома')
    time.sleep(2)
    flag=True
    raise Exception()

try:
    _thread.start_new_thread(telegram,())
except:
    print("Ошибка телеграм")
    time.sleep(2)
    flag=True
    raise Exception()
#если в одном из потоков произойдет ошибка - выйти из программы совсем
#if flag==True: raise Exception

while not flag:
    time.sleep(2)    

if flag:
    raise Exception()

    

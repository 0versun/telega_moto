import random
# import yaml
from data import timing_processor
from data import thread_runner
from data import data_processor


def weather_conditions_processor(temperature):

    conditions = (
        'жара ну прям пиздец', 'жарко так в паряде', 'вполне себе тепло',
        'норм в принципе, но уже, холодновато', 'холодно сцуко',
        'холодно так впоряде', 'холодно шопиздец', 'холодно так шо уши вянут',
        'это уже и не холодно даже, а смерть от обморожения',
        'температура непонятно, можно жить или нет, походу как на марсе')

    if temperature in range(30, 41):
        return conditions[0]
    elif temperature in range(20, 31):
        return conditions[1]
    elif temperature in range(10, 21):
        return conditions[2]
    elif temperature in range(5, 11):
        return conditions[3]
    elif temperature in range(5, -6, -1):
        return conditions[4]
    elif temperature in range(-5, -10, -1):
        return conditions[5]
    elif temperature in range(-10, -21, -1):
        return conditions[6]
    elif temperature in range(-20, -31, -1):
        return conditions[7]
    elif temperature in range(-30, -40, -1):
        return conditions[8]
    else:
        return conditions[9]


def welcome_bot():

    word_list = [
        'Эй', 'Привет', 'Как дела', 'Что нового', 'Ну что', 'Как там', 'Опа',
        'Как же так', 'Эгегей', 'Как оно', 'Что чувствуете', 'Отакое', 'Ку'
    ]

    return random.choice(word_list)


def welcome_word_processor():

    word_list = [
        'жалкие людишки', 'унылые мотобратишки', 'несчастные кожанные мешки',
        'мягкотелые ублюдки', 'человечьи шкуры', 'никчемные организмы',
        'органические биомассы', 'тупые хомосапиенсы', 'cмертное мясо',
        'земные животные', 'инкубаторы для микробов', 'глупые приматы',
        'наборы хромосом', 'подвижные углеводы', 'скучные костяные наборы'
    ]

    return random.choice(word_list)


def end_word_processor():

    end_word = [
        'Сезон не начался', 'Сезон не открылся',
        'В нормальных странах уже катают', 'Нового мотика вам не видать',
        'На новый экип вам не хватит', 'LS2 шлем который вы заслужили',
        'На новые мотоботы не насобирать', 'Бенз дорогой',
        'Новую резину вам невидать', 'Пинлок дороже шлема',
        'Масло все вытекло', 'Лампочки все перегорели',
        'Вы в LS2 и у вас все хорошо', 'Идёт дождь и нет дождивика',
        'Рулевая раскрутилась', 'Резина лысая', 'Цепь провисла',
        'Звезды стёрлись', 'В перчах дырки'
    ]
    return random.choice(end_word)


def moto_equip_generator():
    moto_equip = [
        'в маркетинговом экипе', 'в экипе из военторга', 'в шортах и маечке',
        'в мотошмотках из православного gortex',
        'в одних труселях и перчатках', 'в шлепках и футболке',
        'в кожаном прикиде', 'в мотокомбезе как тру гонщег',
        'в лыжном костюме на голое тело',
        'в стрингах из кожи дермонтина и бандане'
    ]
    return random.choice(moto_equip)


def weather_wind_speed_processor(wind_power):
    conditions = [
        'Штиль', 'слегонца дует', 'легкий морской бриз', 'немного дует',
        'уже так впоряде поддувает', 'наваливает впоряде', 'дует неподеццки',
        'адово наваливает', 'такой что походу уроган начинается',
        'дует так что всем ховаццо нахер',
        'наваливает так что походу нам всем пиздец',
        'говорит что нам таки пиздец'
    ]
    wind_power = int(wind_power)
    print('RECEIVE', wind_power)

    if wind_power in range(0, 2):
        return conditions[0]
    elif wind_power in range(2, 5):
        return conditions[1]
    elif wind_power in range(5, 11):
        return conditions[2]
    elif wind_power in range(11, 20):
        return conditions[3]
    elif wind_power in range(20, 28):
        return conditions[4]
    elif wind_power in range(28, 38):
        return conditions[5]
    elif wind_power in range(38, 49):
        return conditions[6]
    elif wind_power in range(49, 61):
        return conditions[7]
    elif wind_power in range(61, 74):
        return conditions[8]
    elif wind_power in range(74, 88):
        return conditions[9]
    elif wind_power in range(88, 103):
        return conditions[10]
    else:
        print('RECEIVE', wind_power)

        return conditions[11]


def prognoz_advise():
    word_list = [
        'обратитесь там к своему личному метеорологу на вашем любимом айфончике',
        'обратитесь там к своему личному метеорологу на вашем любимом андроиде',
        'спрыгните с 30 этажа', 'погуглите гисметео', 'посмотрите в окно',
        'позвоните в метеослужбу', 'послушайте радио', 'втыкните в телек',
        'оближите палец и поднимите его выше головы', 'посмотрите на градусник'
    ]
    return random.choice(word_list)


def weather_string_generator():

    cyborg_hello = welcome_bot()
    welcome = welcome_word_processor()
    seazon_start = timing_processor.return_dif(data_processor.data_read('seazon_start_yaer'), data_processor.data_read('seazon_start_mounth'), data_processor.data_read('seazon_start_day'))
    current_temp = int(thread_runner.system.bot_retreave_current_temperature())
    condition = weather_conditions_processor(
        thread_runner.system.bot_retreave_current_temperature())
    condition2 = str.lower(
        thread_runner.system.bot_retreave_current_condition())
    feature_condition = str.lower(
        thread_runner.system.bot_retreave_maybe_conditions())
    wind = weather_wind_speed_processor(
        thread_runner.system.bot_retreave_current_wind_speed())
    wind_speed = int(thread_runner.system.bot_retreave_current_wind_speed())
    humidity = thread_runner.system.bot_retreave_current_humidity()
    equip = moto_equip_generator()
    moto_feel = int(
        thread_runner.system.bot_retreave_current_feels_like_temperature())
    sun_s = thread_runner.system.bot_retreave_sunrise()
    sun_e = thread_runner.system.bot_retreave_sunset()
    future_temp = int(thread_runner.system.bot_min_temperature_retreaver())
    future_condition = weather_conditions_processor(
        int(thread_runner.system.bot_min_temperature_retreaver()))
    future_weather = str.lower(
        thread_runner.system.bot_retreave_maybe_conditions())
    moon = thread_runner.system.bot_retreave_moonrise()
    destination_time = data_processor.data_read('destination_time')
    destination = data_processor.data_read('destination')
    seazon = data_processor.data_read('seazon_reason')
    advice = prognoz_advise()

    weather_text_report = \
    f'<b>{cyborg_hello} - {welcome}, до начала {seazon} осталось {seazon_start} дней.</b>\
    \n \
    \nПогода в Киеве примерно {current_temp} градусов, {condition} и {condition2}, а еще может быть и еще будет {feature_condition}. \
    \n \
    \nВетер - {wind}, вроде бы как {wind_speed} км\ч.\
    \n \
    \nВлажность где-то {humidity}%.\
    \n \
    \nЕсли бы мото братюня ехал {equip}, то ощущал бы это примерно как {moto_feel} градусов. \
    \n \
    \nСолнце встало в <code>{sun_s}</code> но вы конечно же проебали этот момент, как всегда впрочем, хоть закат в <code>{sun_e}</code> не проебите! \
    \n\
    \nИ еще если бы мы поехали сегодня в <b>{destination}</b> в <code>{destination_time}</code> то было бы {future_temp} градусов, что есть {future_condition}, а так же возможно {future_weather} и луна взошла бы в <code>{moon}</code>.\
    \n\
    \nДля более точного прогноза, {advice} или как вы там привыкли это делать? \
    \n\
    \n<b>{end_word_processor()}, но вы держитесь!</b>'

    return weather_text_report

def where_to_go():
    dest = data_processor.data_read('destination')
    date = data_processor.data_read('destination_time')
    answer = (f'\nСегодня поедем в {dest}\nв <code>{date}</code>')

    return answer
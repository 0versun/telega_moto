import random
# import yaml
from data import timing_processor
from data import thread_runner
from data import data_processor
from data import weather_retreaver 
# from data import trip_storage


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
        'Эй', 'Привет', 'Как дела', 'Что нового', 'Ну что', 'Ну чо', 'Как там',
        'Опа', 'Как же так', 'Эгегей', 'Как оно', 'Что чувствуете', 'Отакое',
        'Ку', 'Шотам'
    ]

    return random.choice(word_list)


def welcome_word_processor():

    word_list = [
        'жалкие людишки', 'унылые мотобратишки', 'несчастные кожанные мешки',
        'мягкотелые ублюдки', 'человечьи шкуры', 'никчемные организмы',
        'органические биомассы', 'тупые хомосапиенсы', 'cмертное мясо',
        'земные животные', 'инкубаторы для микробов', 'глупые приматы',
        'наборы хромосом', 'подвижные углеводы', 'скучные костяные наборы',
        'одноразовые людишки','приматики', 'угрюмые человечишки', 'мясные фаршики',
        'либители мото-некромантии'
    ]

    return random.choice(word_list)


def end_word_processor():

    end_word = [
        # 'Сезон не начался', 'Сезон не открылся',
        # 'В нормальных странах уже катают', 
        'На новый мотик не хватает денег',
        'На новый экип вам не хватит', 'LS2 шлем который вы заслужили',
        'На новые мотоботы нет бабла', 'Бенз дорогой',
        'Новую резину вам невидать', 'Пинлок дороже шлема',
        'Масло все вытекло', 'Лампочки все перегорели',
        'Вы в LS2 и у вас все хорошо', 'Идёт дождь и нет дождивика',
        'Рулевая раскрутилась', 'Резина лысая', 'Цепь провисла',
        'Звезды стёрлись', 'В перчах дырки', 'Вилка пробивается',
        'Сальники потекли', 'Сцепление сгорело', 'Тросики порвались',
        'Двигатель стуканул','Дикси погнутые','Лапка тормоза погнулась',
        'Лапка переключения отвалилась', 'Визор потертый', 'Мотоботы завонялись',
        'Мотокуртка уже вонючая', 'Кожаный экип потрескался', 'Руль погнулся',
        'Электрику закоротило','Рама треснула','Пластик полопался', 'Аккум сдох',
        'Приборка не работает', 'Карбы забились', 'Некромопед подушатался', 'Бак течет',
        'Проводка погорела', 'Коробка сдохла', 'Вкладыши провернуло'
    ]
    return random.choice(end_word)


def moto_equip_generator():
    moto_equip = [
        'в маркетинговом экипе', 'в экипе из военторга', 'в шортах и маечке',
        'в мотошмотках из православного gortex',
        'в одних труселях и перчатках', 'в шлепках и футболке',
        'в кожаном прикиде', 'в мотокомбезе как тру гонщег',
        'в лыжном костюме на голое тело', 'в стрингах из кожи дермонтина',
        'в одной бандане и перчах', 'в туристической флиске', 'в мотострингах'
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
        'скачайте приложение', 'оближите палец и поднимите его выше головы',
        'посмотрите на градусник'
    ]
    return random.choice(word_list)


def moto_telo():
    telesa_list = [
        'мото тело', 'мото братуня', 'мото приматик', 'мото сеструня',
        'манекен', 'мото маркетолог', 'мото барыга', 'тру байкер',
        'не тру байкер', 'алкомотоблогер', 'мото алконавт', 'мото турист',
        'мистер я все знаю', 'мото эксперт', 'эксперт широкого профиля',
        'стрит сракер','мото покатун','эндуровоин','ракетчик', 'мото школоло'
    ]

    return random.choice(telesa_list)

def pep_talk():
    talk = ['но вы не унывайте', 'но вы не сдавайтесь', 'но вы терпите', 
            'но вы не горюйте','но вы держитесь','но вы не расслаблятесь']
    
    return random.choice(talk)


class v:

    def cyborg_hello(self):
        return welcome_bot()

    def welcome(self):
        return welcome_word_processor()

    def seazon_start(self):
        return f"дней {timing_processor.return_dif(data_processor.data_read('seazon_start_yaer'), data_processor.data_read('seazon_start_mounth'), data_processor.data_read('seazon_start_day'))}"

    def current_temp(self):
        return int(thread_runner.system.bot_retreave_current_temperature())

    def condition(self):
        return weather_conditions_processor(
               thread_runner.system.bot_retreave_current_temperature())

    def condition2(self):
        return str.lower(thread_runner.system.bot_retreave_current_condition())

    def feature_condition(self):
        return str.lower(thread_runner.system.bot_retreave_maybe_conditions())

    def wind(self):
        return weather_wind_speed_processor(
               thread_runner.system.bot_retreave_current_wind_speed())

    def wind_speed(self):
        return int(thread_runner.system.bot_retreave_current_wind_speed())
 
    def humidity(self):
        return thread_runner.system.bot_retreave_current_humidity()

    def equip(self):
        return moto_equip_generator()

    def moto_feel(self):
        return int(thread_runner.system.bot_retreave_current_feels_like_temperature())

    def sun_s(self):
        return thread_runner.system.bot_retreave_sunrise()

    def sun_e(self):
        return thread_runner.system.bot_retreave_sunset()

    def future_temp(self):
        return int(thread_runner.system.bot_min_temperature_retreaver())

    def future_condition(self):
        return weather_conditions_processor(int(thread_runner.system.bot_min_temperature_retreaver()))

    def future_weather(self):
        return str.lower(thread_runner.system.bot_retreave_maybe_conditions())

    def moon(self):
        moon_rise = thread_runner.system.bot_retreave_moonrise()
        if moon_rise == 'no moonrise':
            return 'но не сегодня'
        else:
            return thread_runner.system.bot_retreave_moonrise()

    def destination_time(self):
        return data_processor.data_read('destination_time')

    def destination(self):
        return data_processor.data_read('destination')

    def seazon(self):
        return data_processor.data_read('seazon_reason')

    def advice(self):
        return prognoz_advise()
    
    def gif(self):
        return weather_retreaver.weather_animation_retreaver()

def weather_string_generator_long():

    weather_text_report = \
    f'<b>{v().cyborg_hello() } - {v().welcome()}, до начала {v().seazon()} осталось {v().seazon_start()}.</b>\
    \n \
    \nПогода в Киеве примерно {v().current_temp()} градусов, {v().condition()} и {v().condition2()}, а еще может быть и еще будет {v().feature_condition()}. \
    \n \
    \nВетер - {v().wind()}, вроде бы как {v().wind_speed()} км\ч.\
    \n \
    \nВлажность где-то {v().humidity()}%.\
    \n \
    \nЕсли бы мото братюня ехал {v().equip()}, то ощущал бы это примерно как {v().moto_feel()} градусов. \
    \n \
    \nСолнце встало в <code>{v().sun_s()}</code> но вы конечно же проебали этот момент, как всегда впрочем, хоть закат в <code>{v().sun_e()}</code> не проебите! \
    \n\
    \nИ еще если бы мы поехали сегодня в <b>{v().destination()}</b> в <code>{v().destination_time()}</code> то было бы {v().future_temp()} градусов, что есть {v().future_condition()}, а так же возможно {v().future_weather()} и луна взошла бы в <code>{v().moon()}</code>.\
    \n\
    \nДля более точного прогноза, {v().advice()} или как вы там привыкли это делать? \
    \n\
    \n<b>{end_word_processor()}, но вы держитесь!</b>'

    return weather_text_report


def weather_string_generator_short():

    weather_text_report = \
    f'<b>{v().cyborg_hello()} - {v().welcome()}, до начала {v().seazon()} осталось {v().seazon_start()}.</b>\
    \n \
    \n<b>Расклад по погоде:</b>\
    \nТемпература: <b>{v().current_temp()}</b> градусов,\
    \nТипа {v().condition2()},\
    \nВетер - {v().wind()}, примерно {v().wind_speed()} км\ч.\
    \nВлажность где-то {v().humidity()}%.\
    \n \
    \nЕсли бы {moto_telo()} ехал {v().equip()}, то ощущал бы это как {v().moto_feel()} градусов. \
    \n \
    \nВосход солнца в <code>{v().sun_s()}</code> \
    \nЗакат в <code>{v().sun_e()}</code> не проебите! \
    \nЛуна покажется в <code>{v().moon()}</code> \
    \n\
    \n<b>Во второй половине:</b> \
    \n{v().future_temp()} градусов, типа {v().future_condition()} \
    \nА так же возможно {v().future_weather()}.\
    \n\
    \n<b>{end_word_processor()}, {pep_talk()} !</b> \
    \n<a href="{str(v().gif())}">окрыть анимацию радара</a>'

    return weather_text_report

def weather_animation_generator():
    weather_string_animation = \
    f'\n {welcome_bot()} {moto_telo()} \
    \nТемпература: {v().condition()} ({v().current_temp()})\
    \nВетер - {v().wind()} {v().wind_speed()} км\ч.\
    \nВлажность {v().humidity()}%.\
    \n<a href="{str(v().gif())}">окрыть анимацию радара</a>'

    return weather_string_animation
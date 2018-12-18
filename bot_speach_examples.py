import random
import timing_processor
import weather_retreaver
import string
# import weather_retreaver


def weather_conditions_processor(temperature):

    conditions = ('жара ну прям пиздец',
                  'жарко так в паряде',
                  'вполне себе тепло',
                  'норм в принципе, но уже, холодновато',
                  'холодно сцуко',
                  'холодно так впоряде',
                  'холодно шопиздец',
                  'холодно так шо уши вянут',
                  'это уже и не холодно даже а смерть от обморожения',
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


def welcome_word_processor():

    word_list = ['жалкие людишки',
                 'унылые мотобратишки',
                 'несчастные кожанные мешки',
                 'мягкотелые ублюдки',
                 'человечьи шкуры',
                 'никчемные организмы',
                 'органические биомассы',
                 'тупые хомосапиенсы',
                 'cмертное мясо',
                 'земные животные',
                 'инкубаторы для микробов',
                 'глупые приматы',
                 'наборы хромосом',
                 'подвижные углеводы',
                 'скучные костяные наборы']

    return random.choice(word_list)


def end_word_processor():

    end_word = ['Сезон не начался',
                'Сезон не открылся',
                'В нормальных странах уже катают',
                'Нового мотика вам не видать',
                'На новый экип вам не хватит',
                'LS2 шлем который вы заслужили',
                'На новые мотоботы не насобирать',
                'Бенз дорогой',
                'Новую резину вам невидать',
                'Пинлок дороже шлема',
                'Масло все вытекло',
                'Лампочки все перегорели',
                'Вы в лс2 и у вас все хорошо',
                'Идёт дождь и нет дождивика',
                'Рулевая раскрутилась',
                'Резина лысая',
                'Цепь провисла',
                'Звезды стёрлись',
                'В перчах дырки']
    return random.choice(end_word)


def moto_equip_generator():
    moto_equip = ['в маркетинговом экипе',
                  'в экипе из военторга',
                  'в шортах и маечке',
                  'в мотошмотках из православного gortex',
                  'в одних труселях и перчатках',
                  'в шлепках и футболке',
                  'в кожаном прикиде',
                  'в мотокомбезе как тру гонщег',
                  'в лыжном костюме на голое тело',
                  'в стрингах из кожи дермонтина и бандане']
    return random.choice(moto_equip)


def weather_wind_speed_processor(wind_power):
    conditions = ['Штиль',
                  'слегонца дует',
                  'легкий морской бриз',
                  'немного дует',
                  'уже так впоряде поддувает',
                  'наваливает впоряде',
                  'дует неподеццки',
                  'адово наваливает',
                  'такой что походу уроган начинается',
                  'дует так что всем ховаццо нахер',
                  'наваливает так что походу нам всем пиздец',
                  'говорит что нам таки пиздец']
    wind_power = int(wind_power)
    print('RECEIVE',wind_power)

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
        print('RECEIVE',wind_power)

        return conditions[11]


def weather_string_generator():

    weather_text_report = f'Эй {welcome_word_processor()}, до начала сезона осталось {timing_processor.return_dif(2019,4,4) } дней.\
    \nПогода в Киеве примерно {int(weather_retreaver.system.bot_retreave_current_temperature())} {weather_conditions_processor(weather_retreaver.system.bot_retreave_current_temperature())} и {str.lower(weather_retreaver.system.bot_retreave_current_condition())} а еще может быть и еще будет {str.lower(weather_retreaver.system.bot_retreave_maybe_conditions()) } \
    \nВетер {weather_wind_speed_processor(weather_retreaver.system.bot_retreave_current_wind_speed())}, вроде бы как {int(weather_retreaver.system.bot_retreave_current_wind_speed())} км\ч. \
    \nВлажность где-то {weather_retreaver.system.bot_retreave_current_humidity()}\
    \nЕсли бы мото братюня ехал {moto_equip_generator()} то ощущал бы это примерно как {int(weather_retreaver.system.bot_retreave_current_feels_like_temperature()) } \
    \nСолнце встало в {weather_retreaver.system.bot_retreave_sunrise() } но вы конечно же проебали этот момент, как всегда впрочем, хоть закат в {weather_retreaver.system.bot_retreave_sunset()} не проебите \
    \nДля более точного прогноза обратитесь там к своему личному метеорологу на вашем \
    любимом айфончике или как вы это привыкли делат \
    \nИ еще если бы мы поехали сегодня в Лебедевку в {19:00} то было бы {weather_retreaver.system.bot_min_temperature_retreaver()} \
    \nчто есть {weather_conditions_processor(int(weather_retreaver.system.bot_min_temperature_retreaver()))} а так же возможно {str.lower(weather_retreaver.system.bot_retreave_maybe_conditions())} и луна взошла бы в {weather_retreaver.system.bot_retreave_moonrise() }\
    \n{end_word_processor()} но вы держитесь'
    print(weather_text_report)
    return weather_text_report
    # return

weather_string_generator()

# weather_string_generator()
#     weather_text_report = f'Эй {welcome_word_processor()} до начала сезона осталось {return_dif() } дней \
#     Погода в Киеве примерно {-6} {холодно шопиздец} и {ебошит снег} \
#     Ветер дует {ебанццо 15 км\ч}. \
#     Если бы мото братюня ехал в маркетинговом экипе то ощущал бы это примерно как {-16} \
#     Солнце встало в {14:30} но вы конечно же проебали этот момент, как всегда впрочем \
#     хоть закат в {16Ж00} не проебите у \
#     Для более точного прогноза обратитесь там к своему личному метеорологу на вашем \
#     любимом айфончике или как вы это привыкли делат \
#     И еще если бы мы поехали сегодня в {Лебедевку} в {19:00} то было бы уже \
#     {пиздец темно} и {холодно} и {взошла луна} но мы бы ее {не увидели} потому что {ебошит снег} \
#     {Сезон не открылся} но вы держитесь'

import json
import yaml
import requests
import datetime


weather_params = yaml.load(open('./data/settings/credentials.yaml'))


def weather_url_constructor(params):
    url_constructor = (weather_params['weather_url'] + params +
                       weather_params['weather_key_position'] +
                       weather_params['weather_api_token'] +
                       weather_params['city'])
    print('URL IS',url_constructor)
    return url_constructor

def weather_current_retreaver(url=weather_url_constructor(weather_params['weather_now_prefix'])):
    print('WARNING - RETREAVER for current weather called')
    weather_json_response = requests.get(url)
    return weather_json_response.text


def weather_forecast_retreaver(url=weather_url_constructor(weather_params['wether_forecast'])):
    print('WARNING - RETREAVER for all day weather called')
    weather_json_response = requests.get(url)
    return weather_json_response.text

def weather_animation_retreaver(headers= weather_params['imgur_authorisation'], 
                                base_url= weather_params['imgur_base_url'], 
                                data=weather_params['weather_gif_base_url']):
    print('Try to retreave GIF animation')

    try:
        response = requests.request('POST', base_url, headers=headers, data=data)
        print('GIF Animation Data received')
    except:
        print('Some Yebanina Is Happens', response.text)

    weather_id = json.loads(response.text)["data"]["id"]
    weather_animation = f'https://i.imgur.com/{weather_id}.gif'
    print('Generate link ', weather_animation)
    return weather_animation


class weather_formatter:
    def __init__(self):
        self._weather_now = None
        self._weather_for_day = None

    @property
    def return_day(self):
        print('property called')
        print(self._weather_now)
        return self._weather_for_day

    @property
    def return_now(self):
        print('property called')
        print(self._weather_now)
        return self._weather_now

    @return_now.setter
    def update_weather_data(self, value):
        print('setter called')
        self._weather_now = weather_current_retreaver()
        self._weather_for_day = weather_forecast_retreaver()
    
    def load_current_weather(self):
        print('LOADER ENGAGED')
        raw_data = json.loads(self._weather_now)
        return raw_data
    
    def load_forecast(self):
        print('FORECAST LODER ENGAGED')
        raw_data = json.loads(self._weather_for_day)
        return raw_data
    
    def bot_retreave_current_temperature(self):
        print('CALL TEMP')
        print(self.load_current_weather())
        print(self.load_current_weather()["main"]['temp'])
        return self.load_current_weather()["main"]['temp']

    def bot_retreave_current_condition(self):
        print(self.load_current_weather()["weather"][0]["description"])
        return self.load_current_weather()["weather"][0]["description"]

    def bot_retreave_current_wind_speed(self):
        print(self.load_current_weather()["wind"]["speed"])
        return self.load_current_weather()["wind"]["speed"]
    
    def bot_retreave_current_humidity(self):
        print(self.load_current_weather()["main"]["humidity"])
        return self.load_current_weather()["main"]["humidity"]      
    
    def bot_retreave_current_feels_like_temperature(self):
        print(self.load_current_weather()["main"]["feels_like"])
        return self.load_current_weather()["main"]["feels_like"]
    
    def bot_retreave_sunrise(self):
        print(self.load_current_weather()["sys"]["sunrise"])
        sunrise = datetime.datetime.fromtimestamp(self.load_current_weather()["sys"]["sunrise"]).strftime('%H:%M:%S')
        return sunrise

    def bot_retreave_sunset(self):
        print(self.load_current_weather()["sys"]["sunset"])
        sunset = datetime.datetime.fromtimestamp(self.load_current_weather()["sys"]["sunset"]).strftime('%H:%M:%S')
        return sunset
    
    def bot_retreave_maybe_conditions(self):
        # +3
        print(self.load_forecast()['list'][3]['weather'][0]['description'])
        return self.load_forecast()['list'][3]['weather'][0]['description']

    def bot_min_temperature_retreaver(self):
        print(self.load_forecast()['list'][3]["main"]["temp_min"])
        return self.load_forecast()['list'][3]["main"]["temp_min"]
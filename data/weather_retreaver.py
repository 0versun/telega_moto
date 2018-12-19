import json
import yaml
import requests


weather_params = yaml.load(open('./data/settings/credentials.yaml'))


def weather_url_constructor(params):
    # weather_params = yaml.load(open('credentials.yaml'))
    url_constructor = (weather_params['weather_url'] + params +
                       weather_params['weather_key_position'] +
                       weather_params['weather_api_token'] +
                       weather_params['city'])
    return url_constructor


def weather_current_retreaver(url=weather_url_constructor(weather_params['weather_now_prefix'])):
    print('RETREAVER for current weather called')
    weather_json_response = requests.get(url)
    return weather_json_response.text


def weather_forecast_retreaver(url=weather_url_constructor(weather_params['wether_forecast'])):
    print('RETREAVER for all day weather called')
    weather_json_response = requests.get(url)
    return weather_json_response.text

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
        print(self.load_current_weather()["current"]['temp_c'])
        return self.load_current_weather()["current"]['temp_c']

    def bot_retreave_current_condition(self):
        print(self.load_current_weather()["current"]["condition"]['text'])
        return self.load_current_weather()["current"]["condition"]['text']

    def bot_retreave_current_wind_speed(self):
        print(self.load_current_weather()["current"]["wind_kph"])
        return self.load_current_weather()["current"]["wind_kph"]
    
    def bot_retreave_current_humidity(self):
        print(self.load_current_weather()["current"]["humidity"])
        return self.load_current_weather()["current"]["humidity"]        
    
    def bot_retreave_current_feels_like_temperature(self):
        print(self.load_current_weather()["current"]["feelslike_c"])
        return self.load_current_weather()["current"]["feelslike_c"]

    def bot_retreave_sunrise(self):
        print(self.load_forecast()['forecast']['forecastday'][0]['astro']['sunrise'])
        return self.load_forecast()['forecast']['forecastday'][0]['astro']['sunrise']
    
    def bot_retreave_sunset(self):
        print(self.load_forecast()['forecast']['forecastday'][0]['astro']['sunset'])
        return self.load_forecast()['forecast']['forecastday'][0]['astro']['sunset']
    
    def bot_retreave_maybe_conditions(self):
        print(self.load_forecast()['forecast']['forecastday'][0]['day']['condition']['text'])
        return self.load_forecast()['forecast']['forecastday'][0]['day']['condition']['text']    

    def bot_min_temperature_retreaver(self):
        print(self.load_forecast()['forecast']['forecastday'][0]['day']['mintemp_c'])
        return self.load_forecast()['forecast']['forecastday'][0]['day']['mintemp_c']
    
    def bot_retreave_moonrise(self):
        print(self.load_forecast()['forecast']['forecastday'][0]['astro']['moonrise'])
        return self.load_forecast()['forecast']['forecastday'][0]['astro']['moonrise']


# system = weather_formatter()
# system.update_weather_data = 'Start'

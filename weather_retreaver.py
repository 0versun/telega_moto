import json
import yaml
import requests


weather_params = yaml.load(open('credentials.yaml'))


def weather_url_constructor(params):
    # weather_params = yaml.load(open('credentials.yaml'))
    url_constructor = (weather_params['weather_url'] + params +
                       weather_params['weather_key_position'] +
                       weather_params['weather_api_token'] +
                       weather_params['city'])
    return url_constructor


def weather_retreaver(url):
    weather_json_response = requests.get(url)
    return weather_json_response.text


print(weather_url_constructor(weather_params['weather_now_prefix']))
print(weather_retreaver(weather_url_constructor(
    weather_params['weather_now_prefix'])))


print(weather_url_constructor(weather_params['wether_forecast']))
print(weather_retreaver(weather_url_constructor(
    weather_params['wether_forecast'])))
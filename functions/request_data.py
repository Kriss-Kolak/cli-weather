import requests
from enum import Enum


class Current_Weather(Enum):
    CURRENT = 'current'
    TEMPERATURE = 'temperature_2m'

class Hourly_Weather(Enum):
    HOURLY = 'hourly'
    TEMPERATURE = 'temperature_2m'



def get__current_temperature(latitude: float, longitude: float) -> tuple[float, str]:

    if latitude < -90 or latitude > 90:
        raise Exception(f"LATITUDE HAS TO BE IN RANGE (-90 - 90), current value: {latitude}")

    if longitude < -180 or longitude > 180:
        raise Exception(f"LONGITUDE HAS TO BE IN RANGE (-180 - 180), current value: {longitude}")

    params = params = {
        "latitude": latitude,
        "longitude": longitude,
        Current_Weather.CURRENT.value: Current_Weather.TEMPERATURE.value,
    }

    r = requests.get('https://api.open-meteo.com/v1/forecast', params=params)

    if r.status_code == 200:
        json_object = r.json()
        temperature = json_object[Current_Weather.CURRENT.value][Current_Weather.TEMPERATURE.value]
        temperature_unit = json_object['current_units'][Current_Weather.TEMPERATURE.value]
        return (float(temperature), temperature_unit)

    else: 
        raise Exception(f"STATUS CODE: {r.status_code}")
    
def get_7_day_forecast(latitude: float, longitude: float) -> list[tuple[str, tuple[float, str]]]:

    if latitude < -90 or latitude > 90:
        raise Exception(f"LATITUDE HAS TO BE IN RANGE (-90 - 90), current value: {latitude}")

    if longitude < -180 or longitude > 180:
        raise Exception(f"LONGITUDE HAS TO BE IN RANGE (-180 - 180), current value: {longitude}")

    params = params = {
        "latitude": latitude,
        "longitude": longitude,
        Hourly_Weather.HOURLY.value: Hourly_Weather.TEMPERATURE.value,
    }

    r = requests.get('https://api.open-meteo.com/v1/forecast', params=params)

    if r.status_code == 200:
        json_object = r.json()

        temperature_units = json_object['hourly_units']['temperature_2m']
        time_list = json_object['hourly']['time']
        temperature_list = json_object['hourly']['temperature_2m']
        result_list = []
        for time, temp in zip(time_list, temperature_list):
            result_list.append((time, (float(temp), temperature_units)))
        return result_list
    else: 
        raise Exception(f"STATUS CODE: {r.status_code}")
    
def get_city_name(latitude: float, longitude: float) -> str:
    if latitude < -90 or latitude > 90:
        raise Exception(f"LATITUDE HAS TO BE IN RANGE (-90 - 90), current value: {latitude}")

    if longitude < -180 or longitude > 180:
        raise Exception(f"LONGITUDE HAS TO BE IN RANGE (-180 - 180), current value: {longitude}")

    params = params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json"
    }

    r = requests.get('https://nominatim.openstreetmap.org/reverse', params=params, headers={"User-Agent": "cli-weather-app"})

    if r.status_code == 200:
        json_object = r.json()
        if 'address' in json_object and 'city' in json_object['address']:
            return json_object['address']['city']
        elif 'address' in json_object and 'town' in json_object['address']:
            return json_object['address']['town']
        elif 'address' in json_object and 'village' in json_object['address']:
            return json_object['address']['village']
        else:
            return "Unknown Location"
    else: 
        raise Exception(f"STATUS CODE: {r.status_code}")
    

def get_lat_lon_from_city(city: str) -> tuple[float, float]:
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    r = requests.get('https://nominatim.openstreetmap.org/search', params=params, headers={"User-Agent": "cli-weather-app"})

    if r.status_code == 200:
        json_object = r.json()
        if len(json_object) == 0:
            raise Exception(f"CITY '{city}' NOT FOUND")
        latitude = float(json_object[0]['lat'])
        longitude = float(json_object[0]['lon'])
        return (latitude, longitude)
    else: 
        raise Exception(f"STATUS CODE: {r.status_code}")
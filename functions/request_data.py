import requests
from enum import Enum


class Current_Weather(Enum):
    CURRENT = 'current'
    TEMPERATURE = 'temperature_2m'

class Hourly_Weather(Enum):
    HOURLY = 'hourly'
    TEMPERATURE = 'temperature_2m'



def get__current_temperature(latitude: float, longitude: float) -> tuple[float, str]:

    if latitude < 0 or latitude > 90:
        raise Exception(f"LATITUDE HAS TO BE IN RANGE (0 - 90), current value: {latitude}")
    
    if longitude < 0 or longitude > 90:
        raise Exception(f"LONGITUDE HAS TO BE IN RANGE (0 - 90), current value: {longitude}")
    
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

    if latitude < 0 or latitude > 90:
        raise Exception(f"LATITUDE HAS TO BE IN RANGE (0 - 90), current value: {latitude}")
    
    if longitude < 0 or longitude > 90:
        raise Exception(f"LONGITUDE HAS TO BE IN RANGE (0 - 90), current value: {longitude}")
    
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
        print(json_object)
        result_list = []
        for time, temp in zip(time_list, temperature_list):
            print(f"{time} : {temp} {temperature_units}")
            result_list.append((time, (float(temp), temperature_units)))
        return result_list
    else: 
        raise Exception(f"STATUS CODE: {r.status_code}")
    

import sys
import argparse


from functions.request_data import get__current_temperature, get_7_day_forecast, get_city_name, get_lat_lon_from_city
from functions.create_plot import create_plot

def main():
    parser = argparse.ArgumentParser(description="Get the current temperature for a given latitude and longitude")    
    parser.add_argument("--lat", type=float, help="Latitude of the location")
    parser.add_argument("--lon", type=float, help="Longitude of the location")
    parser.add_argument("--city", type=str, help="City name to get the latitude and longitude from")
    parser.add_argument("--forecast", action="store_true", help="Plot the 7 day forecast")

    parser.parse_args()
    args = parser.parse_args()
    latitude = args.lat
    longitude = args.lon
    city = args.city
    forecast = args.forecast

    if forecast:
        if city:
            latitude, longitude = get_lat_lon_from_city(city)
            if latitude is None or longitude is None:
                print(f"Could not find city: {city}")
                sys.exit(1)
        elif latitude is None or longitude is None:
            print("Latitude and longitude must be provided for forecast.")
            sys.exit(1)
        city = get_city_name(latitude, longitude)
        forecast_data = get_7_day_forecast(latitude, longitude)
        times = [data[0] for data in forecast_data]
        temperatures = [data[1][0] for data in forecast_data]
        plot = create_plot(times, temperatures, latitude, longitude, city)
        print(plot)
    else:
        if city:
            latitude, longitude = get_lat_lon_from_city(city)
            if latitude is None or longitude is None:
                print(f"Could not find city: {city}")
                sys.exit(1)
        elif latitude is None or longitude is None:
            print("Latitude and longitude must be provided.")
            sys.exit(1)
        temperature, unit = get__current_temperature(latitude, longitude)
        if city:
            print(f"Current temperature in {city} (Lat: {latitude}, Lon: {longitude}): {temperature} {unit}")
        else:
            print(f"Current temperature at Latitude: {latitude}, Longitude: {longitude}: {temperature} {unit}")



if __name__ == "__main__":
    main()
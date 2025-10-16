import sys

from functions.request_data import get__current_temperature
from functions.create_plot import create_plot
def main():
    """
    Main function to run the CLI weather application
    """
    if len(sys.argv) != 3:
        print("Usage: python3 cli-weather.py <latitude> <longitude>")
        return

    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python3 cli-weather.py <latitude> <longitude>")
        print("Example: python3 cli-weather.py 52.52 13.405")
        return

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except ValueError:
        print("Latitude and longitude must be valid numbers.")
        return

    print(get__current_temperature(latitude, longitude))

if __name__ == "__main__":
    create_plot([10,11,12],[10,15,18])

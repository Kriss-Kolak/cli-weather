# CLI Weather

A simple command-line tool to get current weather and 7-day forecasts for any location using the Open-Meteo API.

## Features
- Get current temperature by latitude/longitude or city name
- Get and plot a 7-day temperature forecast
- ASCII plot output for quick visualization

## Requirements
- Python 3.8+
- `requests` library

Install dependencies:
```sh
pip install -r requirements.txt
```

## Usage
Run the main script from the project root:

### Get current temperature by coordinates
```sh
python cli-weather.py --lat 51.02 --lon 19.02
```

### Get current temperature by city name
```sh
python cli-weather.py --city Paris
```

### Get and plot 7-day forecast by city name
```sh
python cli-weather.py --city Paris --forecast
```

### Get and plot 7-day forecast by coordinates
```sh
python cli-weather.py --lat 51.02 --lon 19.02 --forecast
```

## Arguments
- `--lat` (float): Latitude of the location
- `--lon` (float): Longitude of the location
- `--city` (str): City name (overrides lat/lon if provided)
- `--forecast`: Show 7-day forecast plot instead of current temperature

## Project Structure
```
cli-weather.py           # Main CLI script
config/                  # Configuration constants
functions/               # Core logic (API, plotting, etc.)
tests/                   # Unit tests
requirements.txt         # Python dependencies
```

## Testing
Run all tests with:
```sh
python -m unittest discover
```

## License
MIT

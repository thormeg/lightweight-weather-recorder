from flask import Blueprint, render_template, request
from typing import List, NamedTuple 
from weather_recorder import db
from weather_recorder.models import Weather

weather_charts = Blueprint('weather_charts', __name__)

class WeatherRecords(NamedTuple):
    dates: List
    temps_high: List
    temps_low: List
    wind: List
    pressure: List
    rain: List


def get_all_weather():
    session = db.session
    result = session.query(Weather).all()

    dates = []
    temps_high = []
    temps_low = []
    wind = []
    pressure = []
    rain = []

    for row in result:
        dates.append(str(row.date_taken)[0:10])
        temps_high.append(row.temperature_high)
        temps_low.append(row.temperature_low)
        wind.append(row.wind_kmh)
        pressure.append(row.pressure)
        rain.append(row.rainfall_mm)

    all_weather = WeatherRecords(
        dates,
        temps_high,
        temps_low,
        wind,
        pressure,
        rain)
    # print(all_weather)
    return all_weather


@weather_charts.route('/chart_all_temps', methods=['GET', 'POST'])
def chart_all_temps():
    w = get_all_weather()
    print(w)
    return render_template(
        'charts/chart_all_temps.html',
        title='Weather Charts',
        labels=w.dates,
        temps_low=w.temps_low,
        temps_high=w.temps_high
    )


@weather_charts.route('/chart_pressure', methods=['GET', 'POST'])
def chart_pressure():
    w = get_all_weather()
    return render_template(
        'charts/chart_pressure.html',
        title='Weather Charts',
        labels=w.dates,
        pressure=w.pressure
    )


@weather_charts.route('/chart_rain', methods=['GET', 'POST'])
def chart_rain():
    w = get_all_weather()
    return render_template(
        'charts/chart_rain.html',
        title='Weather Charts',
        labels=w.dates,
        rain=w.rain
    )


@weather_charts.route('/chart_wind', methods=['GET', 'POST'])
def chart_wind():
    w = get_all_weather()
    return render_template(
        'charts/chart_wind.html',
        title='Weather Charts',
        labels=w.dates,
        wind=w.wind
    )

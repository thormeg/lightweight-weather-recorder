from flask import Blueprint, render_template, request
from weather_recorder import db
from weather_recorder.models import Weather

weather_charts = Blueprint('weather_charts', __name__)


@weather_charts.route('/weather_charts', methods=['GET', 'POST'])
def charts():
    session = db.session
    result = session.query(Weather).all()
    print(f'weather details: {type(result[0])}')
    temps_high: list = []
    temps_low: list = []
    dates: list = []
    for row in result:
        dates.append(str(row.date_taken)[0:10])
        temps_high.append(row.temperature_high)
        temps_low.append(row.temperature_low)

    return render_template(
        'weather_chart.html',
        title='Weather Charts',
        labels=dates,
        temps_low=temps_low,
        temps_high=temps_high
    )

from datetime import date

from flask_wtf import FlaskForm
from weather_recorder.main.date_formatter.date_formatter import format_date
from weather_recorder.main.wind_directions import wind_directions
from weather_recorder.models import Weather
from wtforms import DateField, IntegerField, StringField, SubmitField
from wtforms.validators import ValidationError


def validate_date(form, date_taken):
    if date_taken.data:
        print(f'Attempting to validate with: {date_taken.data}')
        date_taken.data = format_date(str(date_taken.data))
        post_date = Weather.query.filter_by(date_taken=form.date_taken.data).first()
        if post_date:
            raise ValidationError(f'Reading already taken for {date_taken.data}.')


def validate_wind_direction(form, wind_direction):
    direction = wind_direction.data
    if direction and direction in wind_directions:
        pass
    else:
        raise ValidationError(f'Incorrect wind direction: {direction}')


class WeatherForm(FlaskForm):
    date_taken = DateField('Date Taken',
                           validators=[validate_date], default=date.today())
    temperature_low = IntegerField('Temp. Low')
    temperature_high = IntegerField('Temp. High')
    wind_kmh = IntegerField('Wind (km/h)')
    rainfall_mm = IntegerField('Rainfall(mm)')
    wind_direction = StringField('Wind Direction', validators=[validate_wind_direction])
    pressure = IntegerField('Pressure (bars)')
    submit = SubmitField('Submit reading')

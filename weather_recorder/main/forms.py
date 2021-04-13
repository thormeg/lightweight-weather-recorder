from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SubmitField
from wtforms.validators import ValidationError
from weather_recorder.models import Weather


def validate_date(form, date_taken):
    if date_taken.data:
        print(f'Attempting to validate with: {date_taken.data}')
        date_taken.data = datetime.strptime(
            str(date_taken.data) + ' 00:00:00.000001'
            , '%Y-%m-%d %H:%M:%S.%f')
        post_date = Weather.query.filter_by(date_taken=form.date_taken.data).first()
        if post_date:
            raise ValidationError(f'Reading already taken for {date_taken.data}.')


class WeatherForm(FlaskForm):
    date_taken = DateField('Date Taken',
                           validators=[validate_date], default=date.today())
    temperature_low = IntegerField('Temp. Low')
    temperature_high = IntegerField('Temp. High')
    wind_kmh = IntegerField('Wind (km/h)')
    rainfall_mm = IntegerField('Rainfall(mm)')
    submit = SubmitField('Submit reading')

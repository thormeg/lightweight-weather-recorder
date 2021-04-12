from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from weather_recorder.models import Weather


class WeatherForm(FlaskForm):
    date_taken = DateField('Date Taken',
                           validators=[DataRequired()])
    temperature_low = IntegerField('Temp. Low')
    temperature_high = IntegerField('Temp. High')
    wind_kmh = IntegerField('Wind (km/h)')
    rain_mm = IntegerField('Rainfall(mm)')
    submit = SubmitField('Submit reading')

    def validate_date(self, date_taken):
        post_date = Weather.query.filter_by(date_taken=date_taken.data).first()
        if post_date:
            raise ValidationError(f'Reading already taken for {date_taken}.')

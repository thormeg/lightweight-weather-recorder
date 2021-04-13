from flask import render_template, url_for, flash, redirect, Blueprint
from weather_recorder import db
from weather_recorder.main.forms import WeatherForm
from weather_recorder.models import Weather

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
@main.route("/home", methods=['GET', 'POST'])
@main.route("/index", methods=['GET', 'POST'])
def home():
    form = WeatherForm()
    if form.validate_on_submit():
        weather_report = Weather(
            date_taken=form.date_taken.data,
            temperature_low=form.temperature_low.data,
            temperature_high=form.temperature_high.data,
            wind_kmh=form.wind_kmh.data,
            rainfall_mm=form.rainfall_mm.data)
        db.session.add(weather_report)
        db.session.commit()
        flash('Your weather reading has been successfully saved.', 'success')
        return redirect(url_for('main.home'))
    return render_template('home.html', form=form)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

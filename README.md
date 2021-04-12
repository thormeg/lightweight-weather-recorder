# flask-weather-recorder
A reimplementation of my C#/WPF weather recorder using Flask and a SQLite database


# Create DB:
$ from weather_recorder import db, create_app
$ app = create_app()
$ db.create_all(app=app)

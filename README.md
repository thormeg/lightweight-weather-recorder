# Lightweight weather recorder
A small weather recording application built from a Flask backend utilising Bootstrap for styling and CSS on the frontend.

![image](https://user-images.githubusercontent.com/66360292/116109223-e1599280-a6b4-11eb-9e75-e43fd173c93c.png)

Graphs are enabled by Graph.js and fed by the SQLite database. These are highly configurable.
![image](https://user-images.githubusercontent.com/66360292/116109579-37c6d100-a6b5-11eb-9486-f87f4ffd9a3c.png)


# Create DB:
`$ from weather_recorder import db, create_app`

`$ app = create_app()`

`$ db.create_all(app=app)`

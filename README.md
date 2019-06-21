# Flask-leaflet-example
Application Flask leaflet 

Créer une base de données PostgresSQL:
`sudo apt.get install postgressql`

Devenir utilisateur Postgres:
`su postgres`

Créer un utilisateur PostgresSqL:
`create user myuser with encrypted password 'mypass'`

Créer la base de données:
`createdb testdb`

Créer un virtualenv:
`virtualenv -p python3 venv`

Activer virtualenv:
`source venv/bin/activate`

Installer les librairies python:
`pip install -r requirements.txt`

Adapter le fichier `app/routes.py` en y mettant vos identifiant de BDD

Lancer l'application:
`python run.py`


Fait à partir du tuto:"https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates"

par Bertochio Titouan

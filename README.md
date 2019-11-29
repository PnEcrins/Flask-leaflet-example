# Flask-leaflet-example

Application Python Flask Leaflet comprenant un formulaire et une carte affichant les données saisies dans le formulaire.

Sur Linux Ubuntu, installer le moteur de base de données PostgreSQL :

`sudo apt-get install postgresql`

Se connecter avec l'utilisateur ``postgres`` :

`su postgres`

Créer un utilisateur PostgreSQL :

`create user myuser with encrypted password 'mypass'`

Créer la base de données :

`createdb testdb`

Créer un virtualenv :

`virtualenv -p python3 venv`

Activer virtualenv :

`source venv/bin/activate`

Installer les librairies python :

`pip install -r requirements.txt`

Adapter le fichier `app/routes.py` en y mettant vos identifiants de connexion à la BDD

Lancer l'application :

`python run.py`

**Auteur** : Titouan Bertochio / Juin 2019

Réalisé à partir du tutoriel https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

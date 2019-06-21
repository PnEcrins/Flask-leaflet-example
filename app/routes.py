from flask import Flask, render_template, flash, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from .env import DB
from app.models import User
from app.forms import LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://titouan_pg:titouan@localhost:5432/mabase"

with app.app_context():
    from .models import User
    from app.forms import LoginForm
    from .env import DB
    DB.init_app(app)
    DB.create_all()

    User.query.all()


@app.route("/")
@app.route("/map")
def map():
    
    data = DB.session.query(User).all()
    return render_template('map.html', title='Map', users=data)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = LoginForm()
    if form.validate_on_submit():
        data = request.form
        user = User(
            surname=data['surname'],
            email=data['email'],
            name=data['name'],
            X=data['X'],
            Y=data['Y']
        )
        DB.session.add(user)
        DB.session.commit()
        return render_template('map.html')
    else:
        return render_template('add.html', title="Add_to_map", form=form )

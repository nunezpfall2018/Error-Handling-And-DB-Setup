#** Nunez,Priscilla 
#** SI 364 
#** Fall 2018

#** Note: Code is my own, any students I have tutored using my code must include that I have 
#** helped tutor them on ALL homework assignments using my code in SI 206, SI 339 and SI 364. 
#** Please notify our GSIs and Professors.
#** ---> Tutor: Nunez, Priscilla 
#** (Include what assignment number here, also include the lines of code and what you learned by the code used.)

import os
from flask import Flask, render_template, session, redirect, url_for, request
from flask_script import Shell, Manager
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

#** Configured base directory of app
basedir = os.path.abspath(os.path.dirname(__file__))

#** Application configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstringfromsi364thisisnotsupersecurebutitsok'

#** Challenge 2.1 : Update the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://D5@localhost:5432/moviedb"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #** For database use

#** Set up Postico and saw there is also an option to add database

##### Set up Models #####
#** Challenge 2.2: Wrote models for the tables Movie and Director

class Movie(db.Model):                                     #** Similar logic used for Example Tweets and Users in class
    __tablename__ = 'movies'
    movieId = db.Column(db.Integer, primary_key=True)
    movieTitle = db.Column(db.String(64))
    directorId = db.Column(db.Integer, db.ForeignKey('directors.directorId'))

    def __repr__(self):
        return '<Movie %r>' % self.movieTitle

class Director(db.Model):
    __tablename__ = 'directors'
    directorId = db.Column(db.Integer, primary_key=True)   #** primary key provides unique ID
    directorName =  db.Column(db.String(64))               #** keeping same as movie title 64
    #** Completed the model for Director based on the information provided in section notes

if __name__=='__main__':
    db.create_all()
    app.run()

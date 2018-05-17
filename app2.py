from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import uuid
from passlib.hash import sha256_crypt 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///json.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)

from os import path
from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['SECRET_KEY']=""""""
app.config['MYSQL_HOST']=''
app.config['MYSQL_USER']=''
app.config['MYSQL_PASSWORD']=''
app.config['MYSQl_DB']='student'
app.config['MYSQL_CURSORCLASS']='DictCursor'
db=MySQL(app)

    

from .auth import auth
from .views import views
app.register_blueprint(auth,url_prefix='/')
app.register_blueprint(views,url_prefix='/')

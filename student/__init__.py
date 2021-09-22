from os import path
from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
app.config['SECRET_KEY']="1234455ugugfugkagjkgkjdhiuaht4y5i4itgui43htui4hjkfhuh"
app.config['MYSQL_HOST']='stud123.mysql.database.azure.com'
app.config['MYSQL_USER']='student@stud123'
app.config['MYSQL_PASSWORD']='stud1@34'
app.config['MYSQl_DB']='student'
app.config['MYSQL_CURSORCLASS']='DictCursor'
db=MySQL(app)
    

from .auth import auth
from .views import views
app.register_blueprint(auth,url_prefix='/')
app.register_blueprint(views,url_prefix='/')
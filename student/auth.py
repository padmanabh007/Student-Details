from flask import request,render_template,redirect,flash,Blueprint,url_for,session
from .forms import LoginForm,RegisterForm
from werkzeug.security import generate_password_hash,check_password_hash
from . import db

auth = Blueprint('auth',__name__)


@auth.route('/', methods = ['GET', 'POST'])
def login():
    
    c  =  db.connection.cursor()
    forms = LoginForm()
    if forms.validate_on_submit() or request.method == 'POST':

        email = forms.email.data
        password = forms.password.data
        query = """SELECT password FROM student.student WHERE email = %s"""
        c.execute(query,(email,))
        pass_word = c.fetchone()
        print(check_password_hash(pass_word['password'],password))
        if check_password_hash(pass_word['password'], password) :

            c.execute("""SELECT id FROM student.student WHERE email = %s""",(email,))
            idn  =  c.fetchone()
            flash('Logged in Successfully',"success")
            session['id']=idn['id']
            #login_user(idn['id'])
            return redirect(url_for("views.view",idn = idn["id"]))

        else: 
            flash("Incorrect Email or Password","danger")
        c.close()

    return render_template('login.html',title = 'loginpage',form = forms)

@auth.route('/register',methods = [ 'POST','GET'])
def register():
    forms = RegisterForm()
    c = db.connection.cursor()
    if forms.validate_on_submit() or request.method == "POST":

        email = forms.email.data
        password = forms.password.data
        query = """SELECT id FROM student.student WHERE email = %s"""
        c.execute(query,(email,))
        id1  =  c.fetchone()

        if id1:
            flash("Email Id already exists","danger")
        else:

            query = """INSERT INTO student.student (email,password) VALUES (%s, %s)"""
            c.execute(query,(email,generate_password_hash(password),))
            db.connection.commit()
            c.execute("""SELECT id FROM student.student WHERE email = %s""",(email,))
            idn = c.fetchone()
            session['id']=idn['id']
            #login_user(idn['id'])
            flash('Fill this form to complete your registration')
            return redirect(url_for("views.edit",idn = idn))
        c.close()
        
    return render_template('register.html',title = 'register',form = forms)

@auth.route('/logout',methods=[ 'POST', 'GET']) 
#@login_required
def logout():
    session.pop('id', None)
    flash("You have been logged out sucessfully.....")
    return redirect(url_for('auth.login'))
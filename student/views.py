from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from . import db

views = Blueprint('views',__name__)

@views.route('/login/view/<idn>',methods = [ 'POST','GET'])
def view(idn):
    if not session.get('id'):
        flash("Login to access ..........")
        return redirect(url_for('auth.login'))
    c = db.connection.cursor()
    query = """SELECT * FROM student.student WHERE id = %s"""
    c.execute(query,(idn,))
    data = c.fetchone()
    if request.method == "POST":
        flash("You can now edit your details",category = "warning")
        return redirect(url_for("views.sedit",idn = data["id"]))
    c.close()
    return render_template("view.html",title = "details",form = data)


@views.route('/register/edit/<idn>',methods = ['POST','GET'])
def edit(idn):
    if not session.get('id') :
        flash("Login to access ..........")
        return redirect(url_for('auth.login'))
    
    c = db.connection.cursor()
    if request.method == "POST" :
        
        regno = request.form.get('stdregno')
        name = request.form.get('stdname')
        pname = request.form.get('stdpname')
        age = request.form.get('stdage')
        dob = request.form.get('stddob')
        dept = request.form.get('stddept')
        sem = request.form.get('stdpresem')
        avggpa = request.form.get('stdavgpa')
        pho = request.form.get('stdphone')
        add = request.form.get('stdaddres')
        city = request.form.get('stdcity')
        state = request.form.get('stdstate')
        pin = request.form.get('stdpin')
        query = """UPDATE student.student SET regno = %s,name = %s,parentname = %s,age = %s,DOB = %s,department = %s,presentsem = %s,avggpa = %s,phonenum = %s,address = %s,city = %s,state = %s,PIN = %s WHERE id = %s"""
        data = (regno,name,pname,age,dob,dept,sem,avggpa,pho,add,city,state,pin,idn,)
        c.execute(query,data)
        db.connection.commit()
        c.close()
        flash("Details saved successfully!!!",category = "success")
        return redirect(url_for('views.view',idn=idn))

    return render_template("edit.html",title = "update")

@views.route('/login/sedit/<idn>',methods = ['GET','POST'])
def sedit(idn):
    if not session.get('id'):
        flash("Login to access ..........")
        return redirect(url_for('auth.login'))

    cur =  db.connection.cursor()
    query = ""'SELECT * FROM student.student WHERE id = %s'""
    cur.execute(query,(idn,))
    data = cur.fetchone()
    if request.method == 'POST':
        dept = request.form.get('stddept')
        sem = request.form.get('presem')
        avggpa = request.form.get('stdavgpa')
        add = request.form.get('stdaddres')
        city = request.form.get('stdcity')
        state = request.form.get('stdstate')
        pin = request.form.get('stdpin')

        query = """UPDATE student.student SET department = %s,presentsem = %s,avggpa = %s,addresss = %s,city = %s,state = %s,PIN = %s WHERE id = %s"""
        data = (dept,sem,avggpa,add,city,state,pin,idn,)
        cur.execute(query,data)
        db.connection.commit()
        cur.close()

        flash('Details Updated !!! Login Again')
        return redirect(url_for('auth.login'))
    cur.close()

    return render_template('sedit.html',title = 'change',form = data)

@views.route('/admin/full/', methods=['GET', 'POST'])
def full():
    if not session.get('id') or session.get('id') != 'Admin':
        flash('Admin should login to view this page')
        return redirect(url_for('auth.admin'))
    c=db.connection.cursor()
    c.execute("""SELECT * FROM student.student""")
    data = c.fetchall()
    if request.method == 'POST':
        regno=request.form.get('stdregno')
        c.execute('''DELETE FROM student.student WHERE regno = %s''',(regno,))
        db.connection.commit()
        c.close()
        flash('Details deleted successfully !!')
        return redirect(url_for('admin.html'))
    return render_template('admin.html',title='Full details',form=data)
    


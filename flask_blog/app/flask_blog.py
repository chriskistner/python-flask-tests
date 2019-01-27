from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from dbcon import DB_URL, get_env_variable

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ohtheironcewasastoryaboutaguynamedalandhelivedinthesewerswithhislobsterpals'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db=SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20), unique= True, nullable= False )
    email = db.Column(db.String(120), unique= True, nullable= False )
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Book', backref='author', lazy=True)

    def __repr__(self):
        return f"user('{self.username}, {self.email}, {self.image}')" 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    date_published = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"user('{self.title}, {self.date_published}')" 




books = [
    {
        "author": "Chris Kistner",
        "title": "The Pangaea Project: Homecoming",
        "description": "The epic adventure of the Space Colony Pangaea as it returns to Earth.",
        "date_published": '10/15/2012'
    },
        {
        "author": "Chris Kistner",
        "title": "The Pangaea Project: Revenants",
        "description": "The Adventure Continues as Colonel West leads an infiltration team to Earth.",
        "date_published": '4/8/2015'
    }
]

@app.route("/")
@app.route("/home")
def home():
    print(get_env_variable('POSTGRES_DB'))
    return render_template('home.html', books=books)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods= ['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@books.com' and form.password.data == 'password':
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else: 
            flash('Login Failed', 'danger') 
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug = True)
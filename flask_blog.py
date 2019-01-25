from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ohtheironcewasastoryaboutaguynamedalandhelivedinthesewerswithhislobsterpals'

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
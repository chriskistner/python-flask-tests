from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)
# save this as app.py
from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [ 
    {
        'author': 'Tristan Klinski',
        'title': 'Blog Post 1',
        'content': 'My over is not on the Jets',
        'date_posted': 'January 31st, 2022'
    },
    {
        'author': 'Tristan Klinski',
        'title': 'Blog Post 2',
        'content': 'My under is still not on the Jets',
        'date_posted': 'February 1st, 2022'
    }
]

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
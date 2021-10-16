from flask import Flask, render_template

#if you dont feel like running w/ file
    # TO START run this in terminal:
    # cd "C:\Users\Seth Mueller\Documents\programs\GitHub\flask-website"   
    # set FLASK_APP=flaskblog.py
    # set FLASK_DEBUG=1                      you dont need to reset evrytime
    # flask run

#if you get a error run this MUST RUN AS ADMIN (win 10)
    # netstat -ano | find ":5000"            finds things running on :5000 (:5000 can be replaced w/ any port)
    # TASKKILL /F /PID <process id>          pro id is to far right of prev

#

app = Flask(__name__)

posts =  [
    {
        'author': 'Elen Musk',
        'title': 'blog post 1',
        'content': 'tesla',
        'date': 'April 12, 2009'
    },
    {
        'author': 'lebrohn Jahmez',
        'title': 'blog post 2',
        'content': 'basketbell here',
        'date': 'April 13, 1902'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',  posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

#runs the app w/ debug (auto update)
if __name__ == '__main__':
    app.run(debug=True, port=8089)
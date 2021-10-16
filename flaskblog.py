from flask import Flask

app = Flask(__name__)

#if you dont feel like running w/ file
    # TO START run this in terminal:
    # cd "C:\Users\Seth Mueller\Documents\programs\GitHub\flask-website"   
    # set FLASK_APP=flaskblog.py
    # set FLASK_DEBUG=1                      you dont need to reset evrytime
    # flask run

#if you get a error run this MUST RUN AS ADMIN:
# netstat -ano | find ":5000"            finds things running on :5000 (:5000 can be replaced w/ any port)
# TASKKILL /F /PID <process id>          pro id is to far right of prev

#

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

#runs the app w/ debug (auto update)
if __name__ == '__main__':
    app.run(debug=True, port=8089)
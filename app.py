# Web application built with the Python Flask (version 0.12.2) framework for www.funtasticapps.com 
from flask import Flask, render_template

# initialize application
app         = Flask(__name__)

# configure routing
@app.route('/')
def home():
    return render_template('home.html')
    # return "Welcome to my Python Flask web application"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')    
# start application
# From a command line, start the app with command "python index.py"
# app will be served on port 5000 via http://localhost:5000/ 
if __name__ == '__main__':
    app.run(debug=True)


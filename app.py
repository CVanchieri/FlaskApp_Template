### necessary imports ### 
from flask import Flask, render_template


# FalconSQL Login https://api.plot.ly/

"""Create and configure an instance of the Flask application"""
app = Flask(__name__)

### local development ###
# app.config['TESTING'] = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True
# app.config['STATIC_AUTO_RELOAD'] = True
# app.run(debug=True)

### home page ###
@app.route('/')
def root():
    return render_template('home.html')

### page1 ###
@app.route('/page1')
def page1():
    return render_template('page.html')

### page2 ###
@app.route('/page2')
def page2():
    return render_template('page.html')

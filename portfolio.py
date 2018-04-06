from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')
    # return "<h1 style='background-color:pink;color:green;font:45px arial,sans-serif'>Updated Hello World!<h1>"

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')




app.run(debug=True)
"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

time = 10

@app.route('/')
def hello():
    return render_template("html test.html")

@app.route("/test", methods=["POST", "GET"])
def test():
    return render_template("html test.html", time=time)

@app.route("/bad")
def warning_site():
    

@app.route("/saveminutes", methods=["GET"])
def saveminutes():
    global time 
    time = request.args.get("minutes")
    if int(time) > 0:
        print (time)
        return test()
    else:
        return warning_site()


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(host='0.0.0.0')



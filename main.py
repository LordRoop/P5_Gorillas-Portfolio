from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/projects.html')
def projects():
    return render_template("projects.html")


if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port=' 5000', host='192.168.86.51')
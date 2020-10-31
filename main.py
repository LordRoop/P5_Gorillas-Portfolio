from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL to a function
@app.route('/')
def home():
    #Flask import uses Jinga to render HTML
    return render_template("home.html")

@app.route('/projects')
def projects():
    #Flask import uses Jinga to render HTML
    return render_template("projects.html")

@app.route('/journals')
def journals():
    #Flask import uses Jinga to render HTML
    return render_template("journals.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port=' 5000', host='192.168.86.45')
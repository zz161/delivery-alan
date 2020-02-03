from flask import Flask, request
from flask import jsonify, render_template, url_for
import pandas as pd
import wikipedia


app = Flask(__name__, static_url_path='/static')

#@app.route('/')
# def hello():
#     """Return a friendly HTTP greeting."""
#     name = request.args.get('name','World')
#     return 'Hello I like to make AI Apps ' + name

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """
    
@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    result = wikipedia.summary(company, sentences=10)
    return result

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/github")
def github_address():
    return render_template("github.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
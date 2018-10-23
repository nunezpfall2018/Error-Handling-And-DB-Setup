#** Nunez,Priscilla 
#** SI 364 
#** Fall 2018

#** Note: Code is my own, any students I have tutored using my code must include that I have 
#** helped tutor them on ALL homework assignments using my code in SI 206, SI 339 and SI 364. 
#** Please notify our GSIs and Professors.
#** ---> Tutor: Nunez, Priscilla 
#** (Include what assignment number here, also include the lines of code and what you learned by the code used.)

from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

#** Challenge 1: Returned the 404.html template
#** Edited message variations

#** Challenge 2: Included the link to homepage i.e. http://localhost:5000 in 404.html.

#** Challenge 3: Wrote an error handler for 500 error. Simulated Internal Server Error.
#** Challenge 4: Edited the 500.html template to display link to homepage and link to itunes-form.


@app.route('/')
def index():
    raise Exception('This is an example of a python exception error - Fall2018 student.')
    return "Hello, World!"

@app.route('/itunes-form')
def ituneForm():
    return render_template('itunes-form.html')

@app.route('/itunes-result')
def resultTunes():
    artist = request.args.get('artist')           #** Request Artist in blank 
    num = request.args.get('num')                 #** Select number of listings 5 through 15

    url = "https://itunes.apple.com/search"
    params = {"media": "music", "term": artist, "limit": num}
    get_name = requests.get(url, params = params)
    json_format = json.loads(get_name.text)
    context = {
        'results': json_format["results"],
    }
    return render_template('list.html', **context)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    #** OPTION raise Exception('This is an example of a python exception error - nunezp.') Placement would be up by index.


if __name__ == '__main__':
    app.run(debug = True)

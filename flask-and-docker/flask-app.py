from flask import Flask, jsonify, request
from main import main

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def get_post_data():
    
    if request.method == 'POST':

        data = request.get_json()
        # app.logger.error("got JSON, next is getting url from JSON")

        url_string = data['url']
        # app.logger.error("Here's the url: " + url_string)

        rv = main(url_string)

        resp = jsonify(success=True, score=rv)
        return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')

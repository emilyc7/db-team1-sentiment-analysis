from flask import Flask, request
from main import main

app = Flask(__name__)

@app.route('/sentiment', methods = ['POST'])
def get_post_data():
    data = request.get_json()
     # app.logger.error("got JSON, next is getting url from JSON")

    url_string = data['url']
    # app.logger.error("Here's the url: " + url_string)
 
    rv = main(url_string)
    return rv

if __name__ == "__main__":
    app.run(host='0.0.0.0')

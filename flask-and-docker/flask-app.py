from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def get_post_data():
    if request.method == 'POST':
        # data should be jsdata
        data = request.get_json()
        #should be able to call main
        #data = main(jsdata)
        resp = jsonify(success=True)
        return resp

if __name__ == "__main__":
    app.run(host='0.0.0.0')

from flask import Flask, request, render_template
#import main


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('popup.html')

@app.route('/', methods = ['GET', 'POST'])
def get_post_data():
    if request.method == 'POST':
        # data should be jsdata
        data = request.form.get('URL')
        #should be able to call main 
        #data = main(jsdata)
        return render_template('popup.html', data=data)

if __name__ == '__main__':
   app.run(debug = True, port=5000)
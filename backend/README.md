<b>How the application works at the moment:</b>

flask-app.py is the executable; its main method will run and begin to listen on the localhost at port 5000. Once receiving a POST request, it will send the request's data (should be a string of the url) to the main method from main.py. It then expects the return from the main method to be a JSON object, which is then forwarded to the extension in the HTTP response.

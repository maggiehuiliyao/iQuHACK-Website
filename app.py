import random
from flask import Flask, render_template, request

app = Flask(__name__) # Creating our Flask Instance

@app.route('/', methods=['GET'])
def index():
    """ Displays the home page accessible at '/' """

    return render_template('homepage.html')

@app.route('/taskbar/', methods=['GET'])
def taskbar():
    return render_template('taskbar.html')

if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    url = f"http://127.0.0.1:{port}"
    app.run(use_reloader=False, debug=True, port=port)
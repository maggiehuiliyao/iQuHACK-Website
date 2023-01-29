import random

# import os
# import sys
# rootpath = os.path.join(os.getcwd())
# sys.path.append(rootpath)

from utils.Check_flights import check_flights
from flask import Flask, render_template, request

app = Flask(__name__) # Creating our Flask Instance

@app.route('/', methods=['GET'])
def index():
    """ Displays the home page accessible at '/' """

    return render_template('homepage.html')

@app.route('/taskbar/', methods=['GET'])
def taskbar():
    return render_template('taskbar.html')

@app.route('/result/', methods=['POST'])
def result():
    Origin = request.form['Origin']  
    Destination = request.form['Destination']
    Departure_date = request.form['Departure_date']
    Return_date = request.form['Return_date']
    Travel_time = request.form['Travel_time']
    Airlines = request.form['Airlines']
    Food_type = request.form['Food_type']
    Price_range = request.form['Price_range']

    df = check_flights(Origin,Destination,Departure_date,Return_date)
    df_lowest_price = list(df.flight_price_total)[0]

    return render_template(
            'taskbar.html',
            Origin=Origin,
            Destination=Destination,
            Departure_date=Departure_date,
            Return_date=Return_date,
            Travel_time=Travel_time,
            Airlines=Airlines,
            Food_type=Food_type,
            Price_range=Price_range,
            df_lowest_price=df_lowest_price
        )
    

if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    url = f"http://127.0.0.1:{port}"
    app.run(use_reloader=False, debug=True, port=port)
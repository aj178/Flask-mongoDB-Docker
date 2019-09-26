from flask import Flask, render_template, flash, request
from datetime import datetime
from pymongo import MongoClient
import socket
import os

app = Flask(__name__)
my_client = MongoClient(os.environ['DB_URL'], 27017)    # creating mongo client
my_db = my_client['oculyze']                    # creating mongodb database
my_col = my_db['names']                         # creating collection
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('firstname')    # get the http input
        apended_name = name + 'last_name'       # appending last_name to the input string
        client_data = {"firstname": name,
                       "apended_name": apended_name,
                       "timestamp": get_timestamp()
                       }
        my_col.insert(client_data)              # inserting data into database
    return render_template('home.html')


@app.route("/status", methods=['GET', 'POST'])
def status():
    results = list(my_db['names'].find())       # get the contents of the database and stores it in list format
    return render_template('status.html', rows=results)


if __name__ == "__main__":
    app.run(host=IPAddr, debug=True)

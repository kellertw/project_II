import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, create_engine
from Susp_activity import casino_crime
import json
from flask import Flask, jsonify, render_template, request
import requests

import decimal
import datetime


#################################################
# Database Setup
#################################################


# reflect an existing database into a new model

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# @app.route('/')
# def index():
#     # data = requests.get('http://127.0.0.1:5000/casino').json()['data']
#     # return render_template('index.html', data=data)
#     return render_template('index.html')


@app.route("/")
def casino():
    engine = create_engine("sqlite:///casino.sqlite")
    Base = automap_base()

    Base.prepare(engine, reflect=True)
    Keys = Base.classes.keys

    CasinoSW = Base.classes.casinoSW

    session = Session(engine)
    results = session.query(CasinoSW.id, CasinoSW.State, CasinoSW.SuspiciousActivity, CasinoSW.Industry,
                            CasinoSW.Long, CasinoSW.Year, CasinoSW.Countym, CasinoSW.Count, CasinoSW.Lat).all()

    def decoder(obj):
        if isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
    data = []
    for a, b, c, d, e, f, g, h, i in results:
        entry = {
            "id": a,
            "state": b,
            "industry": c,
            "long": d,
            "year": e,
            "countym": f,
            "count": g,
            "lat": h,
            "suspicious": i,
        }
    data.append(entry)

    final_results = {"data": data}
    print(final_results)
    return render_template('index.html', data=final_results)


if __name__ == '__main__':
    app.run(debug=True)
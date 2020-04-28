import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from Susp_activity import casino_crime
import json
from flask import Flask, jsonify

# For Heroku Deployment
from flask import (
    render_template,
    request,
    redirect
    ) 
from flask_sqlalchemy import SQLAlchemy

# Remove tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import decimal
import datetime
def decoder(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
      
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///casino.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Keys = Base.classes.keys

CasinoSW = Base.classes.casinoSW

session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def casino():
    # Create our session (link) from Python to the DB

    # Query all Casino DB
    results = session.query(CasinoSW.id, CasinoSW.State, CasinoSW.SuspiciousActivity, CasinoSW.Industry, CasinoSW.Long, CasinoSW.Year, CasinoSW.Countym, CasinoSW.Count, CasinoSW.Lat).limit(5).all()


    data = []
    for a, b, c, d, e, f, g, h, i in results:
        entry = {
            "id": a,
            "state": b,
            "industry": c,
            "long": decoder(d),
            "year": decoder(e),
            "countym": f,
            "count": g,
            "lat": decoder(h),
            "suspicious": decoder(i),
        }
        data.append(entry)

    final_results = {"data": data}
    return final_results

if __name__ == '__main__':
    app.run(debug=True)

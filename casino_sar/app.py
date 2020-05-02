from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# This is the sqlite:///... connection string that you used to connect to the casino db
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///casino.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class CasinoSW(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String)
    SuspiciousActivity = db.Column(db.Float)
    Industry = db.Column(db.String)
    Long = db.Column(db.String)
    Lat = db.Column(db.String)
    Year = db.Column(db.String)
    Countym = db.Column(db.String)
    Count = db.Column(db.String)


@app.route('/')
def index():
    results = CasinoSW.query.limit(5)
    return render_template('index.html', results=results)


@app.route('/data')
def data():
    data_list = []
    results = CasinoSW.query.all()
    for result in results:
        data_list.append({
            "year": result.Year,
            "state": result.State,
            "countym": result.Countym,
            "industry": result.Industry,
            "suspiciousActivity": result.SuspiciousActivity,
            "count": result.Count
        })
    return {"data": data_list}


if __name__ == '__main__':
    app.run(debug=True)

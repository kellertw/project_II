from flask import Flask, render_template, session, sessions, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# This is the sqlite:///... connection string that you used to connect to the casino db
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///casino.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class CasinoSW(db.Model):
    __tablename__ = 'casinoSW'
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

# @app.route('/activity/<State>')
# def activity(State):
#     casino.query.select

#     res = {}
#     locs = CasinoSW.query
#     for loc in locs:
#         result = jsonify({locs})
#     return result

# @app.route('/api/v1.0/SuspiciousActivity')
# def activities():
#     session=Session(engine)
#     suspiciousActivity= session.query(casinoSW.SuspiciousActivity,casinoSW.State, func.count(casinoSW.count)).\
#         groupby(casinoSW.SusdfpiciousActivity).order_by(casinoSW.State).desc().all()
#     session.close()
#     return jsonify(suspiciousActivity)

@app.route("/Mapping/<Lat>")
def locations(Lat):
    session = Session(engine)
    location = session.query(casinoSW.Lat, casinoSW.Long)
    session.close()
    return jsonify(location)


if __name__ == '__main__':
    app.run(debug=True)
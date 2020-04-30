from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# This is the sqlite:///... connection string that you used to connect to the casino db
app.config['SQLALCHEMY_DATABASE_URI'] = ("sqlite:///Casino.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DATA_FOLDER'] = "data/"

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
# @app.route('/uploads/<path:filename>')
# def download_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename, as_attachment=True)
@app.route("/data/<path:filename>")
def getData(filename):
    out=send_from_directory(app.config['DATA_FOLDER'],filename)
    return out


if __name__ == '__main__':
    app.run(debug=True)

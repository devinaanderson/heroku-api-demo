from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 
from secrets import return_uri


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = return_uri()
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email


@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/collections', methods=['POST', 'DELETE'])
# def collections():
#     email = None
#     if request.method == 'POST':
#         email = request.form['text']
#         reg = User(email)
#         db.session.add(reg)
#         db.session.commit()
#         return render_template('success.html')
#     if request.method == 'DELETE':
#         email = request.form['text']
#         reg = User(email)
#         db.session.delete(reg)
#         db.session.commit()
#         return render_template('success.html')
#     return render_template('home.html')

@app.route('/delete', methods=['POST'])
def collections():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        obj=User.query.filter_by(email=email).first()
        db.session.delete(obj)
        db.session.commit()
        return render_template('success.html')
    return render_template("home.html")

@app.route('/return_emails', methods=['GET'])
def return_emails():
    if request.method == 'DELETE':
        email = request.form['text']
        reg = User(email)
        db.session.delete(reg)
        db.session.commit()
        return render_template('success.html')
    all_emails = db.session.query(User.email).all()
    return jsonify(all_emails)

    

if __name__ == '__main__':
    app.debug = True
    app.run()    
	
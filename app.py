from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://vjkhdjrydbigxj:260c8f99adf9b38164f8f3a817e97d9a53456f70fac1bd5984206071f3546ce7@ec2-184-72-239-186.compute-1.amazonaws.com:5432/dcg65lv1r0cnn6"
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

@app.route('/collections', methods=['DELETE'])
def collections():
    email = None
    if request.method == 'DELETE':
        email = request.form['email']
        reg = User(email)
        db.session.delete(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template('home.html')

@app.route('/return_emails', methods=['GET'])
def return_emails():
    all_emails = db.session.query(User.email).all()
    return jsonify(all_emails)

if __name__ == '__main__':
    app.debug = True
    app.run()    
	
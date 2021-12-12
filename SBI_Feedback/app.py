from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from send_mail import sendemail

feedback_app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
   feedback_app.debug = True
   feedback_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:81850@localhost/sbi'
else:
    feedback_app.debug = False
    feedback_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://icrlrltmkglzkv:d8d5552742dd83baee851d9a705ff846fbfafc7f19102d4971a4812e2023dd72@ec2-18-233-104-114.compute-1.amazonaws.com:5432/d629tuhom1sjjo'

feedback_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(feedback_app)


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    representative = db.Column(db.String(200))
    rating = db.Column(db.String(100))
    comments = db.Column(db.Text())

    def __init__(self, customer, representative, rating, comments):
        self.customer = customer
        self.representative = representative
        self.rating = rating
        self.comments = comments

@feedback_app.route("/")
def home():
    return render_template("home.html")

@feedback_app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        representative = request.form['representative']
        rating = request.form['rating']
        comments = request.form['comments']
        if customer == '' or representative == '':
            return render_template('home.html', message='Please enter required fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, representative, rating, comments)
            db.session.add(data)
            db.session.commit()
            sendemail(customer, representative, rating, comments)
            return render_template('final.html')
        return render_template('home.html', message='You have already submitted feedback')



if __name__ == "__main__":
    feedback_app.run()

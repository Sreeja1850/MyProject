from flask import Flask , render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


myapp = Flask(__name__)
myapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(myapp)

class flaskDB(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100))
    status = db.Column(db.Boolean)
    

@myapp.route('/')
def home():
    incompleted_list = flaskDB.query.filter_by(status=False).all()
    completed_list = flaskDB.query.filter_by(status=True).all()
    return render_template('base.html', incompleted_list=incompleted_list, completed_list=completed_list)

@myapp.route('/add', methods=['POST'])
def add_item():
    activity_name = request.form.get('item')
    add_row = flaskDB(title=activity_name, status=False)
    db.session.add(add_row)
    db.session.commit()
    return redirect(url_for('home'))

@myapp.route("/complete/<int:todo_id>")
def complete(todo_id):
    complete_row = flaskDB.query.filter_by(id=todo_id).first()
    complete_row.status = True
    db.session.commit()
    return redirect(url_for('home'))

@myapp.route("/delete/<int:todo_id>")
def delete(todo_id):
    del_row = flaskDB.query.filter_by(id=todo_id).first()
    db.session.delete(del_row)
    db.session.commit()
    return redirect(url_for("home"))



if __name__ == '__main__':
    db.create_all()
    myapp.run(debug=True)

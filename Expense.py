from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flaskext.mysql import MySQL

mysql = MySQL()


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:''@localhost/alchemy'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payee = db.Column(db.String(100))
    cost = db.Column(db.Float)
    date = db.Column(db.Date)
    budgetCategory = db.Column(db.String(250))

    def __init__(self, payee, cost, date, budgetCategory):
        self.payee = payee
        self.cost = cost
        self.date = date
        self.budgetCategory = budgetCategory

@app.route('/', methods=['GET','POST'])
def add_expense():
    if request.method=='POST':
        payee = request.form['payee'] #text in quotes must be same in html
        cost = request.form['cost']
        date = request.form['date']
        budget_category = request.form['budget_category']

        connection = mysql.get_db()
        cursor = connection.cursor()
        query = "INSERT INTO expenses(payee, cost, date, budget_category) VALUES (%s, %s, %s)"
        cursor.execute(query, (payee, cost, date, budget_category))
        connection.commit()

# class RentalIncome(db.Model):
#     month = db.Column(db.String(20), nullable=False)
#     tenant_room = db.Column(db.Integer, db.ForeignKey('tenant.room_number'), nullable=False)
#     rent = db.Column(db.Float)

# with app.app_context():
#     db.create_all()

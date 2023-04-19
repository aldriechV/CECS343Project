from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


# create tenant class
class Tenant(db.Model):

    id = db.Column('tenant_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    room_number = db.Column(db.Integer(50))

    def __repr__(self):
        return f'Tenant: {self.description}'

    # Constructor
    def __init__(self, name, room_number):

        self.name = name
        self.room_number = room_number


# add tenant
@app.route('/tenant', methods = ['POST'])
def create_tenant():
    name = request.json['name']
    room_number = request.json['room_number']
    new_tenant = Tenant(name, room_number)  # use the constructor
    db.session.add(new_tenant)
    db.session.commit()

    return "New tenant has been added successfully."


# delete tenant
@app.route('/tenant<id>', methods = ['DELETE'])
def delete_tenant(id):
    tenant = Tenant.query.filter_by(id=id).one()
    db.session.delete(tenant)
    db.session.commit()

    return f'Tenant (id: {id}) has been removed successfully.'


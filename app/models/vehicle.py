from app import db

'''make clases declared here
to be available on make_shell_context in
Manager.py'''

class Vehicle(db.Model):
    __tablename__= 'vhc_vehicle'
    veh_id = db.Column(db.Integer, primary_key = True)
    veh_model = db.Column(db.String(64),unique =True)
    veh_type = db.Column(db.String(64))
    veh_version = db.Column(db.String(64))
    veh_manufacture_date_since = db.Column(db.Integer)
    veh_manufacture_date_until = db.Column(db.Integer)

    compatibilities = db.Table('vhc_compatibilities', db.Column('veh_id', db.Integer, db.ForeignKey('vhc_vehicle.veh_id')), db.Column('itm_id', db.Integer, db.ForeignKey('item.itm_id')))

    items = db.relationship('Item', secondary = compatibilities, backref = db.backref('vhc_vehicle', lazy = 'dynamic'),lazy='dynamic')

    def __repr__(self):
        return '<Vehicle %r>' %self.veh_model


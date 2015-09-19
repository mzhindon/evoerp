from app import db

'''Make clases declared here to
   be available on make_shell_context in
   Manager.py'''
class Category(db.Model):
    __tablename__ = 'inv_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    description = db.Column(db.String(128))

    items = db.relationship('Item',backref='category')

    def __repr__(self):
        return '<Categorie %r>' % self.name

class Item(db.Model):
    __tablename ='item'
    itm_id = db.Column(db.Integer, primary_key = True)
    itm_code = db.Column(db.String(64),unique = True)
    itm_customs_code = db.Column(db.String(64),unique = True)
    itm_quantity_on_hand = db.Column(db.Integer)
    itm_quantity_on_order = db.Column(db.Integer)
    itm_price = db.Column(db.Float)

    itm_category_id_fk = db.Column(db.Integer, db.ForeignKey('inv_categories.id'))
    itm_brand_id_fk = db.Column(db.Integer, db.ForeignKey('cmn_brands.bnd_id'))

    def __repr__(self):
        return '<Item %r>' % self.code

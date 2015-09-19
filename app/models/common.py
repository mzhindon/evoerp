from app import db

'''make classes declared here
to make available on make_shell_context in
Manager.py'''

class Brand(db.Model):
    __tablename__ = 'cmn_brands'
    bnd_id = db.Column(db.Integer,primary_key = True)
    bnd_name = db.Column(db.String(64), unique = True)

    def __repr__(self):
        return 'Brand %r' %self.bnd_name
    

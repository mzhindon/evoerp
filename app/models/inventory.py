from app import db

'''Make clases declared here to
   be available on make_shell_context in 
   Manager.py'''
class Category(db.Model):
    __tablename__ = 'inv_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique = True)
    description = db.Column(db.String(128))

    def __repr__(self):
        return '<Categorie %r>' % self.name

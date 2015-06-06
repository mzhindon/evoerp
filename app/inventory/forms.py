from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from app.models.inventory import Category

class ListCategoriesForm(Form):
    parametro = StringField('Buscar:')
    submitFind = SubmitField('Buscar')  

class EditCategoryForm(Form):
    name= StringField('Nombre:',validators=[Required()])
    description = StringField('Descripcion:')
    submitSave = SubmitField('Guardar')

    #def __init__(self,category,*args,**kwargs):
    #    self.category = category
 

    #def validate_name(self,field):
    #    if field.data != self.category.name  and Category.query.filter_by(name = field.name).first():
     #       raise ValidationError('Categoria ya registrada')
        

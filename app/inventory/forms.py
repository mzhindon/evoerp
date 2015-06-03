from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class ListCategoriesForm(Form):
    parametro = StringField('Buscar:',)
    submitFind = SubmitField('Buscar')
    submitNew = SubmitField('Nuevo')  

class EditCategoryForm(Form):
    name= StringField('Nombre:',validators=[Required()])
    description = StringField('Descripcion:')
    submitSave = SubmitField('Guardar')

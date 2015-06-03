from flask import render_template, session, redirect, url_for, flash
from . import inventory
from .forms import ListCategoriesForm, EditCategoryForm

@inventory.route('/list_categories',methods=['GET','POST'])
def list_categories():
    form = ListCategoriesForm()
    if form.validate_on_submit():
        form.parametro.data = ''
    return render_template('inventory/list_categories.html',form=form)

@inventory.route('/edit_category',methods=['GET','POST'])
def edit_category():
    form = EditCategoryForm()
    if form.validate_on_submit():
        form.name.data = ''
        form.description.data=''
        flash('Registro guardado exitosamente!') 
        return redirect(url_for('.edit_category'))
    return render_template('inventory/edit_category.html',form=form)

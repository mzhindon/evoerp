from flask import render_template, session, redirect, url_for, flash
from . import inventory
from .forms import ListCategoriesForm, EditCategoryForm
from .. import db
from app.models.inventory import Category

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
        '''verify if the category does not exist in db'''
        category = Category.query.filter_by(name = form.name.data).first()
        if category is None:
            category = Category(name = form.name.data, description = form.description.data)
            db.session.add(category)
            flash('Registro guardado exitosamente!') 
        else:
            flash('Registro ya existe!') 
        form.name.data = ''
        form.description.data='' 
        return redirect(url_for('.edit_category'))
    return render_template('inventory/edit_category.html',form=form)

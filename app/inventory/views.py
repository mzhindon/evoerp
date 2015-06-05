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
    categories = Category.query.all()
    return render_template('inventory/list_categories.html',form=form,categories=categories)

@inventory.route('/add_category',methods=['GET','POST'])
def add_category():
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
        return redirect(url_for('.add_category'))
    return render_template('inventory/edit_category.html',form=form)

@inventory.route('/edit_category/<int:id>',methods=['GET','POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    form = EditCategoryForm()
    if form.validate_on_submit(): 
        category.name = form.name.data, 
        category.description = form.description.data
        db.session.add(category)
        flash('Registro actualizado exitosamente!')  
        form.name.data = ''
        form.description.data='' 
        return redirect(url_for('.add_category'))
    form.name.data = category.name
    form.description.data = category.description
    return render_template('inventory/edit_category.html',form=form)

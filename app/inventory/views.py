from flask import render_template, session, redirect, url_for, flash, request, current_app
from . import inventory
from .forms import ListCategoriesForm, EditCategoryForm, SearchItemsForm, EditItemForm
from .. import db
from app.models.inventory import Category, Item

@inventory.route('/list_categories',methods=['GET','POST'])
def list_categories():
    form = ListCategoriesForm()
    page = request.args.get('page',1,type = int)
    if session.get('parametro') is None : 
        pagination = Category.query.paginate(page, per_page = current_app.config['EVOERP_CATEGORIES_PER_PAGE'], error_out = False)
        print('if 1') 
    else:
        pagination = Category.query.filter(Category.name.like('%'+session['parametro']+'%')).paginate(page,per_page=current_app.config['EVOERP_CATEGORIES_PER_PAGE'],error_out=False)
        del session['parametro']
        print('if 2')
    categories = pagination.items
    if form.validate_on_submit():
        print('if 3: form.parametro.data',form.parametro.data)
        if form.parametro.data != '':
            print('if 4')
            session['parametro'] = form.parametro.data
            form.parametro.data = ''
        print ('redirect') 
        return redirect(url_for('.list_categories'))
    return render_template('inventory/list_categories.html',form=form,categories = categories, pagination = pagination)

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
        return redirect(url_for('.list_categories'))
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
        return redirect(url_for('.list_categories'))
    form.name.data = category.name
    form.description.data = category.description
    return render_template('inventory/edit_category.html',form=form)

@inventory.route('/list_items',methods=['GET','POST'])
def list_items():
    form = SearchItemsForm()
    return render_template('inventory/list_items.html',form=form)

@inventory.route('/add_item',methods=['GET','POST'])
def add_item():
    form = EditItemForm()
    if form.validate_on_submit():
        '''verify if the item does not exist in db'''
        item = Item.query.filter_by(itm_code = form.code.data).first()
        if item is None:
            item = Item(itm_code = form.code.data, itm_customs_code = form.customs_code.data, itm_quantity_on_hand= form.quantity_on_hand.data, itm_quantity_on_order= form.quantity_on_order.data, itm_price= form.price.data )
            db.session.add(item)
            flash('Registro guardado exitosamente!') 
        else:
            flash('Registro ya existe!') 
        form.code.data = ''
        form.customs_code.data = ''
        form.quantity_on_hand.data = ''
        form.quantity_on_order.data = '' 
        form.price.data = ''
        return redirect(url_for('.items'))
    return render_template('inventory/edit_item.html',form=form)
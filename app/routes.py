from flask import (
	redirect,
	request,
	render_template,
	url_for
	)

from app import app, db
from app.forms import CreateEditForm
from app.models import Entity


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
	form = CreateEditForm()
	context = {'form': form}
	if form.validate_on_submit():
		name = form.name.data
		content = form.content.data
		entity = Entity(name=name, content=content)
		db.session.add(entity)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('create.html', context=context)


@app.route('/delete/<id>')
def delete(id):
	entity = Entity.query.get_or_404(id)
	db.session.delete(entity)
	db.session.commit()
	context = {
		'message': f'The Entity {id} has been deleted!'
		}
	return render_template('delete.html', context=context)


@app.route('/retrieve', methods=['GET'])
def retrieve():
	queryset = Entity.query.all()
	context = {'queryset': queryset}
	return render_template('retrieve.html', context=context)


@app.route('/search')
def search():
	name = request.args.get('search')
	queryset = Entity.query.filter_by(name=name)
	context = {'queryset': queryset}
	return render_template('retrieve.html', context=context)


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
	entity = Entity.query.get_or_404(id)
	form = CreateEditForm(obj=entity)
	context = {'form': form}
	if form.validate_on_submit():
		name = form.name.data
		content = form.content.data
		entity = Entity.query.get_or_404(id)
		entity.name = name
		entity.content = content
		db.session.commit()
		return redirect(url_for('retrieve'))
	return render_template('update.html', context=context)

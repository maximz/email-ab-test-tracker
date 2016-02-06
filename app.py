from flask import Flask, render_template, request, url_for, redirect
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.basicauth import BasicAuth
import os
import uuid

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)

from models import *



@app.route('/')
def index():
	Record
	return "Tracker."

@app.route('/mark/<uid>')
def mark(uid):
	record = Record.query.get(slug2uuid(uid))
	record.marked = True
	db.session.commit()
	return 'Response recorded'

@app.route('/admin')
@basic_auth.required
def summary():
	exps = db.session.query(Record.experiment_name, db.func.count(Record.experiment_name).label("count")).group_by(Record.experiment_name).all()
	return render_template('status.html', exps=exps)

@app.route('/admin/create')
@basic_auth.required
def create():
	return render_template('create.html')

@app.route('/admin/submit', methods=['POST'])
@basic_auth.required
def make_new_experiment():
	name = request.form['name']
	users = [u.strip() for u in request.form['users'].split('\n')]
	for u in users:
		rec = Record(name,u)
		db.session.add(rec)
	db.session.commit()
	print '%s: Added %d users' % (name, len(users))
	return redirect(url_for('report', name=name))

@app.route('/admin/report/<name>')
@basic_auth.required
def report(name):
	records = Record.query.filter_by(experiment_name=name).order_by(Record.marked).all()
	return render_template('report.html', exp_name=name, records=records)

@app.route('/admin/csv/<name>')
@basic_auth.required
def csv(name):
	records = Record.query.filter_by(experiment_name=name).order_by(Record.marked).all()
	return '<br/>'.join([r.csv() for r in records])



@app.route('/status')
def status():
	return 'OK'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=app.config['PORT'])


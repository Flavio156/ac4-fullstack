from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/example', methods=['GET'])
def get_example():
    examples = Example.query.all()
    return {'examples': [{'id': example.id, 'name': example.name} for example in examples]}

@app.route('/example', methods=['POST'])
def post_example():
    name = request.json['name']
    example = Example(name=name)
    db.session.add(example)
    db.session.commit()
    return {'id': example.id}
#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Gift

from models import db # import your models here!

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Hello world"

@app.get('/gifts')
def get_gifts():
    all_gifts = Gift.query.all()
    return make_response(jsonify([gift.to_dict() for gift in all_gifts]), 200)

@app.get('/gifts/<int:id>')
def get_gift_id(id):
    gift = Gift.query.filter(Gift.id==id).first()
    if not gift:
        return make_response(jsonify({"error": f"There is no user with this {id}"}), 404)
    return make_response(jsonify(gift.to_dict()), 200)

@app.post('/gifts')
def post_gift():
    new_data=request.json
    print(new_data)
    try:
        gift=Gift(name=new_data['name'], price=new_data['price'])
        db.session.add(gift)
        db.session.commit()
        return make_response(jsonify(gift.to_dict()),201)
    except Exception as e:
        return make_response(jsonify({'error': f'Server threw error {e}'}), 406)

@app.delete('/gifts/<int:id>')
def delete_gift(id):
    try: 
        found_gift=db.session.get(Gift,id)
        db.session.delete(found_gift)
        db.session.commit()
    except Exception as e:
        return make_response(jsonify({'error': f'Server threw error {e}'}), 406)
# write your routes here!

if __name__ == '__main__':
    app.run(port=5555, debug=True)

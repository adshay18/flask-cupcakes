"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from itsdangerous import json

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "baked"

connect_db(app)

@app.route('/api/cupcakes')
def list_cupcakes():
    '''Get info about all cupcakes in JSON'''
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    '''Returns JSON by single cupcake id'''
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
    '''Creates a new cupcake and returns JSON of the new snack'''
    cupcake = Cupcake(flavor=request.json["flavor"], size=request.json["size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(cupcake)
    db.session.commit()
    response = jsonify(cupcake=cupcake.serialize())
    return (response, 201)
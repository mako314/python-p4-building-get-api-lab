#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import asc, desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        bakery_dict = bakery.to_dict()
        bakeries.append(bakery_dict)
        # bakery_dict = {
        #     "name" : bakery.name,
        #     "bakery_id" : bakery.id,
        #     "created_at" : bakery.created_at,
        #     "updated_at": bakery.updated_at,
        # }
        # bakeries.append(bakery_dict)

    response = make_response(
        bakeries,
        200
    )
    # print(bakeries)

    # bakeries = Bakery.query.all()
    # all_bakeries = bakeries.to_dict()
    # response = make_response(
    #     all_bakeries,
    #     200
    # )

    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter(Bakery.id == id).first()

    bakery_dict = bakery.to_dict()
    response = make_response(
        bakery_dict,
        200
    )
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods_descending = BakedGood.query.order_by(asc(BakedGood.price)).all()

    #its a list can't to_dict rip
    # baked_price_dict = baked_goods_descending.to_dict()
    #so break it up dummy

    baked_goods = []
    for baked_good in baked_goods_descending:
        baked_good_dict = baked_good.to_dict()
        baked_goods.append(baked_good_dict)

        # baked_good_dict = {
        #     "created_at" : baked_good.created_at,
        #     "baked_good_id" : baked_good.id,
        #     "name" : baked_good.name,
        #     "updated_at": baked_good.updated_at,
        #     "bakery_id": baked_good.bakery_id,
        #     "price" : baked_good.price
        # }
        # baked_goods.append(baked_good_dict)

    response = make_response(
        baked_goods,
        200
    )
    #I tried to also just pass the baked_goods list 
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_goods_expensive = BakedGood.query.order_by(desc(BakedGood.price)).limit(1).first()
    baked_good_dict = baked_goods_expensive.to_dict()
    
    # baked_goods = []
    # for baked_good in baked_goods_expensive:
        # baked_goods.append(baked_good_dict)

        # baked_good_dict = {
        #     "created_at" : baked_good.created_at,
        #     "baked_good_id" : baked_good.id,
        #     "name" : baked_good.name,
        #     "updated_at": baked_good.updated_at,
        #     "bakery_id": baked_good.bakery_id,
        #     "price" : baked_good.price
        # }
        # baked_goods.append(baked_good_dict)

    response = make_response(
        baked_good_dict,
        200
    )
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)

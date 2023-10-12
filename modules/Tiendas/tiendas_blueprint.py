import json
from flask import Blueprint, jsonify, request
from modules.Tiendas.Tienda import Tienda

from modules.Tiendas.Tiendas_servce import tiendas_service



tiendas_blueprint = Blueprint("tiendas_blueprint", __name__)

service = tiendas_service

@tiendas_blueprint.route('/tiendas/all')
def datos_tiendas_all_products():
    
    tiendas = tiendas_service.create_tiendas()
    
    res = tiendas._get_all_data_products()
    
    with open("data/datos_diarios.json", "w") as doc:
        json.dump(res, doc)
    
    return jsonify(res)

@tiendas_blueprint.route('/tiendas/product/<id>')
def datos_tiendas_id_product(id):
    
    tiendas = tiendas_service.create_tiendas()
    
    return jsonify(tiendas._get_id_data_products(int(id)))

@tiendas_blueprint.route('/tiendas/product', methods=["POST"])
def datos_tiendas_multiple_products():
    
    if request.method == "POST":
        req = request.get_json()
        
        res = []
        
        tiendas = tiendas_service.create_tiendas()
        
        for id in req["lista_id"]:
            res.append(tiendas._get_id_data_products(int(id)))
        
        return jsonify(res)
    
@tiendas_blueprint.route("/tiendas", methods=["GET"])
def get_tiendas():
    
    tienda = Tienda()
    
    return jsonify({"tiendas": tienda.Tiendas})
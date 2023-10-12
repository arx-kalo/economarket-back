from flask import Blueprint, jsonify

from modules.Products.Products import Products

product_blueprint = Blueprint("product_blueprint", __name__)

@product_blueprint.route("/product/categories", methods=["GET"])
def categories():
    
    prod = Products()
    
    try:
        return jsonify(
            { 
             "categories": list(set(prod.Base["Categoria"]))
            }
        )
    except Exception as e:
        
        return {
            "Error": e.__str__( )
        }

@product_blueprint.route("/products", methods=["GET"])
def products():
    prod = Products()
    
    try:
        return jsonify(
            { 
             "Products": prod._get_list_products()
            }
        )
    except Exception as e:
        
        return {
            "Error": e.__str__( )
        }
@product_blueprint.route("/products/scrap", methods=["GET"])
def get_products():
    prod = Products()
    
    try:
        return jsonify(prod._get_list_scrap_products())
    except Exception as e:
        
        return {
            "Error": e.__str__( )
        }
    


from modules.Products.products_blueprint import product_blueprint
from modules.Tiendas.tiendas_blueprint import tiendas_blueprint
from start_app import star_app

app = star_app()

app.register_blueprint(product_blueprint)
app.register_blueprint(tiendas_blueprint)

@app.route("/",methods=["GET"])
def index():
    
    return """<h1>!!YOU HAVE BEEN HACKED RIGHT NOW!!</h1>"""

if __name__ == "__main__":
    
    app.run("0.0.0.0", 5500, True)
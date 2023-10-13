
from modules.Products.Products import Products



class Tienda:
    
    __id : int
    __Price: float
    __img: str
    __tiendas: list = ["Olimpica", "Jumbo", "Exito", "Carulla" ]

    
    def __init__(self) -> None:
        
        self.__objects = {
            "Olimpica": None,
            "Jumbo": None,
            "Carulla": None,
            "Exito": None,
        }
    
    @property
    def Tiendas(self):
        return self.__tiendas
    
    def __call__(self) -> dict:
        
        return {
            "id": self.__id,
            "price": self.__Price,
            "img": self.__img
        }
    
    def _add_childrens(self, childs: list) -> None:
        
        for child in childs:
            self.__objects[child["type"]] = child["Object"]
        
    def _get_scrap_product(self): pass
    
    def _get_all_data_products(self) -> list:
        p = Products()
        _actual = []
        
        for product in p.Products:
            
            if str(product["Descripción"]) != "NaN":
                temp = {
                    "id": product["id"],
                    "Descripcion": product["Descripción"],
                    "Categoria": product['Categoria'],
                    'Sub Categoria': product['Sub Categoria'],
                    "unidades": product['unidades'],
                    "disponibilidad":[]
                }
                
                for t in self.__tiendas:
                    
                    try:
                        if product[f"Link {t}"] != None and "https" in product[f"Link {t}"] :
                            tienda = self.__objects[t]
                                                                        
                            data = tienda._get_scrap_product(product[f"Link {t}"])
                            if t == "Jumbo":
                                temp[f"{t}"] = data
                                temp[f"{t}"]["url"] = product[f"Link {t}"]
                                if data.__len__() > 0:
                                    temp["disponibilidad"].append(t)
                            else:
                                if "offers" in  data:
                                    temp[f"{t}"] = {
                                        "price": data["offers"]["lowPrice"],
                                        "img": data["image"] 
                                    }
                                    temp["disponibilidad"].append(t)
                                else:
                                    temp[f"{t}"] ={}
                            
                        else:
                            temp[f"{t}"] = {}
                    except:
                        product[f"{t}"] = {}
                _actual.append(temp)
        
        return _actual
    def _get_id_data_products(self, id:int) -> dict:
        p = Products()
        product = p.Products[id - 1]
        temp = {
                "id": product["id"],
                "Descripcion": product["Descripción"],
                "Categoria": product['Categoria'],
                'Sub Categoria': product['Sub Categoria'],
                "unidades": product['unidades'],
                "disponibilidad":[]
            }
        for t in self.__tiendas:
            
            try: 
                if product[f"Link {t}"] != None and "https" in product[f"Link {t}"]:
                    tienda = self.__objects[t]
                                                                
                    data = tienda._get_scrap_product(product[f"Link {t}"])
                    if t == "Jumbo":
                        temp[f"{t}"] = data
                        temp[f"{t}"]["url"] = product[f"Link {t}"]
                        
                        if data.__len__() > 0:
                            temp["disponibilidad"].append(t)
                    else:
                        if "offers" in  data:
                            temp[f"{t}"] = {
                                "price": data["offers"]["lowPrice"],
                                "img": data["image"],
                                "url": product[f"Link {t}"]
                            }
                            temp["disponibilidad"].append(t) 
                        else:
                            temp[f"{t}"] ={}
                else:
                    temp[f"{t}"] = {}
            except:
                temp[f"{t}"] = {}
        return temp
        
        
                
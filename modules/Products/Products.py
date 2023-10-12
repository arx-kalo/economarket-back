import json
import pandas as pd
import re


class Products:
    
    __base: pd.DataFrame
    __products: list
    def __init__(self) -> None:
        
        self.__base = pd.read_excel("Data/100 productos EM.xlsx")
        self.__descripciones = self._get_descripcion_and_unidades()
        self.__products = self._get_list_products()
        
    @property
    def Base(self) -> dict:
        
        return self.__base.to_dict(orient="list")
    @property
    def Products(self) -> list:
        
        return self.__products
    
    def _get_descripcion_and_unidades(self) -> list[dict]:
    
        pattern = r'(^.*?)(\d+(\.\d+)?)( [^\d]+)?$'
        resp = []

        for s in self.__base["Descripción"].to_list():
            match = re.search(pattern, str(s))
            if match:
                original = match.group(1).strip()
                numero = match.group(2)
                complemento = match.group(4).strip() if match.group(4) else ''
            else:
                original = s
                numero = ""
                complemento = ""
            
            resp.append({
                    "Descripcion": original,
                    "unidades": numero+" "+complemento
            })
        
        return resp
    def _get_list_products(self) -> list:
        
        products = []
        for x in range(len(self.__base)):
            
            if(str(self.__base["Descripción"][x]) != "nan"):
                _p = {
                    "id": int(self.__base["Productos"][x]),
                    "Descripción": self.__descripciones[x]["Descripcion"],
                    "unidades": self.__descripciones[x]["unidades"],
                    "Categoria": self.__base["Categoria"][x],
                    "Sub Categoria": self.__base["Sub categoría"][x],
                    "Link Carulla": self.__base["Link Carulla"][x] if self.__base["Link Carulla"][x] != "N.A" else None,
                    "Link Exito": self.__base["Link Éxito"][x] if self.__base["Link Éxito"][x] != "N.A" else None,
                    "Link Jumbo": self.__base["Link Jumbo"][x] if self.__base["Link Jumbo"][x] != "N.A" else None,
                    "Link Olimpica": self.__base["Link Olimpica"][x] if self.__base["Link Olimpica"][x] != "N.A" else None,
                }
                
                products.append(_p)
            
        return products
    
    def _get_list_scrap_products(self) -> list:
        
        with open("data/datos_diarios.json", "r") as data:
            
            datos = json.load(data)
        
        return datos
            
            
         
    
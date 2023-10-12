from abc import ABC, abstractmethod
from modules.Tiendas.Carulla import Carulla
from modules.Tiendas.Exito import Exito
from modules.Tiendas.Jumbo import Jumbo
from modules.Tiendas.Olimpica import Olimpica

from modules.Tiendas.Tienda import Tienda


class tiendas_service(ABC):
    
   @abstractmethod
   def create_tiendas() -> Tienda:
        tiendas = Tienda()  
    
        list_objects = [{
            "type": "Olimpica",
            "Object": Olimpica()
        },{
            "type": "Carulla",
            "Object": Carulla()
        },{
            "type": "Jumbo",
            "Object": Jumbo()
        },{
            "type": "Exito",
            "Object": Exito()
        }]
        
        tiendas._add_childrens(list_objects) 
        
        return tiendas

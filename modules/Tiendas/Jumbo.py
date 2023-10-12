import bs4
import requests
from .Tienda import Tienda


class Jumbo(Tienda):
    
    def __init__(self) -> None:
        super().__init__()
    
    def _get_scrap_product(self, link: str):
        
        r = requests.get(link)
        
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, "html.parser")
            interes = soup.find_all('div', 'tiendasjumboqaio-jumbo-minicart-2-x-price')
            data = {}
            
            try:
                data["price"] = float(interes[0].text[2:].replace(".",""))
            except:
                data["price"] = interes
            return data
        
        return {}
            
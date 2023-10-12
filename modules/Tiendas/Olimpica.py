
from .Tienda import Tienda
import requests
import bs4
import json


class Olimpica(Tienda):
    
    def __init__(self) -> None:
        super().__init__()
    
    def _get_scrap_product(self, link: str):
        r = requests.get(link)
        
        if r.status_code == 200:
            soup = bs4.BeautifulSoup(r.text, "html.parser")
            interes = soup.find_all('script', type='application/ld+json')
            
            try:
                interes = json.loads(interes[0].text)
            except:
                print("------>", interes)
                interes = {}
            
            return interes
        
        else:
            return {} 
import requests
from bs4 import BeautifulSoup
import html_to_json

def chek_link(link):
    try:
        req = requests.get(str(link)).content.decode("utf-8")
        bs = BeautifulSoup(req, "html.parser")
        site = bs.find_all("ul", class_="params-paramsList-2PiKQ")
        ch = html_to_json.convert(str(site))

        if "4+" in str(ch) or "Битый" in str(ch) or "Снято " in str(ch) or "Выше рыночной" in str(ch):
            return False

        else:
            return True

    except:
        print("Нет соединения")

        
        


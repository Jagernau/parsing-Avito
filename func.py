import re
import requests
from bs4 import BeautifulSoup
import html_to_json
from chek import chek_link

def get_info(nums_pages):

    url = f"https://www.avito.ru/nizhniy_novgorod?q=lada&p={nums_pages}"
    try:
        requests.get(url)
        
    except:
        print("Ошибка соединения")
        
    else:
        req = requests.get(url)
        bs = BeautifulSoup(req.content.decode("utf-8"), "html.parser")
        content = bs.find_all("div", class_= "iva-item-content-rejJg")
        w = ["Битый", "Салон", "салон", "Автодилер", "Акция", "акция", "битая"]
        g = ["Месяцев", "Лет", "неделя", "год", "дней", "месяца", "недели", "месяцев", "недель"]

        text = "i"

        for i in content:
            bs_cont = BeautifulSoup(str(i), "html.parser")
            st = str(i)

            if w[1] in st or w[2] in st or w[3] in st or w[4] in st or w[5] in st or w[6] in st or "битый" in st or "дней" in st or " дней<" in st or "месяц" in st or "запрет" in st or "+4" in st or "еще походит" in st or "Поменять" in st or "гнилые" in st or "4+" in st or "+4" in st or "1998" in st or "Арест" in st or "арест" in st:
                continue

            st2 = str(html_to_json.convert(st))
            if w[1] in st2 or w[2] in st2 or w[3] in st2 or w[4] in st2 or w[5] in st2 or w[6] in st2 or "битый" in st2 or "дней" in st2 or " дней<" in st2 or "месяц" in st2 or "запрет" in st2 or "+4" in st2 or "еще походит" in st2 or "Поменять" in st2 or "гнилые" in st2 or "4+" in st2 or "+4" in st2 or "1998" in st2 or "Арест" in st2 or "арест" in st2:

                continue
 

            strin = str(bs_cont.find_all("div", class_="date-text-KmWDf")[0])

            if g[1] in strin or g[2] in strin or g[3] in strin or g[4] in strin or g[6] in strin or g[6] in strin or g[7] in strin or g[8] in strin or " дней" in strin or " дней<" in strin or " дней " in strin or "дней" in strin or "неделю" in strin or "Дней" in strin:
                continue

            num = re.findall(r'\d+', strin)
            if int(num[1]):
                if int(num[1]) > 4:
                    continue


            
            json_content = html_to_json.convert(str(i))
            if "дней" in str(json_content) or "копия" in str(json_content) or "4 собственника" in str(json_content) or "Копия" in str(json_content):
                continue
            if "недель" in str(json_content) or "неделю" in str(json_content):
                continue
            data = json_content["div"][0]["div"]

            price = data[1]["div"][2]["span"][0]["span"][0]["meta"][1]["_attributes"]["content"]
            if price.isdigit():
                if int(price) > 130000:
                    continue
                if int(price) < 70000:
                    continue

            href = data[0]["a"][0]["_attributes"]["href"]
            
            title = data[0]["a"][0]["_attributes"]["title"]


            
            if chek_link(f"https://www.avito.ru{href}") == False:
                continue

            text += f"\nСсылка:  https://www.avito.ru{href}  Описание:  {title},\n"

        return text




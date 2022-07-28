import requests

def resp():
    respr = requests.get("https://www.avito.ru/nizhniy_novgorod?q=lada&p=1").status_code
    return str(respr)



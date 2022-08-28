import requests

url = "http://v.juhe.cn/toutiao/index"

P = {
    "key":"c573a28a528c0d07399a71461096dddb",
    "type":"tiyu"
}


reponse = requests.get(url=url,params=P)
print(reponse.text)
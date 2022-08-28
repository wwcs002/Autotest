

import requests

url = "http://192.168.247.129/prod-api/system/user/importData?updateSupport=0"

header = {
    "Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjAzODMwNGNlLWVlYzctNDFhNC05MzlmLWU3NTNmOGVhMTQ3ZSJ9.a5qVDoVOjP6E8g3nimPQXna-MD9xZ2zKYdqYw4BcJ2-mEEOliR64gSTsbs3dtK-coCn4b7OQbPGnC6g_OPGcVA",
    "Cookie":"username=admin; password=l1QVVG5fnWgaTzHmIAGuhZm5nHL8B25E/ToEgRC2ATSDaW1lx3s5v29S1xDOeEuHDqZQIaidstJ2V6DyW4CbWw==; rememberMe=true; Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjAzODMwNGNlLWVlYzctNDFhNC05MzlmLWU3NTNmOGVhMTQ3ZSJ9.a5qVDoVOjP6E8g3nimPQXna-MD9xZ2zKYdqYw4BcJ2-mEEOliR64gSTsbs3dtK-coCn4b7OQbPGnC6g_OPGcVA; sidebarStatus=0",
    "Content-Type":"multipart/form-data; boundary=----WebKitFormBoundarywC9yl124F92HA9FZ"

}

f = open(file="C:/Users/mac/Desktop/工作簿1.xlsx",mode="rb")



fil = {
    "file":f
}
print(f)


res = requests.post(url=url,data=fil,headers=header,timeout=0.0000001)

print(res.json())



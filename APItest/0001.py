
import  requests


h =  {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Dicloud-Header-Csrf-Token": "eVVre4h-BbWTb82mrCq9bIxbKc4:1661527159997",
        "Cookie":"u_name=186*****374; feq=1; Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1661437752,1661523312,1661524617,1661527151; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661527151; q=z3GKGRFj1leNBmnyyd1DlYyiowHLE1ktFNVofmNAWVEkzDkOwkAMQNG7_NqK7HFmc0vPHVjC0gwSiCrK3RFwgbcylMAnnRRhGGHCSIR3tSwMJ1QYM2GlJHPruQsjE-z2CAcChCPR6uyetOTeUk-qwpnwrMJCrLwe7-dpIfImXH6a5VTtq10JrBX1VpvXGeH2V--Ebp8AAAD__w=="
    }


url = "https://api.didiyun.com/dicloud/wallet/v4/checkPrice"

d = {"goods":{"orderScene":"scene_create","couponId":"CHECKCOUPON","autoContinue":False,"offerings":[{"regionId":"gz","zoneId":"gz02","cnt":1,"product":"dc2","offeringUuid":"b9bb78ab2ec6408f8dcc73dc2b5dd54d","elements":[{"cnt":1,"product":"ebs","offeringUuid":"d10c319c66c10b780b9d299488ad45ed","factorValues":{"ebs.size":40},"customDetail":{"ebs.name":"EBS_HE_01","ebs.type":"Root"},"regionId":"gz","zoneId":"gz02","payType":"prePaid"}],"payType":"prePaid"}]}}


r = requests.post(url=url,json=d,headers=h)
print(r.json())
print("******************************")

r= r.json()


d1 = r["data"]# 获取到data
print(d1)

print("************************************")

print(d1["priceInfo"])
dict2 = d1["priceInfo"]


print("***************************************")
#dict = d1[0]

list = dict2["resultPrices"]
print(list)
print("***************************************")
dict3 = list[0]
print(dict3)
print("***************************************")
print(dict3["price"])

aaa = r["data"]["priceInfo"]["resultPrices"][0]["price"]

print(aaa)





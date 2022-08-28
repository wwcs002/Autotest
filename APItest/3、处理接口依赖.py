import requests
import time

baseUrl = "https://api.didiyun.com"
list = "/dicloud/i/compute/dc2/list"

start = "/dicloud/i/compute/dc2/start"
stop = "/dicloud/i/compute/dc2/stop"




if __name__ == '__main__':
    header ={
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660666673,1660919456,1661011426,1661437752; feq=1; u_name=186*****374; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661437762; q=Ei-BwJ9A2dKEVj5Gg1M6_tO1pl2jXY6yHmtyVp_5_pEkzDkOwkAMQNG7_NqKPPZscUvPHVjC0gwSiCrK3RFwgbcylMAnnRRhJCIJwwifNRVhOKHCyESq1TRbrSaMQrDbIxwIEI5Eb9ndtJa522yqwplw68JCrLwe7-dpIcomXH5ayt76V7sSpF7Ve-veMsLtr94J3T4BAAD__w==",
        "Dicloud-Header-Csrf-Token": "Z2NP4SQnN9G1DFsG9Mt4hJrKOaw:1661437863084"
    }

    j1 = {"start":0,"limit":10,"simplify":False,"condition":{}}

    res1 = requests.post(url=baseUrl+list,json=j1,headers=header)
    print("第一个请求的请求参数为：",res1.text)
    print("***************************************************")


    res1_json = res1.json()
    # data_list = res1_json["data"]
    # dc2 = data_list[0]
    # print(dc2)
    # UUid = dc2["dc2Uuid"]
    # print(UUid)
    UUid = res1_json["data"][0]["dc2Uuid"]#data[0].dc2Uuid
    print(UUid)


    #data[0].dc2Uuid


    j2 = {"dc2":[{"dc2Uuid":UUid}]}

    res2 = requests.post(url=baseUrl+stop,json=j2,headers=header)
    print("这是第二个接口的响应数据",res2.json())

    print("***************************************************")

    time.sleep(20)
    print("睡眠结束 一共睡10秒")

    j3 = {"dc2": [{"dc2Uuid": UUid}]}

    res3 = requests.post(url=baseUrl+start,json=j3,headers=header)
    print("这是第三个接口的响应数据",res3.json())






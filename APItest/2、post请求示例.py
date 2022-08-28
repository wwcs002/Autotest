import requests


baseUrl = "https://api.didiyun.com/"

url = "dicloud/i/compute/dc2/list"

head = {
    "Accept":"application/json, text/plain, */*",
    "Content-Type":"application/json;charset=UTF-8",
    "Cookie":"Hm_lvt_9eaa41ddde51c419f3c8953af0161d25=1660666673,1660919456,1661011426,1661437752; feq=1; u_name=186*****374; Hm_lpvt_9eaa41ddde51c419f3c8953af0161d25=1661437762; q=Ei-BwJ9A2dKEVj5Gg1M6_tO1pl2jXY6yHmtyVp_5_pEkzDkOwkAMQNG7_NqKPPZscUvPHVjC0gwSiCrK3RFwgbcylMAnnRRhJCIJwwifNRVhOKHCyESq1TRbrSaMQrDbIxwIEI5Eb9ndtJa522yqwplw68JCrLwe7-dpIcomXH5ayt76V7sSpF7Ve-veMsLtr94J3T4BAAD__w==",
    "Dicloud-Header-Csrf-Token":"Z2NP4SQnN9G1DFsG9Mt4hJrKOaw:1661437863084"
}

data_request = {"start":0,"limit":10,"simplify":False,"condition":{}}

res = requests.post(url=baseUrl+url,json=data_request,headers=head)
print(res.status_code)#响应状态码
p = res.raw.read()#返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
print(res.content)#字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
print(res.headers)#以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
res.raise_for_status() #失败请求(非200响应)抛出异常
print(p)
print("text文本形式查看相应数据",res.text)
print("json文本形式查看相应数据",res.json())
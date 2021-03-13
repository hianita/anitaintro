# 把網址中的所有資料讀取下來，有網路連線的情況下就能抓取
# 利用json模組處理json格式的資料
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response)  
    
# 將指定資料列表出來，要找到景點名稱,經度,緯度,第一張照片網址
clist=data["result"]["results"]
with open("data.txt", "w",encoding="utf-8") as file:
    for info in clist:
        file.write(info["stitle"]+",") 
        file.write(info["longitude"]+",") 
        file.write(info["latitude"]+",") 
        url=info["file"]  # 先讀取
        spl=url.split("http:") #把網址中有http:的部分當成分隔，所以網址的http:都不見了
        urltop=spl[1] # 找到清單的第一個網址，再把http:加進來
        url_1="http:"+urltop+"\n" #得出第一個網址
        file.write(url_1)   # 再寫入



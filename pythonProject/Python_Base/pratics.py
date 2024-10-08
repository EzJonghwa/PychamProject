import requests
url ="http://127.0.0.1:8080/api/addCode"
# post 미리 보낼 데이터
data ={
    "commCd" : "AA01"
    ,"commNm" : "Tsest"
    ,"commOrd" : 1
}
#  요청 헤더 JSON
headers = {"Content-Type" : "application/json"}
res = requests.post(url, json=data, headers=headers)
print(f"status code:{res.status_code}")
res.encoding ="utf-8"
print(f"body:{res.text}")
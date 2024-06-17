import requests

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text+"\n")
# 發送GET請求，一般用來獲取資源操作

x = requests.delete('https://w3schools.com/python/demopage.php')
print(x.text+"\n")
# 發送DELETE請求，一般用來刪除資源操作

x = requests.get('https://w3schools.com')
print(x.status_code+"\n")
# 200表示正常運行網頁的理想狀態代碼，訪客、機器人、連結權重連結到其它網頁。

x = requests.head('https://www.w3schools.com/python/demopage.php')
print(x.headers+"\n")
# 發送HEAD請求，一般用來獲取head資源操作

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}
x = requests.post(url, json = myobj)
print(x.text)
# 發送POST請求，一般用來創建資源操作
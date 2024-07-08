# Pegatron_Intern

# W2-1_FastAPI

## 1.HTTP verbs (HTTP 協定的五種服務請求方法)

HTTP Method: GET、POST、PUT、PATCH 和 DELETE。

- CRUD：
  網頁對 Server 發出的 Request，通常包含 4 個不同的動作 - create 新增 - read 讀取 - update 更新 - delete 刪除

| POST                 | GET                              | PUT                                | PATCH                                          | DELETE               |
| -------------------- | -------------------------------- | ---------------------------------- | ---------------------------------------------- | -------------------- |
| 新增一筆資料(Create) | 讀取想要的服務的資料或狀態(Read) | 修改**一整項**已存在的資料(Update) | 現有資料欄位中，修改**部分**資料或更新(Update) | 刪除指定資料(Delete) |
|                      | safe & idempotent                | idempotent                         |                                                | idempotent           |

- 「safe」是指該操作不會改變原本的資源狀態，並且同樣的結果是可以被快取（Cache）的。
  例如：查看訂單是不會改變訂單本身紀錄。
- 「idempotent」是指該操作不管做 1 遍、2 遍或多遍，都會得到同樣的資源狀態結果。
  例如：同一筆資料被 DELETE 了 2 次，雖然都是一樣的結果，但第二次發送會因為資料已經被刪除而失敗喔！

連結參考：[RESTful API](https://progressbar.tw/posts/53#:~:text=POST%EF%BC%8FPUT%C2%A0%E9%83%BD%E5%8F%AF%E4%BB%A5,%E5%9C%A8%E5%93%AA%E8%A3%A1%E5%91%A2%3F)

## 2.RESTful API

如果 Web API 符合上述的 Rest 架構來建立，就可以將它稱作 Restful API
(Rest 化 ＝ Restful)

---

- 如果我們在寫一隻商品的 WebAPI，讓工程師隨便寫可能會有以下方式來作 interface：

  1. 獲得商品資料 GET /getAllItems
  2. 獲得商品資料 GET /getItem/11
  3. 新增商品資料 POST /createItem
  4. 更新商品資料 POST /updateItem/
  5. 刪除商品資料 POST /deleteItem/

- 若是以使用 RESTful API 開發的話:

  1. 獲取商品資料 /GET /items
  2. 獲取商品資料 /GET /items/1
  3. 新增商品資料 /POST /items
  4. 更新商品資料 /PATCH /items/1
  5. 刪除商品資料 /DELETE /items/1

## 3.HTTP 狀態碼 (Status Code)

### 常見的狀態碼類別：

- 1xx 參考資訊（Informational）
- 2xx 成功（Successful）
- 3xx 重新導向（Redirection）
- 4xx 用戶端錯誤（Client Error）
- 5xx 伺服器錯誤（Server Error）

### 常見的狀態碼及其代表的意義

- http code 200 = OK
- http code 301 = 永久重定向
- http code 302 = 暫時性的替代頁面
- http code 404 = 找不到網頁
- http code 410 = 過時網頁
- http code 500 = 內部伺服器錯誤
- http code 503 = 暫時無法使用

## 4.FastAPI

### 如何執行網站伺服器？

- VS Code 終端機輸入 `uvicorn 檔名:app --reload`
- `app`變數：表示將 Fast API 儲存在 app 這個變數中
- ` --reload`：設定當更新檔案時，自動載入已經更新的東西
- 解釋：透過 uvicorn 這個 ASGI server(uvicorn 是前後端的 web server)，告訴它我們的 Fast API 在哪裡，將後端程式 run 起來

### 打開瀏覽器

- 進入終端機顯示的網址

### 如何暫停伺服器連接？

- 輸入快捷鍵`ctrl + c`，強迫中斷後端程式

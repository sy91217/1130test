# 先準備資料, 再建立網站伺服器
# 準備資料
import json
file=open("data.txt", mode="r", encoding="utf-8")
data=json.load(file) # 網站沒有中斷, 因此伺服器中資料活著
file.close() # 伺服器不會中斷, 因此不會自動關閉檔案, 最好關掉

# 建立網站伺服器
# flask # 安裝 flask, 在 terminal 輸入 pip install flask (不能 cls)
from flask import * # 載入 flask 模組
app=Flask("My Website") # 建立一個網站應用程式物件

# 最關鍵
# 網站的網址: https://主機名稱/路徑?參數名稱=資料&參數名稱=資料&... # 幫助使用者連線到主機/程式
# 例如: http://127.0.0.1:5000/
@app.route("/") # 指定對應的網址路徑 # 若有人連線到對應路徑, 則執行下列動作 (若出現 404, 不代表無法連上網站, 代表程式不提供該路徑服務)
def home(): # 對應的處理函式
    return "<h3>Hello Flask</h3><div>This is line 1</div><script>alert('Hello');</script>" # 回應給前端的訊息 # 可直接使用 JavaScript 語法撰寫

# 例如: http://127.0.0.1:5000/test.php?keyword=關鍵字
@app.route("/test.php") # 指定對應的網址路徑 # 若有人連線到對應路徑, 則執行下列動作 (若出現 404, 不代表無法連上網站, 代表程式不提供該路徑服務)
def test(): # 對應的處理函式
    # 取得網址列上的參數: request.args.get("參數名稱", 預設值)
    keyword=request.args.get("keyword", None) # 若使用者沒有輸入關鍵字, 則會出現預設值
    if keyword==None:
        return redirect("/") # 回應給前端的訊息 # 若沒有輸入關鍵字, 則導向首頁 # redirect: 重新導向其他路徑
    else:
        if keyword in data:
            return "中文: "+data[keyword]
        else:
            return "沒有翻譯"
            # return "Hello "+keyword # 回應給前端的訊息 # 網址上的關鍵字輸入甚麼, 網頁上就會跑出甚麼

# 若新增新的路徑, 必須強制中斷後重新啟動程式
# 後端寫程式碼, 在前端呈現 (前端/後端 皆可執行 code)

app.run() # 啟動伺服器
# 執行後, 下方會出現網址
# 由於是連上伺服器, 因此會一直跑, 若要強制中斷則要輸入 ctrl+c, 則會無法連上網站

# https://tw.search.yahoo.com/search?fr=yfp-search-sb&p=test
# https://tw.search.yahoo.com/search?fr=yfp-search-sb&p=測試
# 連線到 yahoo 的搜尋服務, 提供搜尋的關鍵字
# 參數: fr, p (yahoo 的搜尋服務會傳入兩種資料)

# lint tool 幫忙檢查程式














# 暖身
# 移除 Anaconda 和 Python 舊版本
# 在 terminal 打 python 可顯示版本

# while 迴圈
# result=0
# n=1
# while n<=10:
#     result+=n
#     n+=1
# print(result)

# for 迴圈
# result=0
# for n in range(1,11):
#     result+=n
# print(result)

# for 變數 in 列表:
# result=0
# for n in [5,7,2]:
#     result+=n
# print(result)

# 函式
# def test(n1,n2):
#     return n1+n2
# result=test(3,4)
# print(result)

# 讀取檔案
# file=open("data.txt",mode="r") # open 開啟檔案, 模式(mode): 讀取(read, r)
# data=file.read() # 讀取檔案後, 將資料匯入 data 變數中
# file.close() # 讀完把檔案關掉, 不然佔記憶體
# print(data) # 印出 data 中的資料 
# webcrawler
進階程式設計1A-期中報告(2025/04/17製作)

1.程式目標:
爬蟲亞洲大學資訊工程學系的教師介紹網頁,抓取每位教師的姓名和研究領域
並將它儲存成.txt檔和儲存至SQLite的資料庫
---------------
2.爬蟲工具選擇
我主要是想選擇下列三種爬蟲工具,三個都使用過分析好壞再決定
---------------

                 |BeautifulSoup|                |Selenium|               |Scrapy|
|優點|    ----------------       |速度快|       -----------------     |可用於JavaScript動態載入|----- |最完整,適合較大型專案|

|缺點|   ----------    |無法處理 JavaScript|        -------------     |比較慢、耗資源大|         -------------        |好難@@|
 
|較適合用途|       ----  |表格,簡易用途|        ------------------------              |較泛用|                -------------     |大量資料,整個網站都要爬|

最終決定使用BeautifulSoup搭配Selenium 用簡單快速+完整緩慢互相彌補
並且將資料同時存至SQLite資料庫內


3.設計思路
---
|設定目標網址:定義網頁|

|初始化資料儲存:創建或連接到SQLite資料庫並對其初始化|

|遍歷目標網址:使用迴圈逐一處理每個網頁|

|抓取網頁內容:使用Selenium獲取頁面的原始HTML原始碼|

|解析網頁內容:使用Beautiful Soup函式庫解析HTML內容|

|提取姓名和研究領域:使用find方法定位後提取需要的資料|

|儲存資料:使用SQL的INSERT INTO語句將提取到儲存|

|善後:錯誤處理、關閉資源、輸出結果、輸入檔案|

4.程式展示
---
主程式.py 最主要程式

附屬程式.py 是用來查看SQLite資料庫的簡易程式,可以將兩個程式一起放進Colab使用

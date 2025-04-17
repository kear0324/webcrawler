# webcrawler
進階程式設計1A-期中報告

1.程式目標:
爬蟲亞洲大學資訊工程學系的教師介紹網頁,抓取每位教師的姓名和研究領域
並將它儲存成.txt檔和儲存至SQLite的資料庫

2.爬蟲工具選擇
我主要是想選擇下列三種爬蟲工具,三個都使用過分析好壞再決定

                 |BeautifulSoup|                |Selenium|               |Scrapy|
|優點|    .........................       |速度快|      ...............          |可用於JavaScript動態載入|    ............... |最完整,適合較大型專案|

|缺點|     ..........   ..........     |無法處理 JavaScript|      ...............          |比較慢、耗資源大|               ...............       |好難@@|
 
|較適合用途|    ..........  ..........     |表格,簡易用途|         ...............                  |較泛用|                ...............        |大量資料,整個網站都要爬|

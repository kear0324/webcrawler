!pip install requests beautifulsoup4 selenium webdriver-manager

import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

urls = [
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty",
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_professor",
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_Associate_Professor",
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_Assistant_Professor",
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_Lecturer",
    "https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Part_time_faculty"
]
db_filename = "teacher_research_areas_combined.db"
txt_filename = "all_teacher_research_areas_combined.txt"
use_selenium = True

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    url TEXT,
    name TEXT,
    research_area TEXT,
    method TEXT  -- 記錄爬取方法 (requests/selenium)
)
""")
conn.commit()

all_teacher_research_areas_txt = ""

if use_selenium:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    except Exception as e:
        print(f"Selenium WebDriver 初始化失敗：{e}")
        use_selenium = False
        print("將嘗試使用 requests 和 BeautifulSoup 進行爬蟲。")
else:
    driver = None

for url in urls:
    print(f"正在爬取：{url} (使用 {'Selenium' if use_selenium else 'requests'})")
    all_teacher_research_areas_txt += f"--- {url} (使用 {'Selenium' if use_selenium else 'requests'}) ---\n"
    try:
        if use_selenium and driver:
            driver.get(url)
            time.sleep(3)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        else:
            response = requests.get(url)
            response.raise_for_status()
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')

        teacher_items = soup.find_all('div', class_='i-member-item')

        for item in teacher_items:
            name_span = item.find('span', class_='member-data-value-name')
            research_area_span = item.find('span', class_='member-data-value-7')

            if name_span and research_area_span:
                name_link = name_span.find('a')
                if name_link:
                    name = name_link.text.strip()
                else:
                    name = name_span.text.strip()
                research_area = research_area_span.text.strip()

                cursor.execute("INSERT INTO teachers (url, name, research_area, method) VALUES (?, ?, ?, ?)",
                               (url, name, research_area, 'selenium' if use_selenium else 'requests'))
                all_teacher_research_areas_txt += f"{name}：{research_area}\n"

    except Exception as e:
        error_message = f"爬取 {url} 時發生錯誤 (使用 {'Selenium' if use_selenium else 'requests'})：{e}\n"
        print(error_message)
        all_teacher_research_areas_txt += error_message + "\n"

    all_teacher_research_areas_txt += "\n"
    conn.commit()
    time.sleep(1)

if use_selenium and driver:
    driver.quit()

with open(txt_filename, "w", encoding="utf-8") as file:
    file.write(all_teacher_research_areas_txt)

conn.close()

print(f"所有網頁的老師專長已儲存到 {txt_filename} 檔案中。")
print(f"所有網頁的老師專長也已儲存到 SQLite 資料庫 {db_filename} 中。")

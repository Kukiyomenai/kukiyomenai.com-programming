import re
import requests
from bs4 import BeautifulSoup

url = "https://news.yahoo.co.jp/"

# User-Agentを指定してHTMLを取得 (403エラー回避のため)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')

# 主要ニュースのリストを取得
# やり方その1
pickups = soup.find_all(href=re.compile("https://news.yahoo.co.jp/pickup"))
# やり方その2
# pickups = soup.select("a.sc-1nhdoj2-1")

for i in pickups:
    print(i.text)
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 設定部分 ---
# 監視したいメルカリの検索結果ページのURL
TARGET_URL = "https://jp.mercari.com/search?keyword=ストームエメラルダ&sort=created_time&order=desc&status=on_sale"
# 欲しい価格（以下）
TARGET_PRICE = 500 
# 監視の間隔（秒）
CHECK_INTERVAL = 300


def check_mercari_price():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1000,500')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(service=Service(), options=options)
    
    try:
        driver.get(TARGET_URL)
        wait = WebDriverWait(driver, 10)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//li[@data-testid="item-cell"]'))
        )
        item_cells = driver.find_elements(By.XPATH, '//li[@data-testid="item-cell"]')

        if not item_cells:
            print("検索結果の商品が見つかりませんでした。")
            return

        first_item = item_cells[0]

        name_elem = first_item.find_element(By.XPATH, './/*[contains(@class, "itemName__")]')
        price_elem = first_item.find_element(By.XPATH, './/*[contains(@class, "number__")]')

        latest_name = name_elem.text
        latest_price_str = price_elem.text
        latest_price = int(latest_price_str.replace("¥", "").replace(",", "").replace("円", "").strip())

        print(f"----------------------------------------")
        print(f"【最新出品】: {latest_name}")
        print(f"【現在価格】: {latest_price:,}円  (希望価格: {TARGET_PRICE:,}円)")

        if latest_price <= TARGET_PRICE:
            print(f"希望価格以下の商品が出品されました！ ({latest_price:,}円)")
        else:
            print("希望価格以下の商品はまだ出品されていません。")

    except Exception as e:
        print(f"エラーが発生しました: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    print("メルカリの価格監視を開始...")
    
    while True:
        check_mercari_price()
        print(f"次回チェックまで {CHECK_INTERVAL} 秒待機...\n")
        time.sleep(CHECK_INTERVAL)
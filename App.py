from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def get_first_yandex_image_selenium(image_url):
    search_url = f"https://yandex.com/images/search?rpt=imageview&url={image_url}"

    # Setup WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Jalankan tanpa GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(search_url)
    time.sleep(3)  # Tunggu loading halaman

    try:
        # Cari elemen gambar pertama di hasil pencarian
        first_image = driver.find_element(By.XPATH, '//img[contains(@class, "serp-item__thumb")]')
        image_src = first_image.get_attribute("src")
    except Exception as e:
        image_src = None
    finally:
        driver.quit()
    
    return image_src

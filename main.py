from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
web = "https://www.trendyol.com/butik/liste/2/erkek"
driver.get(web)

keyword = "dumbell"

driver.implicitly_wait(5)

search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/input")
search_box.send_keys(keyword)

search_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div/i")
search_button.click()

driver.implicitly_wait(5)

product_price = []

items = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "p-card-wrppr with-campaign-view add-to-bs-card")]')))

for item in items:
    whole_price = item.find_elements(By.XPATH, './/div[@class="prc-box-dscntd"]')

    if whole_price != []:
        price = whole_price[0].text
    else:
        price = 0
    product_price.append(price)

print(product_price)


driver.quit()


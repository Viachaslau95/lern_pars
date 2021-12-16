from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime



options = webdriver.ChromeOptions()

#user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36)")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

# headless mode
# options.add_argument("--headless")
# options.headless = True

driver = webdriver.Chrome(
    executable_path='/home/yaroslav/projects/Scraping/lern_pars/selenium_pars/chromedriver/chromedriver',
    options=options
)

try:
    start_time = datetime.datetime.now()
    driver.get("https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty")
    # print(driver.window_handles)
    time.sleep(5)
    driver.implicitly_wait(5)

    items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")
    items[0].click()
    time.sleep(5)
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])

    username = driver.find_element_by_class_name("seller-info-name")
    print(f"User name is: {username.text}")
    time.sleep(3)
    # driver.implicitly_wait(5)

    driver.close()

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)
    # driver.implicitly_wait(5)

    items[1].click()
    time.sleep(5)
    # driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)
    # driver.implicitly_wait(5)

    # username = driver.find_element_by_xpath("//div[@data-marker='seller-info/name']")

    ad_date = driver.find_element_by_class_name("title-info-metadata-item-redesign")
    print(f"Date:{ad_date.text}")

    finish_time = datetime.datetime.now()
    spend_time = finish_time - start_time
    print(spend_time)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

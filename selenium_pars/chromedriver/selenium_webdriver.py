from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36)")


# disable webdriver mode

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    executable_path='/home/yaroslav/projects/Scraping/lern_pars/selenium_pars/chromedriver/chromedriver',
    options=options
)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

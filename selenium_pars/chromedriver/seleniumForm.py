from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from auth_data import vk_login, vk_password


# url = "https://www.instagram.com/"


options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36)")


driver = webdriver.Chrome(
    executable_path='/home/yaroslav/projects/Scraping/lern_pars/selenium_pars/chromedriver/chromedriver',
    options=options
)

try:
    driver.get("https://vk.com/")
    time.sleep(5)

    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys(vk_login)

    password_input = driver.find_element_by_id("index_pass")
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    # login_button = driver.find_element_by_id("index_login_button").click()
    time.sleep(10)

    profile_link = driver.find_element_by_id("l_pr").click()
    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

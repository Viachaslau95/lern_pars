# from selenium import webdriver
from seleniumwire import webdriver
import time
import random
from fake_useragent import UserAgent

# url = "https://www.instagram.com/"

user_agent_list = [
    "hello",
    "top 1",
    "best_of_the_best"
]
useragent = UserAgent()

# options
options = webdriver.ChromeOptions()
# options.add_argument("user-agent=HelloWorld:)")
# options.add_argument(f"user-agent={random.choice(user_agent_list)}")
options.add_argument(f"user-agent={useragent.random}")

# set proxy
# options.add_argument("--proxy-server=138.128.91.65:8000")

driver = webdriver.Chrome(
    executable_path='/home/yaroslav/projects/Scraping/lern_pars/selenium_pars/chromedriver/chromedriver',
    options=options
)

try:
    driver.get(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent")
    time.sleep(5)
    # driver.get("https://2ip.ru")
    # time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data(url):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Connection": "keep-alive",
        "User - Agent":
            "Mozilla / 5.0(X11;Linux x86_64) AppleWebKit/537.36(KHTML, likeGecko) Chrome / 96.0.4664.45Safari/537.36"
    }

    r = requests.get(url=url, headers=headers)

    with open("index.html", "w") as file:
        file.write(r.text)

    # get hotels urls
    r = requests.get("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%&r=936629060", headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    hotels_cards = soup.find_all("div", class_="hotel_card_dv")

    for hotel_url in hotels_cards:
        hotel_url = hotel_url.find("a").get("href")
        print(f"https//www.tury.ru{hotel_url}")


# def get_data_with_selenium(url):
#     options = webdriver.ChromeOptions()
#     # options.send_keys("")


def main():
    get_data("https://www.tury.ru/hotel/most_luxe.php")


if __name__ == '__main__':
    main()
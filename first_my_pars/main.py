import requests
from bs4 import BeautifulSoup
import json

url = "https://www.khl.ru/standings/"

headers = {
    "user-agent":
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

req = requests.get(url)
src = req.text
#
# with open("index.html", "w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
#
soup = BeautifulSoup(src, "lxml")

# conference = soup.find(class_="b-data_row").find("h4").text
table_data_west = soup.find_all(class_="b-data_row")[0].find_all("tr")
table_info_west = list()

for item in table_data_west[1:]:
    club_inf = item.find_all("td")
    name = item.find(class_="e-club_name")

    title = name.text
    position = club_inf[0].text
    games = club_inf[2].text
    win_games = club_inf[3].text
    points = club_inf[10].text

    table_info_west.append(
        {
            "Title": title,
            "Position": position,
            "Games": games,
            "Win": win_games,
            "Points": points,
        }
    )

with open(f"data/West.json", "a", encoding="utf-8") as file:
    json.dump(table_info_west, file, indent=4, ensure_ascii=False)

table_data_east = soup.find_all(class_="k-data_table")[1].find_all("tr")

table_info_east = list()
for item in table_data_east[1:]:
    club_inf = item.find_all("td")
    name = item.find(class_="e-club_name")

    title = name.text
    position = club_inf[0].text
    games = club_inf[2].text
    win_games = club_inf[3].text
    points = club_inf[10].text

    table_info_east.append(
        {
            "Title": title,
            "Position": position,
            "Games": games,
            "Win": win_games,
            "Points": points,
        }
    )

with open(f"data/East.json", "a", encoding="utf-8") as file:
    json.dump(table_info_east, file, indent=4, ensure_ascii=False)

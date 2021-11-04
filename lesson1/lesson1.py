import re

from bs4 import BeautifulSoup

with open("blank/index.html")as file:
    src = file.read()
# print(src)


soup = BeautifulSoup(src, "lxml")

#
# title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", {"class": "user_name"}).find("span").text
# print(user_name)
# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)
#
# for item in find_all_spans_in_user_info:
#     print(item.text)

# links = soup.find(class_="social__networks").find("ul").find_all("a")
# for item in links:
#     item_text = item.text
#     item_url = item.get("href")
#     print(f"{item_text}: {item_url}")


find_a_by_text = soup.find("a", text=re.compile("Instagram"))
print(find_a_by_text)

find_all_by_text = soup.find_all(text=re.compile("([Ii]nstagram)"))
print(find_all_by_text)
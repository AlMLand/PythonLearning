import os

import requests
from bs4 import BeautifulSoup

# these packages are used to extract the data from the page
# necessary packages: requests, lxml, beautifulsoup4 (bs4)

#       syntax                          match result
#   soup.select("div")              all elements with "div" tag
#   soup.select("#some_id")         all elements with id="some_id"
#   soup.select(".some_class")      all elements with class="some_class"
#   soup.select("div span")         all elements with "span" tag inside "div" tag
#   soup.select("div > span")       all elements with "span" tag directly inside "div" tag, with nothing in between

# result = requests.get('https://example.com/')
# soup = BeautifulSoup(result.text, 'html.parser')
# print(soup.select("title")[0].get_text())

result = requests.get(
    "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%8D%D0%BF%D0%B8%D0%B7%D0%BE%D0%B4%D0%BE%D0%B2_%D1%82%D0%B5%D0%BB%D0%B5%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B0_%C2%AB%D0%9D%D0%B0%D1%80%D0%BA%D0%BE%C2%BB")
soup = BeautifulSoup(result.text, 'html.parser')

# GET СОДЕРЖАНИЕ
for tag in soup.select(".toclevel-1"):
    uis = tag.select(".toclevel-2")
    if uis:
        print(tag.select("a")[0].get_text())
        for ui in uis:
            print(f"  {ui.get_text()}")
    else:
        print(tag.get_text())

# DOWNLOAD IMAGE
# get the source of the image from the page
image_src = soup.select(".mw-file-element")[0]["src"]
# get the name of the image from the source, all after last /
image_name = image_src.split("/")[-1]
# download the image from the page
image = requests.get(f"https:{image_src}")
# create a folder for the images if it does not exist
folder_name = "images"
os.makedirs(folder_name, exist_ok=True)
# save the image to the folder "images"
if not os.path.exists(f"{folder_name}\\{image_name}"):
    with open(f"{folder_name}\\{image_name}", "wb") as file:
        file.write(image.content)

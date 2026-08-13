from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
textt=response.text
soup=BeautifulSoup(textt,"html.parser")

print(soup.find(name="span",class_="titleline"))


























# with open("website.html") as f:
#     content = f.read()
#
# soup = BeautifulSoup(content, "html.parser")
# # print(soup.prettify())
# print(soup.find_all(name="a"))
#
#
# for tag in soup.find_all(name="a"):
#     print(tag.get("href"))

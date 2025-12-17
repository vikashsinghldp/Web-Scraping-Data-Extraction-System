import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.wikihow.com/Main-Page"
response = requests.get(url)
#print(response.status_code)
#print(response.text)
html = response.text
soup = BeautifulSoup(html, "html.parser")
#print(soup.title)
#find header tag
header = soup.find("h1")

for p in soup.find_all("p"):
    #print(p.text)
    pass

soup.find("div", class_="content")
soup.find_all("span", class_="price")
soup.find(id="main")
soup.find_all("a", href=True)
soup.select("div.article h2")
soup.select(".price")
soup.select("#main")

#extract link
links = soup.find_all("a")

for link in links:
    print(link.get("href"))

#Handling headers
headers = {
    "User-Agent": "Mozilla/5.0"
}

#response = requests.get(url, headers=headers)
# with open("data.txt", "w", encoding="utf-8") as f:
#     f.write(response.text)
#titles = soup.find_all("h2", class_="post-title")
titles = soup.find_all("p")
with open("post.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"])
    for title in titles:
        writer.writerow([title.text])

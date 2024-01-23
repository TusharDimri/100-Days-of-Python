import requests
from bs4 import BeautifulSoup 

response=requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

article_texts = []
article_links = []

article_tag = soup.select(selector=".titleline a")
print(article_tag)
for article in article_tag:
    article_text = article.getText()
    article_texts.append(article_text)

    article_link =  article.get("href")
    article_links.append(article_link)

article_upvote = soup.find_all(name="span", class_="score")

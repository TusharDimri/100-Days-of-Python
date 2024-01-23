import requests
from bs4 import BeautifulSoup 

response=requests.get("https://news.ycombinator.com/")
page = response.text

soup = BeautifulSoup(page, 'html.parser')
print(soup.title)

article_texts = []
article_links = []

article_tag = soup.select(selector=".titleline a")
# print(article_tag)
for article in article_tag:
    article_text = article.getText()
    article_texts.append(article_text)

    article_link =  article.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.select(selector=".score")]

print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
index = article_upvotes.index(largest_number)
print(index)
print(article_texts[index], article_links[index])
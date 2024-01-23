from bs4 import BeautifulSoup
import lxml

with open("website.html", "r", encoding="utf8") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'lxml')
print(soup.title.string)
# print(soup.prettify())
# print(soup.a) # First a tag in the website
# print(soup.p) # First p tag in the website

all_a_tags = soup.find_all(name="a")
#print(all_a_tags)
for tag in all_a_tags:
    print(tag.getText(), tag.get("href"))

heading = soup.find_all(name="h1", id="name")
print(heading)

section_heading= soup.find_all(name="h3", class_="heading") # Attribute is called class_  because class is a reserved keyword in Python.
print(section_heading[0].get("class"))

company_url = soup.select_one(selector="p a")
print(company_url.getText())

name = soup.select_one(selector="#name")
print(name.getText())

headings = soup.select(selector=".heading")
print(headings)
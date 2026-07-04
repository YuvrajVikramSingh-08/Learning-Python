from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

article_tag = soup.select(selector=".titleline > a")
article_upvote = soup.find_all(name="span", class_="score")
# t = soup.find_all(name = "span", class_="titleline")

i = 0

article_texts = []
article_links = []
article_upvotes = [score.getText() for score in article_upvote]
for item in article_tag:
    article_link = item.get("href")
    article_links.append(article_link)
    article_text = item.getText()
    article_texts.append(article_text)
    n_up = article_upvote[i].getText()
    # article_upvotes.append(n_up)
    # print(article_link)
    # print(article_text)
    # print(n_up)
    i += 1

article_upvotes = [int(upvote.split()[0]) for upvote in article_upvotes]
# print(article_links)
# print(article_texts)
# print(article_upvotes)

ind = 0
for i in range(len(article_upvotes)):
    if article_upvotes[i] == max(article_upvotes):
        ind = i

print(f'''Article Title: {article_texts[ind]}
Article Link: {article_links[ind]}
Article Upvotes: {article_upvotes[ind]}''')


# import lxml
#
# with open("./website.html", "r") as web:
#     content = web.read()
#
# soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
#
# print(soup.prettify())
# print(soup.a)
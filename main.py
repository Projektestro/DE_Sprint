import requests as req
from bs4 import BeautifulSoup
import json
import tqdm

data = {
    "data":[]
}

for page in range(1,11):
    url = f"https://habr.com/ru/search/page{page}/?q=Data%20science&target_type=posts&order=relevance"
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tag_time = soup.find(class_ = "tm-article-snippet__datetime-published").text[0:16]
    tag_title = soup.find(attrs= {"data-test-id": "article-snippet-title-link"}).text
    tag_rating = soup.find(class_ = "tm-votes-meter__value tm-votes-meter__value tm-votes-meter__value_positive tm-votes-meter__value_appearance-article tm-votes-meter__value_rating").text
    tag_href = soup.find(attrs= {"data-test-id":"article-snippet-title-link"})

    print(tag_time, tag_title, tag_rating, tag_href.attrs["href"])

    url_object = "https://habr.com" + tag_href.attrs["href"]
    resp_object = req.get(url_object)
    soup = BeautifulSoup(resp_object.text, "lxml")

    while True:
        try:
            tag_tag = soup.find(class_ = "tm-tags-list__link").text
            print(f"Теги: {tag_tag}")
            break
        except AttributeError:
            print(f"Теги: - ")
            break

    while True:
         try:
            tag_hab = soup.find(class_="tm-hubs-list__link router-link-active").text
            print(f"Хабы: {tag_hab}")
            break
         except AttributeError:
            print(f"Хабы: - ")
            break

    data["data"].append({"Datetime":tag_time, "Title":tag_title, "Rating":tag_rating, "Tag":tag_tag, "Hab":tag_hab, "Url":url_object})
    # print(data)

    with open("data.json", "w") as file:
        json.dump(data, file, ensure_ascii=False)
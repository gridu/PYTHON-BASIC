import calendar
from datetime import datetime
from unittest import mock

import requests
from bs4 import BeautifulSoup
import re
import math
import unittest
from unittest.mock import Mock, MagicMock


class Article:
    def __init__(self, date, title, author, time_to_read=""):
        self.date = date
        self.title = title
        self.author = author
        self.time_to_read = time_to_read


def print_sheet(sheet_title, articles_to_print, num_of_articles, width_of_title):
    width_sheet = 100
    author_width = 24

    sheet_title = " " + sheet_title + " "

    for _ in range(math.floor((width_sheet - len(sheet_title)) / 2)):
        print("=", end="")
    print(sheet_title, end="")
    for _ in range(math.ceil((width_sheet - len(sheet_title)) / 2)):
        print("=", end="")
    print()

    print(f'| {articles_to_print[0][0]:<{width_of_title}} | ', end="")
    print(f'{articles_to_print[1][0]:<{author_width + 6}} | ', end="")
    print(f'{articles_to_print[2][0]:<{10}} | ', end="")
    print(f'{articles_to_print[3][0]:<{9}} |')

    for _ in range(width_sheet):
        print("-", end="")
    print()

    counter_of_printed_articles = 0
    for i in range(1, len(to_print[0])):
        print(f'| {articles_to_print[0][i]:<{width_of_title}} | ', end="")
        print(f'{articles_to_print[1][i]:<{author_width + 6}} | ', end="")
        print(f'{articles_to_print[2][i]} | ', end="")
        print(f'{articles_to_print[3][i][:-5]:<{9}} |')

        if articles_to_print[3][i] != " ":
            counter_of_printed_articles += 1
            if counter_of_printed_articles == num_of_articles:
                break


def get_all_articles(url) -> list:
    req = requests.get(url)
    print(type(req.content))

    cont = BeautifulSoup(req.content, "html.parser")
    # print(cont.prettify())
    articles = cont.find_all("article")
    articles_list = []
    for article in articles:
        art_date = article.find(class_="name")
        art_date = re.search("[A-Z][a-z]. [0-3][0-9], [1-2][0-9]..", art_date.text).group(0)
        # print(art_date)
        art_date = str(list(calendar.month_abbr).index(art_date[0:3])) + art_date[3:]
        art_date = datetime.strptime(art_date, "%m %d, %Y")
        art_date = art_date.date()

        author = article.find("strong").text.strip()
        # print(hm.text.strip())

        time_to_read = article.find("b").text.strip()
        # print(time_to_read)

        title = article.find("h4").text + "."
        # print(title)
        articles_list.append(Article(art_date, title, author, time_to_read))

    return articles_list


def sort_newest_articles(articles_list, max_title_size) -> list:
    articles_list.sort(key=lambda article: article.date, reverse=True)
    to_print = [["Title of the article"], ["Author"], ["Date"], ["Read time"]]

    for article in articles_list:
        title_to_split = str(article.title)
        num_of_lines = 0
        while len(title_to_split) > max_title_size:
            space_index = max_title_size - 1
            if title_to_split[max_title_size] == " ":
                space_index = max_title_size
            else:
                while title_to_split[space_index] != " ":
                    space_index -= 1
            to_print[0].append(title_to_split[:space_index])
            title_to_split = title_to_split[space_index + 1:]
            num_of_lines += 1
        if len(title_to_split) > 0:
            to_print[0].append(title_to_split)
            num_of_lines += 1

        to_print[1].append(article.author)
        to_print[2].append(article.date)
        to_print[3].append(str(article.time_to_read))
        for _ in range(num_of_lines - 1):
            to_print[1].append(" ")
            to_print[2].append("          ")
            to_print[3].append(" ")

    return to_print


def sort_fastest_to_read_articles(articles_list, max_title_size) -> list:
    articles_list.sort(key=lambda article: int(article.time_to_read[:-9]))
    to_print = [["Title of the article"], ["Author"], ["Date"], ["Read time"]]

    for article in articles_list:
        title_to_split = str(article.title)
        num_of_lines = 0
        while len(title_to_split) > max_title_size:
            space_index = max_title_size - 1
            if title_to_split[max_title_size] == " ":
                space_index = max_title_size
            else:
                while title_to_split[space_index] != " ":
                    space_index -= 1
            to_print[0].append(title_to_split[:space_index])
            title_to_split = title_to_split[space_index + 1:]
            num_of_lines += 1
        if len(title_to_split) > 0:
            to_print[0].append(title_to_split)
            num_of_lines += 1

        to_print[1].append(article.author)
        to_print[2].append(article.date)
        to_print[3].append(str(article.time_to_read))
        for _ in range(num_of_lines - 1):
            to_print[1].append(" ")
            to_print[2].append("          ")
            to_print[3].append(" ")

    return to_print


url = "https://blog.griddynamics.com/"

articles_list = get_all_articles(url)
max_title_size = 38

to_print = sort_newest_articles(articles_list, max_title_size)
num_of_newest_articles = 5
print_sheet("Newest articles from Grid Dynamics' blog", to_print, num_of_newest_articles, max_title_size)

to_print = sort_fastest_to_read_articles(articles_list, max_title_size)
num_of_fastest_articles = 10
print_sheet("Fastest to read articles from Grid Dynamics' blog", to_print, num_of_fastest_articles, max_title_size)


class TestArticlesParsing(unittest.TestCase):
    def setUp(self) -> None:
        self.articles = [Article(datetime.strptime("09 13, 2022", "%m %d, %Y").date(),
                            "Totally original title", "Free Guy", "1337 min read"),
                        Article(datetime.strptime("09 15, 2022", "%m %d, %Y").date(),
                            "Better love story than Twilight", "Simon Qwertyso", "25 min read"),
                        Article(datetime.strptime("09 14, 2022", "%m %d, %Y").date(),
                            "Python for beginners book is now available", "Kek Doublev", "22 min read")
                        ]

    def test_newest_articles(self):
        to_print_newest_articles = sort_newest_articles(self.articles, 38)
        self.assertEqual(to_print_newest_articles[0][1], "Better love story than Twilight")
        self.assertEqual(to_print_newest_articles[0][2], "Python for beginners book is now")
        self.assertEqual(to_print_newest_articles[0][3], "available")
        self.assertEqual(to_print_newest_articles[0][4], "Totally original title")
        self.assertEqual(to_print_newest_articles[1][1], "Simon Qwertyso")
        self.assertEqual(to_print_newest_articles[1][2], "Kek Doublev")
        self.assertEqual(to_print_newest_articles[1][4], "Free Guy")
        self.assertEqual(to_print_newest_articles[2][1], datetime(2022, 9, 15).date())
        self.assertEqual(to_print_newest_articles[2][2], datetime(2022, 9, 14).date())
        self.assertEqual(to_print_newest_articles[2][4], datetime(2022, 9, 13).date())
        self.assertEqual(to_print_newest_articles[3][1], "25 min read")
        self.assertEqual(to_print_newest_articles[3][2], "22 min read")
        self.assertEqual(to_print_newest_articles[3][4], "1337 min read")

    def test_fastest_articles(self):
        to_print_fastest_articles = sort_fastest_to_read_articles(self.articles, 38)
        self.assertEqual(to_print_fastest_articles[0][3], "Better love story than Twilight")
        self.assertEqual(to_print_fastest_articles[0][1], "Python for beginners book is now")
        self.assertEqual(to_print_fastest_articles[0][2], "available")
        self.assertEqual(to_print_fastest_articles[0][4], "Totally original title")
        self.assertEqual(to_print_fastest_articles[1][3], "Simon Qwertyso")
        self.assertEqual(to_print_fastest_articles[1][1], "Kek Doublev")
        self.assertEqual(to_print_fastest_articles[1][4], "Free Guy")
        self.assertEqual(to_print_fastest_articles[2][3], datetime(2022, 9, 15).date())
        self.assertEqual(to_print_fastest_articles[2][1], datetime(2022, 9, 14).date())
        self.assertEqual(to_print_fastest_articles[2][4], datetime(2022, 9, 13).date())
        self.assertEqual(to_print_fastest_articles[3][3], "25 min read")
        self.assertEqual(to_print_fastest_articles[3][1], "22 min read")
        self.assertEqual(to_print_fastest_articles[3][4], "1337 min read")


    """
    @mock.patch('requests.get')
    def test_all_articles_parsed(self, mock_request):
        article = "<article> <span class=\"badge\">Featured post</span> <div class=\"author\"> " + \
                  "<img alt=\"Eugene Steinberg\" class=\"b-lazy\" data-src=\"headshot.png\" " + \
                  "src=\"data:image/gif\"/> <span class=\"name\"> <strong> Eugene Steinberg	</strong> <br/> " + \
                  "Sep 15, 2022 • <b>	1337 min read </b> </span> </div> <div class=\"cardbody\"> " + \
                  "<h4 class=\"ellip2\">Very original title</h4> <p class=\"ellip3\">" + \
                  "Originally published by Total Retail E-commerce</p> <span class=\"arrow\">Learn more</span> " + \
                  "</div> </article>"
        article = article.encode()
        mock_request.content.return_value = article
        article = get_all_articles("https://blog.griddynamics.com/")
        self.assertEqual(article, [2, 4, "as"])
    """


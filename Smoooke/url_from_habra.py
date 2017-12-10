import requests
from lxml import html
import re


def get_topics():

    request  = requests.get(url='https://habrahabr.ru/')
    parser_body_top_index = html.fromstring(request.text)

    list_url = []

    for i in parser_body_top_index.xpath('//a/@href'):
        searching_url = re.match(r'^https:\/\/habrahabr.ru\/post\/\d{6,7}[^?#]*', i)
        if searching_url != None:
            list_url.append(searching_url.group())

    clear_list = []

    for i in list_url:
        if i not in clear_list:
            clear_list.append(i)

    return clear_list

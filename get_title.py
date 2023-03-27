import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime


def get_title(url,var = 0):
    parse_url = urlparse(url)
    if parse_url != "http" and parse_url != "https":
        parse_url._replace(scheme="http")
    response = requests.get(url)  # URLからHTMLを取得するこれで追加
    if not response.ok:
        raise ValueError("URLへのアクセスに失敗しました．")
    soup = BeautifulSoup(response.text, "html.parser")
    # タイトルを取得
    if soup.title is None:
        raise ValueError("Title is None")
    title = soup.title.string
    # 日付を取得
    dt = datetime.datetime.now()
    year = dt.year
    month = dt.month
    day = dt.day

    if var == 0:
        ret = title
    elif var == 1: 
        ret = f'Auther:"{title}",{url},({year}/{month}/{day}閲覧)'
    elif var == 2:
        ret = f'Auther({year}/{month}/{day}).「{title}」.{url}.({year}/{month}/{day}閲覧)'
    elif var == 3:
        ret = f'<a href="{url}" title="{title}">{title}</a>'
    elif var == 4:
        ret = f'[{title}]({url})'
    else:
        ret = title

    return ret
import requests
from bs4 import BeautifulSoup
import datetime


def get_title(url,var = 0):
    try:
        response = requests.get(url)  # URLからHTMLを取得する
        soup = BeautifulSoup(response.text, "html.parser")  # HTMLをBeautifulSoupオブジェクトに変換する        
    except:
        return '<Failed>This URL is of a form that cannot be processed or does not exist.'

    # タイトルを取得
    title = soup.title.string
    # 日付を取得
    dt = datetime.datetime.now()
    year = dt.year
    month = dt.month
    day = dt.day

    ret = title
    if var == 0:
        ret = title
    elif var == 1: 
        ret = f'Auther:"{title}",{url},({year}/{month}/{day}閲覧)'
    elif var == 2:
        ret = f'Auther({year}/{month}/{day}).「{title}」.{url}.({year}/{month}/{day}閲覧)'
    elif var == 3:
        ret = f'<a href="{url}" title="{title}">{title}</a>'
    else:
        ret = title

    return ret



print(get_title('http://nishikiout.com'))
print(get_title('hta[gka]'))
import requests
from bs4 import BeautifulSoup
import datetime


def get_title(url,var = 0):
    try:
        response = requests.get(url)  # URLからHTMLを取得する
    except:
        try:
            url = f'http://{url}'
            response = requests.get(url)
        except:
            return '<Error>This URL is of a form that cannot be processed or does not exist.<ErrCode -1>'
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # タイトルを取得
    try:
        title = soup.title.string
    except:
        return '<Error>This URL could not be processed.<ErrCode -2>'
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
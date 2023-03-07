import requests
from bs4 import BeautifulSoup

def get_title(url):
    try:
        response = requests.get(url)  # URLからHTMLを取得する
        soup = BeautifulSoup(response.text, "html.parser")  # HTMLをBeautifulSoupオブジェクトに変換する

        title = soup.title.string  # titleタグの中身を取得する
        return title
    except:
        return 1;

    

print(get_title('http://nishikiout.com'))
print(get_title('hta[gka]'))
import requests
from bs4 import BeautifulSoup
import JokeManager

url = "http://www.qiushibaike.com/text/"
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
}

s = requests.session()
s.headers.update(headers)

res = s.get(url)
if res.ok:
    html = res.content.decode(encoding='utf-8')
    html = BeautifulSoup(html, 'html.parser')
    divs = html.find_all(name='div', attrs={"class": "article block untagged mb15"})
    jokes = []
    for div in divs:
        # print(div)
        joke_id = int(div.get('id').split('_')[2])
        content_div = div.find_all(name='div', attrs={'class': 'content'})[0]
        cont = content_div.get_text().strip()
        jokes.append((joke_id, cont))
    # 保存到redis
    JokeManager.saveJokesToRedis(jokes)
    print('done.')
else:
    print('error when accessing url:%s' % url)

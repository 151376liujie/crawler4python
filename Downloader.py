import requests
from Throttle import Throttle

class Downloader:
    '''
    下载器
    '''

    def __init__(self, delay, retry=2, user_agent='wswp'):
        self.throttle = Throttle(delay)
        self.retry = retry
        self.user_agent = user_agent

    def download(self, url):
        '''
        下载网页
        :param url:
        :return:
        '''
        self.throttle.wait(url)
        print("downloading:", url)
        if self.user_agent:
            headers = {"User-Agent": self.user_agent}
        resp = requests.get(url, headers=headers)
        if resp.ok:
            html = resp.content.decode('utf-8')
        else:
            print("download %s error " % url)
            html = None
            if self.retry > 0:
                return self.download(url, self.user_agent, self.retry - 1)
        return html

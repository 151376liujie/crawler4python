from urllib import parse
from _datetime import datetime
import time

class Throttle:

    def __init__(self,delay):
        self.delay = delay
        self.domains = {}

    def wait(self,url):
        '''
        判断一个URL在下载前需要延迟的时间，单位为秒
        :param url:
        :return:
        '''
        domain = parse.urlparse(url).netloc
        last_accessed_time = self.domains.get(domain)
        if self.delay > 0 and last_accessed_time is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed_time).seconds
            if sleep_secs > 0:
                print("going to sleep %d seconds" % sleep_secs)
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()
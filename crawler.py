import re
from urllib import parse
from Downloader import Downloader


def link_crawler(seedUrl, fetchedPattern,max_depth = -1,max_number_download = -1):
    '''
    爬取页面指定的链接
    :param seedUrl: 种子URL
    :param fetchedPattern:需要爬取的URL正则表达式
    :param max_depth: 最大深度，种子URL的深度为0，默认不限制
    :param max_number_download: 最大下载URL数量,默认不限制
    :return:
    '''
    url_queue = [seedUrl]
    # 存储已经爬取过的URL(key)和其深度
    seen = {seedUrl : 0}
    url_number_of_downloaded = 0
    downloader = Downloader(1)
    while url_queue:
        currUrl = url_queue.pop()
        depth = seen[currUrl]
        if depth != max_depth:
            #下载网页
            html = downloader.download(currUrl)
            #解析html中的所有链接
            allLinks = get_link(html)
            #只爬取指定的链接
            if fetchedPattern :
                wanted_links = filter(lambda li : re.match(fetchedPattern,li),allLinks)
            else:
                wanted_links = allLinks
            for link in wanted_links:
                #将解析到的相对链接转换为全链接
                link = parse.urljoin(seedUrl, link)
                if link not in seen:
                    seen[link] = depth + 1
                    url_queue.append(link)
        url_number_of_downloaded += 1
        if url_number_of_downloaded == max_number_download:
            break
    return url_number_of_downloaded,seen


def get_link(html):
    '''
    得到html页面中的所有链接
    :param html:
    :return:
    '''
    regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return regex.findall(html)

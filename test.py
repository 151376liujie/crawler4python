import crawler

def testDownload(url):
    html = crawler.download(url)
    print(html)

def testLinkCrawler(url,pattern,max_depth):
    links,seen = crawler.link_crawler(url,pattern,max_depth)
    print(links)
    print(seen)

if __name__ == '__main__':
    # testDownload("http://httpstat.us/500")
    testLinkCrawler("http://example.webscraping.com",'/(index)',max_depth=-1)



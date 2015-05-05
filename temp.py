__author__ = 'Yuanjiang Huang'
import urlparse

def main():
    link = 'www.rongmofang.com/project/list?page=0&duration=0&name=&status=4&guarantee=0'
    url = 'http://www.rongmofang.com/1'
    external = True
    print urlparse.urlparse(link).netloc
    print urlparse.urlparse(url).netloc
    if urlparse.urlparse(link).netloc == urlparse.urlparse(url).netloc:
        external = False
    print external

if __name__ == "__main__":
    main()

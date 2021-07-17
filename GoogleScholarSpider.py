import time, re, json, sys
from bs4 import BeautifulSoup
import pprint, requests


class GoogleScholarScholar:
    """
    Input: "https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7127218252840885994"
    Output : {paper_title:[...]} -> json format
    """
    def __init__(self):
        self.title = []

    def parser(self):
        """
        this code cannot work because it will be detected as ROBOT
        """

        REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Accept-Charset": "UTF-8,*;q=0.5"}
        page_url = "https://scholar.google.com/scholar?oi=bibs&hl=en&cites=7127218252840885994"

        session = requests.Session()
        res = session.get(page_url, headers=REQUEST_HEADERS)
        res.encoding = 'UTF-8'
        return res.text

    def run(self, res):
        self.title = []
        self.parse(res)
        return self.jsonencode()

    def parse(self, res):
        soup = BeautifulSoup(res, "lxml")
        for author in soup.select('.gs_ri .gs_rt a'):
            self.title.append(author.text)

    def jsonencode(self):
        # decode list data to json format
        return json.dumps({'paper_title': self.title})

if __name__ == '__main__':
    fpath = sys.argv[1]
    f = open(fpath, 'r')
    res = f.read()

    spider = GoogleScholarScholar()
    result = spider.run(res)
    pprint.pprint(result)

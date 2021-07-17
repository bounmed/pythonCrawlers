# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, re, json, pprint
from bs4 import BeautifulSoup

class MicroScholar:
    """
    Input: Bayesian operational modal analysis: Theory, computation, practice
    Output: {papers:[...], journal:’...’} (json format)
    """

    def __init__(self):
        self.papers = []

        self.journal = []
        self.affiliations = []
        self.query = ''
        self.res = ''

    def run(self, query):
        self.res = self.spider(query)
        self.parse()
        return self.jsonencode()

    def spider(self, query):
        driver = webdriver.Chrome()
        base_url = "https://academic.microsoft.com"
        driver.get(base_url + "/")
        #search-input
        #.ma-suggestion-control .suggestion-box input #SearchBoxSubmit
        driver.find_element_by_css_selector("#search-input").send_keys(query)
        driver.find_element_by_css_selector("#SearchBoxSubmit").click()

        newurl = driver.current_url.replace("&f=", "&f=Pt%3D%271%27")
        newurl = newurl.replace("orderBy=0", "orderBy=1")
        driver.get(newurl)

        time.sleep(3)
        res = driver.page_source
        driver.close()
        return res

    def parse(self):
        soup = BeautifulSoup(self.res, "lxml")


        for maCard in soup.find_all('ma-card'):
            paper = []
            authors = []
            print ("============================================")

            title = maCard.select('a.title')
            print(title)
            # parse authors and affiliations
            for author in maCard.select('.author'):
                authors.append(author.text)
            paper.append(authors)
            # parse journal
            tmp_journal = []
            for journal in maCard.select('.publication .au-target')[1:]:
                tmp_journal.append(str(journal.text))
            paper.append(tmp_journal)

            self.papers.append(paper)
        #mainArea > router-view > ma-serp > div > div.results > div > compose > div > div.results > ma-pager > div > i
    def jsonencode(self):
        # decode list data to json format
        return json.dumps({'papers': self.papers})

if __name__ == '__main__':
    query = "arabic pos deep learning"
    spider = MicroScholar()
    result = spider.run(query)
    pprint.pprint(result)

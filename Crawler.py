# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, re, json, pprint
from bs4 import BeautifulSoup

class MicrosoftScholar:
    """
    Input: Bayesian operational modal analysis: Theory, computation, practice
    Output: {papers:[...], journal:’...’} (json format)
    """

    def __init__(self):
        self.papers = []
        self.pages = []
        self.res = ''
        self.driver = ''

    def run(self, queries):
        paperlist = []
        self.driver = webdriver.Chrome()
        for query in queries:
            self.res = self.spider(query)
            self.parse()
            paperlist = paperlist + self.papers
        #return json.dumps({'papers': self.papers})
        self.driver.close()
        return json.dumps({'papers': paperlist})

    def spider(self, query):

        base_url = "https://academic.microsoft.com"
        self.driver.get(base_url + "/")
        #search-input
        #.ma-suggestion-control .suggestion-box input #SearchBoxSubmit
        self.driver.find_element_by_css_selector("#search-input").send_keys(query)
        self.driver.find_element_by_css_selector("#SearchBoxSubmit").click()
        #self.driver.find_element_by_id("SearchBoxSubmit").click()
        # order by date
        newurl = self.driver.current_url.replace("&f=", "&f=Pt%3D%271%27")
        newurl = newurl.replace("orderBy=0", "orderBy=1")
        self.driver.get(newurl)

        #self.driver.find_element_by_css_selector(".icon-up.right").click()
        #self.driver.find_element_by_css_selector("i[class='icon-up right au-target']").click()
        page = 0
        try:
            notfound = self.driver.find_element_by_css_selector(".not-found")
            notfound_page = len(notfound) > 0
        except NoSuchElementException:
            notfound_page = False


        while not notfound_page:
            self.pages.append(self.driver.page_source)
            newurl = newurl.replace("skip="+str(page*10), "skip="+str(page*10+10))
            self.driver.get(newurl)
            time.sleep(1)
            try:
                notfound = self.driver.find_element_by_css_selector(".not-found")
                notfound_page = len(notfound) > 0
            except NoSuchElementException:
                notfound_page = False
            page = page + 1
            #self.pages.append(self.driver.page_source)
            #self.driver.find_element_by_css_selector(".not-found").click()
        #print(res)
        #return res
        return ''

    def parse(self):
        for page_src in self.pages:
            soup = BeautifulSoup(page_src, "lxml")

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
    #query = "arabic pos deep learning"
    queries = [
            'arabic pos deep learning',
            'arabic pos neural network',
            'neural network arabic',
            'neural network Arabic pos'
            'neural network',
            'deep learning Arabic',
            'Arabic pos tagger',
            'Arabic pos tagging',
        ]
    spider = MicrosoftScholar()
    result = spider.run(queries)
    pprint.pprint(result)

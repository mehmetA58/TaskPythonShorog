import csv
import time

from base.logger import customLogger
from selenium.webdriver import Keys
from Pages.YahooPage import YahooPage
from Tests.test_base import BaseTest
from Config.config import TestData


class Test_YahooSearch(BaseTest):
    log = customLogger()

    def test_visible_yahoo_page(self):
        self.yahopage = YahooPage(self.driver)
        self.log.info("*****'LOGIN' YAHOO TESTS *****\n")
        flag = self.yahopage.is_yahoo_big_logo_is_displayed()
        assert flag
        self.log.info("Yahoo big logo is displayed\n")
        title = self.yahopage.get_title(TestData.YAHOO_PAGE_TITLE)
        assert title == TestData.YAHOO_PAGE_TITLE
        with open("C:\\Users\\PC\\IdeaProjects\\TaskPython\\TestData\\TestData.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
                self.yahopage.do_search_a_text_on_yahoo(row[0] + Keys.ENTER)
                time.sleep(3)
                assert row[0] in self.yahopage.GET_TITLE()
                self.log.info(row[0]+"with contains "+self.yahopage.GET_TITLE()+"\n")
                self.yahopage.do_csv_Write()
                self.yahopage.navigateBack()
        self.log.info("*****'CLOSE' YAHOO TESTS *****\n")

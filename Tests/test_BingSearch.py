import csv
import time
from base.logger import customLogger
from Config.config import TestData
from Pages.BingPage import BingPage
from Tests.test_base import BaseTest
from selenium.webdriver.common.keys import Keys


class Test_BingSearch(BaseTest):
    log = customLogger()

    def test_visible_bing_page(self):
        self.bingPage = BingPage(self.driver)
        self.log.info("*****'LOGIN' BING TESTS *****\n")
        flag = self.bingPage.is_bing_logo_isDisplayed()
        assert flag
        self.log.info("Google big logo is displayed\n")
        title = self.bingPage.get_title(TestData.BING_PAGE_TITLE)
        assert title == TestData.BING_PAGE_TITLE
        with open("C:\\Users\\PC\\IdeaProjects\\TaskPython\\TestData\\TestData.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
                self.bingPage.do_search_a_text_on_bing(row[0] + Keys.ENTER)
                time.sleep(3)
                assert row[0] in self.bingPage.GET_TITLE()
                self.bingPage.do_csv_Write()
                self.bingPage.navigateBack()
        self.log.info("*****'CLOSE' BING TESTS *****\n")


import csv
import time

from selenium.webdriver.common.keys import Keys

from Pages import BasePage
from Pages.GooglePage import GooglePage
from Tests.test_base import BaseTest
from Config.config import TestData


class Test_GoogleSearch(BaseTest):

    def test_google_page(self):
        self.googlePage = GooglePage(self.driver)
        flag = self.googlePage.is_google_big_logo_is_displayed()
        assert flag
        title = self.googlePage.get_title(TestData.GOOGLE_PAGE_TITLE)
        assert title == TestData.GOOGLE_PAGE_TITLE
        with open("C:\\Users\\PC\\IdeaProjects\\TaskPython\\TestData\\TestData.csv", 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                print(row)
                self.googlePage.do_search_a_text_on_google(row[0] + Keys.ENTER)
                time.sleep(3)
                assert row[0] in self.googlePage.GET_TITLE()
                self.googlePage.do_csv_Write()
                self.googlePage.navigateBack()

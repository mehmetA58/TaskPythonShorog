
from selenium.webdriver.common.keys import Keys
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
        self.googlePage.do_search_a_text_on_google(TestData.TEXT_DATA+Keys.ENTER)
        self.googlePage.do_csv_Write()



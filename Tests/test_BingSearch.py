from Config.config import TestData
from Pages.BingPage import BingPage
from Tests.test_base import BaseTest
from selenium.webdriver.common.keys import Keys


class Test_BingSearch(BaseTest):

    def test_visible_bing_page(self):
        self.bingPage = BingPage(self.driver)
        flag = self.bingPage.is_bing_logo_isDisplayed()
        assert flag
        title = self.bingPage.get_title(TestData.BING_PAGE_TITLE)
        assert title == TestData.BING_PAGE_TITLE
        self.bingPage.do_search_a_text_on_bing(TestData.TEXT_DATA + Keys.ENTER)
        self.bingPage.do_csv_Write()

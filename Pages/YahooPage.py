from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


class YahooPage(BasePage):
    SEARCH_BOX = (By.CSS_SELECTOR, "#ybar-sbq")
    LOGO = (By.XPATH, "//a[@id='ybar-logo']")
    RESULT_STATUS = (By.XPATH, "(//h3[@class='title']//a)[2]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.YAHOO_BASE_URL)

    def get_yahoo_page_title(self, title):
        return self.get_title(title)

    def is_yahoo_big_logo_is_displayed(self):
        return self.is_visible(self.LOGO)

    def do_search_a_text_on_yahoo(self, text):
        self.do_send_keys(self.SEARCH_BOX, text)

    def do_csv_Write(self):
        self.csvWrite(self.RESULT_STATUS)

    def assertSearchText(self,text):
        report=self.get_element_text(self.RESULT_STATUS)
        assert self.get_element_text(text) in report
        print("Test PASS")

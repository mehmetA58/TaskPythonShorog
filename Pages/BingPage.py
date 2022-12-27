from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class BingPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#bLogo")
    SEARCH_BOX = (By.XPATH, "//input[@id='sb_form_q']")
    RESULT_STATUS = (By.XPATH, "//span[@class='sb_count']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BING_BASE_URL)

    def get_bing_page_title(self, title):
        return self.get_title(title)

    def is_bing_logo_isDisplayed(self):
        return self.is_visible(self.LOGO)

    def do_search_a_text_on_bing(self, text):
        self.do_send_keys(self.SEARCH_BOX, text)

    def do_csv_Write(self):
        self.csvWrite(self.RESULT_STATUS)

    def assertSearchText(self,text):
        report=self.get_element_text(self.RESULT_STATUS)
        print(self.get_element_text(self.RESULT_STATUS))
        assert self.get_element_text(text) in report
        print("Test PASS")

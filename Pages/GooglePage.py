from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class GooglePage(BasePage):
    SEARCH_BOX = (By.NAME, "q")
    GOOGLE_BIG_LOGO = (By.XPATH, "//img[@alt='Google']")
    RESULT_STATUS = (By.XPATH, "//div[@id='result-stats']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.GOOGLE_BASE_URL)

    def get_google_page_title(self, title):
        return self.get_title(title)

    def is_google_big_logo_is_displayed(self):
        return self.is_visible(self.GOOGLE_BIG_LOGO)

    def do_search_a_text_on_google(self,text):
        self.do_send_keys(self.SEARCH_BOX,text)

    def get_result_amount(self):
        self.get_element_text(self.RESULT_STATUS)

    def do_csv_Write(self):
        self.csvWrite(self.RESULT_STATUS)

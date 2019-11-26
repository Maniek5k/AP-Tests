from selenium.webdriver.common.by import By
from pages.searchpage import SearchPage
from drivermanager import DriverManager


class SearchTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        SearchPage.__init__(self, driver)

    def runTest(self):
        self.services.submit_form_by_xpath(self, self.search_input, self.qweqwe)

        self.services.is_element_visible(self, By.CLASS_NAME, self.alert_warning)

        self.services.clear_element_by_xpath(self, self.search_input)

        self.services.send_keys_by_xpath(self, self.search_input, self.enter)

        self.services.is_element_visible(self, By.CLASS_NAME, self.alert_warning)

        self.services.submit_form_by_xpath(self, self.search_input, self.blouse)

        self.services.is_element_visible(self, By.LINK_TEXT, self.blouse)
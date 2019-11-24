from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import services

from drivermanager import DriverManager


class SearchTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = services.Services
        self.search_input = '//*[@id="search_query_top"]'
        self.enter = Keys.RETURN
        self.alert_warning = 'alert-warning'
        self.blouse = 'Blouse'
        self.alert_success = 'alert-success'
        self.qweqwe = 'qweqwe'

    def runTest(self):
        self.services.submit_form_by_xpath(self, self.search_input, self.qweqwe)

        self.services.is_element_present(self, By.CLASS_NAME, self.alert_warning)

        self.services.clear_element_by_xpath(self, self.search_input)

        self.services.send_keys_by_xpath(self, self.search_input, self.enter)

        self.services.is_element_present(self, By.CLASS_NAME, self.alert_warning)

        self.services.submit_form_by_xpath(self, self.search_input, self.blouse)

        self.services.is_element_present(self, By.LINK_TEXT, self.blouse)
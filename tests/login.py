import unittest

from selenium.webdriver.common.by import By
from utils.drivermanager import DriverManager
from pages.loginpage import LoginPage


class LoginTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        LoginPage.__init__(self, driver)

    def runTest(self):
        # going to login page
        self.driver.get(self.login_page)

        # providing login credentials
        self.services.send_keys_by_xpath(self, self.email_address, self.user_email)

        self.services.send_keys_by_xpath(self, self.pwd_input, self.user_pwd)

        self.services.assert_and_click(self, By.XPATH, self.submit_btn)

        # check if login was successful
        self.services.is_element_visible(self, By.XPATH, self.heading)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.log_out)

if __name__ == '__main__':
    unittest.main()

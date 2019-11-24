import unittest

from selenium.webdriver.common.by import By

import services
from utils.drivermanager import DriverManager


class LoginTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = services.Services
        self.login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.email_address = '//*[@id="email"]'
        self.user_email = 'emailer5k+selenium@gmail.com'
        self.pwd_input = '//*[@id="passwd"]'
        self.user_pwd = '12345'
        self.submit_btn = '//*[@id="SubmitLogin"]'
        self.heading = '//*[@id="center_column"]/h1'

    def runTest(self):
        # going to login page
        self.driver.get(self.login_page)

        # providing login credentials
        self.services.send_keys_by_xpath(self, self.email_address, self.user_email)
        self.services.send_keys_by_xpath(self, self.pwd_input, self.user_pwd)

        self.services.assert_and_click(self, By.XPATH,  self.submit_btn)

        # check if login was successful
        self.services.is_element_present(self, By.XPATH, self.heading)


if __name__ == "__main__":
    unittest.main()

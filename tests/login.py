import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import services
from drivermanager import DriverManager
from services import Services


class LoginTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = Services(self.driver)
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
        services.Services.send_keys_by_xpath(self, self.email_address, self.user_email)
        services.Services.send_keys_by_xpath(self, self.pwd_input, self.user_pwd)

        services.Services.assert_and_click_by_xpath(self, self.submit_btn)

        # check if login was successful
        services.Services.is_element_present(self, self.heading)


if __name__ == "__main__":
    unittest.main()



    #

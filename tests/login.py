import unittest

from selenium.common.exceptions import NoSuchElementException

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
        self.heading = 'h1.page-heading'

    def runTest(self):
        # going to login page
        self.driver.get(self.login_page)

        # providing login credentials
        self.driver.find_element_by_xpath(self.email_address).send_keys(self.user_email)
        self.password = self.driver.find_element_by_xpath(self.pwd_input).send_keys(self.user_pwd)

        self.driver.find_element_by_xpath(self.submit_btn).click()

        # check if login was successful

        try:
            self.driver.find_element_by_css_selector(self.heading)
            self.driver.find_element_by_css_selector('a.logout').click()
            return True
        except NoSuchElementException:
            return False


if __name__ == "__main__":
    unittest.main()
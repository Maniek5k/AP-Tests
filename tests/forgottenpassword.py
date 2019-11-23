import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ForgottenPassword(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to automation practice homepage
        cls.driver.get("http://automationpractice.com/index.php")

    def test_forgotten_password(self):
        # going to login page
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

        # clicking forgot your password link
        self.go_to_forgotten_pwd()

        # providing existing user email
        self.forgot_pwd_mail = self.driver.find_element_by_xpath('//*[@id="email"]')
        self.forgot_pwd_mail.send_keys('emailer5k+selenium@gmail.com')
        self.forgot_pwd_mail.submit()

        # checking password recovery for existing user
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'p.alert-success'))

        # going back to login page
        self.back_to_login = self.driver.find_element_by_css_selector('ul.footer_links > li > a')
        self.back_to_login.click()

        # going to forgotten password page
        self.go_to_forgotten_pwd()

        # providing non existing user email
        self.forgot_pwd_mail = self.driver.find_element_by_xpath('//*[@id="email"]')
        self.forgot_pwd_mail.send_keys('qweqweqweqeeqwe@gmail.com')
        self.forgot_pwd_mail.submit()

        # checking for correct alert message
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'div.alert-danger'))

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    # helper class for element visibility
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def go_to_forgotten_pwd(self):
        self.forgot_pwd = self.driver.find_element_by_link_text('Forgot your password?')
        self.forgot_pwd.click()

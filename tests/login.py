import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to automation practice homepage
        cls.driver.get("http://automationpractice.com/index.php")

    def test_login(self):
        # going to login page
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

        # providing login credentials
        self.email_address = self.driver.find_element_by_xpath('//*[@id="email"]')
        self.email_address.send_keys('emailer5k+selenium@gmail.com')
        self.password = self.driver.find_element_by_xpath('//*[@id="passwd"]')
        self.password.send_keys('12345')
        self.sign_in = self.driver.find_element_by_xpath('//*[@id="SubmitLogin"]')
        self.sign_in.click()

        # check if login was successful
        self.driver.implicitly_wait(5)
        self.account_page = self.driver.current_url
        correct_account_page = 'http://automationpractice.com/index.php?controller=my-account'
        timeout = 5
        try:
            account_page_present = EC.presence_of_element_located((By.ID, 'center_column'))
            WebDriverWait(self.driver, timeout).until(account_page_present)
            self.assertEqual(self.account_page, correct_account_page)
        except TimeoutException:
            print("Loading took too much time!")

        # log out
        self.log_out = self.driver.find_element_by_css_selector('a.logout')
        self.log_out.click()

    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

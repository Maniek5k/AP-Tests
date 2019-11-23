import random
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class NewsletterSubscribe(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to automation practice homepage
        cls.driver.get("http://automationpractice.com/index.php")

    def test_newsletter_subscribe(self):
        self.prefix_created = str(random.randint(0, 99999))
        # trying to set up a new subscription
        self.subscribe_to_newsletter()

        # check for correct subscription
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'p.alert-success'))

        # trying to set up subscription with existing email address
        self.subscribe_to_newsletter()

        # check for correct alert message - subscription exists
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'p.alert-danger'))

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    # newsletter subscription function
    def subscribe_to_newsletter(self):
        self.newsletter_input = self.driver.find_element_by_xpath('//*[@id="newsletter-input"]')
        self.newsletter_input.send_keys(self.prefix_created + '@testmail.com')
        self.newsletter_input.send_keys(Keys.RETURN)

    # helper class for element visibility
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

import random

from selenium.webdriver.common.by import By

import services
from utils.drivermanager import DriverManager


class NewsletterSubscribe(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = services.Services
        self.newsletter_input = '//*[@id="newsletter-input"]'
        self.prefix_created = str(random.randint(0, 99999))
        self.newsletter_mail = self.prefix_created + '@testmail.com'
        self.newsletter_submit = 'submitNewsletter'

    def runTest(self):
        # trying to set up a new subscription
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct subscription
        self.services.is_element_present(self, By.CSS_SELECTOR, 'p.alert-success')

        # trying to set up subscription with existing email address
        self.driver.get("http://automationpractice.com/index.php")
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct alert message - subscription exists
        self.services.is_element_present(self, By.CSS_SELECTOR, 'p.alert-danger')

import random

from selenium.webdriver.common.by import By

import services
from utils.drivermanager import DriverManager


class NewsletterSubTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = services.Services
        self.homepage = 'http://automationpractice.com/index.php'
        self.newsletter_input = '//*[@id="newsletter-input"]'
        self.prefix_created = str(random.randint(0, 99999))
        self.newsletter_mail = self.prefix_created + '@testmail.com'
        self.newsletter_submit = 'submitNewsletter'
        self.alert_success = 'p.alert-success'
        self.alert_danger = 'p.alert-danger'

    def runTest(self):
        # trying to set up a new subscription
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct subscription
        self.services.is_element_present(self, By.CSS_SELECTOR, self.alert_success)

        # trying to set up subscription with existing email address
        self.driver.get(self.homepage)
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct alert message - subscription exists
        self.services.is_element_present(self, By.CSS_SELECTOR, self.alert_danger)
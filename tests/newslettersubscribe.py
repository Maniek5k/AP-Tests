from selenium.webdriver.common.by import By
from utils.drivermanager import DriverManager
from pages.newsletterpage import NewsletterPage


class NewsletterSubTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        NewsletterPage.__init__(self, driver)

    def runTest(self):
        # trying to set up a new subscription
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct subscription
        self.services.is_element_visible(self, By.CSS_SELECTOR, self.alert_success)

        # trying to set up subscription with existing email address
        self.driver.get(self.homepage)
        self.services.send_keys_by_xpath(self, self.newsletter_input, self.newsletter_mail)
        self.services.assert_and_click(self, By.NAME, self.newsletter_submit)

        # check for correct alert message - subscription exists
        self.services.is_element_visible(self, By.CSS_SELECTOR, self.alert_danger)
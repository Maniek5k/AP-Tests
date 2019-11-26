import random
import services


class NewsletterPage:

    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.homepage = 'http://automationpractice.com/index.php'
        self.newsletter_input = '//*[@id="newsletter-input"]'
        self.prefix_created = str(random.randint(0, 99999))
        self.newsletter_mail = self.prefix_created + '@testmail.com'
        self.newsletter_submit = 'submitNewsletter'
        self.alert_success = 'p.alert-success'
        self.alert_danger = 'p.alert-danger'

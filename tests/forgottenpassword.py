from selenium.webdriver.common.by import By

import services
from utils.drivermanager import DriverManager


class ForgotPwdTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.services = services.Services
        self.account_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.forgot_pwd_btn = 'p.lost_password > a'
        self.forgot_pwd_input = '//*[@id="email"]'
        self.forgot_pwd_mail = 'emailer5k+selenium@gmail.com'
        self.forgot_pwd_alert_success = 'p.alert-success'

    def runTest(self):
        self.driver.get(self.account_page)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.forgot_pwd_btn)

        self.services.submit_form_by_xpath(self, self.forgot_pwd_input, self.forgot_pwd_mail)

        self.services.is_element_present(self, By.CSS_SELECTOR, self.forgot_pwd_alert_success)
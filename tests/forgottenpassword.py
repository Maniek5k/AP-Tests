from selenium.webdriver.common.by import By
from utils.drivermanager import DriverManager
from pages.forgottenpwdpage import ForgottenPwdPage


class ForgotPwdTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        ForgottenPwdPage.__init__(self, driver)

    def runTest(self):
        self.driver.get(self.account_page)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.forgot_pwd_btn)

        self.services.submit_form_by_xpath(self, self.forgot_pwd_input, self.forgot_pwd_mail)

        self.services.is_element_visible(self, By.CSS_SELECTOR, self.forgot_pwd_alert_success)
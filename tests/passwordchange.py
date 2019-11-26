from selenium.webdriver.common.by import By
from drivermanager import DriverManager
from pages.pwdchangepage import PassChangePage


class PwdChangeTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        PassChangePage.__init__(self, driver)

    def runTest(self):

        def pwdEdit(self):
            self.driver.get(self.login_page)

            self.services.send_keys_by_xpath(self, self.email_address, self.change_password_email)

            self.services.send_keys_by_xpath(self, self.pwd_input, self.change_password_pwd)

            self.services.assert_and_click(self, By.XPATH, self.submit_btn)

        def pwdSubmit(self):
            self.services.assert_and_click(self, By.NAME, self.change_password_submit)

            self.services.is_element_visible(self, By.CSS_SELECTOR, self.change_password_success)

        pwdEdit(self)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.change_password_info)

        self.services.send_keys_by_xpath(self, self.change_password_current, self.change_password_pwd)

        self.services.send_keys_by_xpath(self, self.change_password_new, self.new_password)

        self.services.send_keys_by_xpath(self, self.change_password_confirm, self.new_password)

        pwdSubmit(self)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.change_password_back)

        self.services.assert_and_click(self, By.CSS_SELECTOR, self.change_password_info)

        self.services.send_keys_by_xpath(self, self.change_password_current, self.new_password)

        self.services.send_keys_by_xpath(self, self.change_password_new, self.change_password_pwd)

        self.services.send_keys_by_xpath(self, self.change_password_confirm, self.change_password_pwd)

        pwdSubmit(self)








import random

from selenium.webdriver.common.by import By

from drivermanager import DriverManager
from pages.createaccpage import CreateAccPage

class CreateAccTest(DriverManager):

    def __init__(self, driver):
        super().__init__()
        CreateAccPage.__init__(self, driver)

    def runTest(self):
        self.driver.get(self.create_acc_login_page)

        self.services.submit_form_by_xpath(self, self.create_acc_mail_input, self.create_acc_mail)

        self.services.assert_and_click(self, By.XPATH, self.create_acc_radio)

        self.services.send_keys_by_xpath(self, self.create_acc_first_name, self.create_acc_data)

        self.services.send_keys_by_xpath(self, self.create_acc_last_name, self.create_acc_data)

        self.services.send_keys_by_xpath(self, self.create_acc_pwd, self.create_acc_postal_code)

        self.services.send_keys_by_xpath(self, self.create_acc_address_first, self.create_acc_data)

        self.services.send_keys_by_xpath(self, self.create_acc_address_last, self.create_acc_data)

        self.services.send_keys_by_xpath(self, self.create_acc_address, self.create_acc_data)

        self.services.send_keys_by_xpath(self, self.create_acc_city, self.create_acc_data)

        self.services.assert_and_click(self, By.XPATH, self.create_acc_state)

        self.services.send_keys_by_xpath(self, self.create_acc_zip, self.create_acc_postal_code)

        self.services.send_keys_by_xpath(self, self.create_acc_mobile, self.create_acc_phone_no)

        self.services.is_element_visible(self, By.CSS_SELECTOR, self.create_acc_my_acc)
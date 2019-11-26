import random

import services

class CreateAccPage:

    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.create_acc_login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.create_acc_mail_input = '// *[ @ id = "email_create"]'
        self.create_acc_radio = '//*[@id="id_gender1"]'
        self.create_acc_first_name = '//*[@id="customer_firstname"]'
        self.create_acc_last_name = '//*[@id="customer_lastname"]'
        self.create_acc_pwd = '//*[@id="passwd"]'
        self.create_acc_address_first = '//*[@id="firstname"]'
        self.create_acc_address_last = '//*[@id="lastname"]'
        self.create_acc_address = '//*[@id="address1"]'
        self.create_acc_city = '//*[@id="city"]'
        self.create_acc_state = '//*[@id="id_state"]'
        self.create_acc_zip = '//*[@id="postcode"]'
        self.create_acc_mobile = '//*[@id="phone_mobile"]'
        self.create_acc_submit = '//*[@id="submitAccount"]'
        self.create_acc_my_acc = 'h1.page-heading'

        self.prefix_created = str(random.randint(0, 99999))
        self.create_acc_mail = self.prefix_created + '@testmail.com'
        self.create_acc_data = 'tester'
        self.create_acc_postal_code = '12345'
        self.create_acc_phone_no = '123123123'


import services


class PassChangePage:
    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.change_password_email = "emailer5k+pwd@gmail.com"
        self.change_password_pwd = '12345'
        self.new_password = '54321'
        self.email_address = '//*[@id="email"]'
        self.pwd_input = '//*[@id="passwd"]'
        self.submit_btn = '//*[@id="SubmitLogin"]'
        self.change_password_info = 'i.icon-user'
        self.change_password_current = '//*[@id="old_passwd"]'
        self.change_password_new = '//*[@id="passwd"]'
        self.change_password_confirm = '//*[@id="confirmation"]'
        self.change_password_submit = 'submitIdentity'
        self.change_password_success = 'p.alert-success'
        self.change_password_back = 'ul.footer_links > li > a'
import services


class ForgottenPwdPage:

    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.account_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.forgot_pwd_btn = 'p.lost_password > a'
        self.forgot_pwd_input = '//*[@id="email"]'
        self.forgot_pwd_mail = 'emailer5k+selenium@gmail.com'
        self.forgot_pwd_alert_success = 'p.alert-success'

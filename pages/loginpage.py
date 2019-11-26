import services


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.login_page = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
        self.user_email = 'emailer5k+selen@gmail.com'
        self.user_pwd = '12345'
        self.email_address = '//*[@id="email"]'
        self.pwd_input = '//*[@id="passwd"]'
        self.submit_btn = '//*[@id="SubmitLogin"]'
        self.heading = '//*[@id="center_column"]/h1'
        self.log_out = 'a.logout'

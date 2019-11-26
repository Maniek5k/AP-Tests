import services
from selenium.webdriver.common.keys import Keys


class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.services = services.Services
        self.search_input = '//*[@id="search_query_top"]'
        self.enter = Keys.RETURN
        self.alert_warning = 'alert-warning'
        self.blouse = 'Blouse'
        self.alert_success = 'alert-success'
        self.qweqwe = 'qweqwe'

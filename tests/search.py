import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to automation practice homepage
        cls.driver.get("http://automationpractice.com/index.php")

    def test_search(self):
        # sending search query without any search keyword
        self.search_field = self.driver.find_element_by_xpath('//*[@id="search_query_top"]')
        self.search_field.submit()

        # checking for correct alert displayed
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'p.alert-warning'))

        # search for Blouse
        self.search_field = self.driver.find_element_by_xpath('//*[@id="search_query_top"]')
        self.search_field.send_keys("Blouse")
        self.search_field.submit()

        # check if found product matches search query
        self.product_name = self.driver.find_element_by_xpath('//*[@id="center_column"]/ul/li/div/div[2]/h5/a')
        self.assertEqual(self.product_name.text, "Blouse")

        # search for non existing product
        self.search_field = self.driver.find_element_by_xpath('//*[@id="search_query_top"]')
        self.search_field.clear()
        self.search_field.send_keys("qweqwe")
        self.search_field.submit()

        # check for correct alert message displayed
        self.alert_message = self.driver.find_element_by_xpath('//*[@id="center_column"]/p')
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, 'p.alert-warning'))

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver.quit()

    # helper class for element visibility
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True
import unittest

from selenium import webdriver


class DriverManager(unittest.TestCase):

    def setUp(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to automation practice homepage
        cls.driver.get("http://automationpractice.com/index.php")

    def tearDown(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

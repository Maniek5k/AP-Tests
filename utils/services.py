import logging
import random

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)


class Services:
    def __init__(self, driver):
        self.driver = driver

    def create_random_prefix(self):
        self.prefix_created = str(random.randint(0, 99999))
        return self.prefix_created

    def wait_for_element(self, locator, timeout=20):
        logging.info("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)))

    def is_element_visible(self, how, locator):
        logging.info("# Verifying Element is visible... %s" % locator)
        try:
            self.driver.find_element(how, locator)
            logging.info("# Element is visible: %s" % locator)
        except NoSuchElementException:
            logging.error("# Element '%s' is not visible." % locator)
            self.driver.close()
            return False

    def is_element_present_xpath(self, locator):
        logging.info("# Verifying Element is present... %s" % locator)
        try:
            self.driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            self.driver.close()
            return False
        return True

    def send_keys_by_xpath(self, locator, keys):
        logging.info("# Filling up input field... %s" % locator)
        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)

    def submit_form_by_xpath(self, locator, keys):
        logging.info("# Filling up input field... %s" % locator)
        element = self.driver.find_element_by_xpath(locator)
        element.send_keys(keys)
        element.submit()

    def clear_element_by_xpath(self, locator):
        element = self.driver.find_element_by_xpath(locator)
        element.clear()

    def assert_and_click(self, how, locator):
        logging.info("# Wait for element to appear... %s" % locator)
        ele = self.driver.find_element(how, locator)
        ele.click()

    def get_text_by_xpath(self, locator):
        return self.driver.find_element_by_xpath(locator).text

    def assert_element_present(self, how, locator):
        logging.info("# Verifying Element is present.")
        assert self.is_element_present(how, locator), "Element '%s' should be present." % locator

    def assert_element_is_not_present(self, locator):
        logging.info("# Verifying Element is not present.")
        assert not self.is_element_present(locator), "Element '%s' should not be present." % locator

    def wait_for_element_visible(self, locator, timeout=20):
        logging.info("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_element_invisible(self, locator, timeout=20):
        logging.info("# Wait for element to appear... %s" % locator)
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))

    def assert_element_visibility(self, locator, is_visible=True):
        logging.info("# Verifying Element visibility.")
        assert is_visible == self.is_element_visible(locator), "Element '%s' visibility should be %s." % (
            locator, is_visible)

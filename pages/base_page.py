from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def find_element_by_locator(self, locator):
        return self.driver.find_element(*locator)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locators_text(self, locator_1, i_text):
        method, locator = locator_1
        locator = locator.format(i_text)
        return (method, locator)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])




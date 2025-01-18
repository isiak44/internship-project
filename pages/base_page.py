from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_until_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )

    def wait_until_visible_and_click(self, *locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        ).click()

    def verify_current_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'Expected {expected_url} does not match {actual_url}'

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but got {actual_text}'

    def wait_until_presence_of_elements(self, *locator):
        self.wait.until(
            EC.presence_of_all_elements_located(locator),
            f'Elements by {locator} not present')

    def wait_until_clickable(self, *locator):
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message= f'Element by {locator} not clickable'
        )

    def wait_for_all_element_visible(self, *locator):
        return self.wait.until(
            EC.visibility_of_all_elements_located(locator),
            message= f'Elements by {locator} not visible'
        )
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    HOME_PAGE = 'https://soft.reelly.io/'
    SIGN_IN_HEADER = (By.CSS_SELECTOR, '.form-header')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button')
    MY_DEALS_BTN = (By.CSS_SELECTOR, "[href='/deals'].menu-button-block")

    def open_home_page(self):
        self.open_url(self.HOME_PAGE)
        self.wait_until_visible(*self.SIGN_IN_HEADER)

    def login_credentials(self):
        self.find_element(*self.EMAIL_FIELD).send_keys('<Email>')
        self.find_element(*self.PASSWORD_FIELD).send_keys('<Password>')
        self.click(*self.LOGIN_BTN)




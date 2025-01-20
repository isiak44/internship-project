from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    HOME_PAGE = 'https://soft.reelly.io/'
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email-2')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#field')
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button')
    MY_DEALS_BTN = (By.CSS_SELECTOR, "[href='/deals'].menu-button-block")

    def open_home_page(self):
        self.open_url(self.HOME_PAGE)
        self.wait_until_clickable(*self.LOGIN_BTN)
        sleep(3)

    def login_credentials(self):
        self.input_text('EMAIL', *self.EMAIL_FIELD)
        self.input_text('PASSWORD', *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BTN)




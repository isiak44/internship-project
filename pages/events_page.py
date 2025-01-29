from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class EventsPage(BasePage):
    COMPANY_BTN = (By.CSS_SELECTOR, "div [href='/market-companies'][class*='menu-text']")

    def click_company_btn(self):
        self.click(*self.COMPANY_BTN)

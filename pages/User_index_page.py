from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class IndexPage(BasePage):
    MARKET_BTN = (By.CSS_SELECTOR, "div [href='/market-companies'].menu-button-block")
    EVENTS_BTN = (By.CSS_SELECTOR, ".menu-mobile [href='/calendar']")


    def click_market_btn(self):
        self.wait_until_visible_and_click(*self.MARKET_BTN)

    def click_events_btn(self):
        self.click(*self.EVENTS_BTN)

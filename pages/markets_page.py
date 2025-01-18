from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MarketPage(BasePage):
    MARKET_PG_URL = 'https://soft.reelly.io/market-companies'
    FILTER_BTN = (By.CSS_SELECTOR, "div [wized*='{SUBSTRING}']")
    MARKET_CARDS = (By.CSS_SELECTOR, "div.tags-block-3")
    LICENCE_TAG = (By.XPATH, "//*[text()='{SUBSTRING}' and @wized='marketCompanyTagText']")

    def get_card_tag_locator(self, text):
        return self.LICENCE_TAG[0], self.LICENCE_TAG[1].replace('{SUBSTRING}', text)

    def get_fiter_btn_locator(self, text):
        return self.FILTER_BTN[0], self.FILTER_BTN[1].replace('{SUBSTRING}', text)

    def verify_market_pg(self):
        self.verify_current_url(self.MARKET_PG_URL)

    def click_filter_btn(self, selected_filter):
        filter_btn = self.get_fiter_btn_locator(selected_filter)
        self.click(*filter_btn)

    def verify_all_cards_tag(self, selected_tag):
        product_cards = self.wait_for_all_element_visible(*self.MARKET_CARDS)
        selected_tag = self.get_card_tag_locator(selected_tag)
        for card in product_cards:
            card.find_element(*selected_tag)


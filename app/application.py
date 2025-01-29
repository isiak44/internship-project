from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.markets_page import MarketPage
from pages.User_index_page import IndexPage
from pages.events_page import EventsPage


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.markets_page = MarketPage(self.driver)
        self.User_index_page = IndexPage(self.driver)
        self.events_page = EventsPage(self.driver)
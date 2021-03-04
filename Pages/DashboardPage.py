from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.SchedulePage import SchedulePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, TestData.DASHBOARD_PAGE_TITLE)

    def open_schedule_page(self):
        self.click_element((By.CSS_SELECTOR, ("div.icon-schedule")))
        return SchedulePage(self.driver)




from Config.config import TestData
from Pages.BasePage import BasePage

class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, TestData.DASHBOARD_PAGE_TITLE)

import unittest
import Logger.Logger as L
from Config.config import TestData
from Tests.TestBase import TestBase
from Pages.LoginPage import LoginPage

class LoginTest(TestBase):

    def test_login(self):
        L.logging.info("##################### Test - " + self._testMethodName + " - Started #####################")
        L.logging.info("Logging in with email: " + TestData.EMAIL + ", password: " + TestData.PASSWORD)
        login_page = LoginPage(self.driver)
        L.logging.info("Open page: " + TestData.DASHBOARD_PAGE_TITLE)
        dashboard_page = login_page.log_in(TestData.EMAIL, TestData.PASSWORD)

if __name__ == "__main__":
        unittest.main()
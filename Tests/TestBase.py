import unittest
import Logger.Logger as L
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.options import Options
from Pages.LoginPage import LoginPage


class TestBase(unittest.TestCase):

        @classmethod
        def setUp(cls):
            L.logging.info("********************** Set Up **********************")
            cls.options = Options()
            cls.options.add_argument("--start-maximized")
            cls.options.add_argument("--disable-notifications")
            cls.options.add_argument("--incognito")
            cls.driver = webdriver.Chrome(options=cls.options, executable_path=TestData.CHROME_EXECUTABLE_PATH)
            cls.driver.implicitly_wait(5)
            L.logging.info("Navigate to Login page: " + TestData.BASE_URL)
            cls.driver.get(TestData.BASE_URL)
            cls.driver.implicitly_wait(5)


        @classmethod
        def tearDown(cls):
            L.logging.info("********************** Test finished - Tear Down **********************")
            cls.driver.quit()








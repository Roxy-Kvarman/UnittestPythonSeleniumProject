
from Pages.DashboardPage import DashboardPage
from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, TestData.LOGIN_PAGE_TITLE)

    def log_in(self, email, password):
        self.click_element((By.XPATH, ("//a[text()='Sign In']")))
        self.click_element((By.XPATH, ("//a[text()='Sign in with email']")))
        email_field = self.driver.find_element(By.XPATH, ("//input[@name='email']"))
        self.insert_text(email_field, email)
        password_field = self.driver.find_element(By.XPATH, ("//input[@name='password']"))
        self.insert_text(password_field, password)
        self.click_element((By.XPATH, ("//button[text()='Sign in']")))
        return DashboardPage(self.driver)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Logger.Logger as L



class BasePage:
    def __init__(self, driver, page_title):
        self.driver = driver
        if len(page_title) != 0:
            self.page_title = page_title
            self.verify_page_title(page_title)

    def verify_page_title(self, page_title):
        is_title = WebDriverWait(self.driver, 30).until(EC.title_contains(page_title))
        if not is_title:
            L.logging.error(f'Navigation to page : {page_title} failed. Actual page title: {self.driver.title}')
            raise ValueError

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((by_locator))).click()

    def insert_text(self, element, text):
        element.click()
        element.clear()
        element.send_keys(text)

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class NewSubjectForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "")

    def create_new_subject(self, subject_name, index):
        name_field = self.driver.find_element(By.NAME, ("name"))
        self.insert_text(name_field, subject_name)
        self.click_element((By.XPATH, ("//a[text()='Advanced']")))
        self.click_element((By.CSS_SELECTOR, ("a.menu-btn")))
        menu = self.driver.find_element_by_xpath("//div[@class='menu']")
        selector = f'./ul/li[{index}]'
        color = menu.find_element_by_xpath(selector)
        color.click()
        self.click_element((By.XPATH, ("//span[text()='Save']")))



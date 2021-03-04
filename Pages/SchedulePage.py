from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.Forms.ManageSubjectsForm import ManageSubjectsForm


class SchedulePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, TestData.SCHEDULE_PAGE_TITLE)

    def open_manage_subjects_form(self):
        self.click_element((By.XPATH, ("//a[text()='Manage Subjects']")))
        return ManageSubjectsForm(self.driver)


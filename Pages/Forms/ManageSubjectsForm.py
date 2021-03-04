from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Pages.Forms.NewSubjectForm import NewSubjectForm


class ManageSubjectsForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver, "")

    def open_new_subject_form(self):
        self.click_element((By.XPATH, ("//a[text()='New Subject']")))
        return NewSubjectForm(self.driver)

    def close_on_schedule_page(self):
        self.click_element((By.XPATH, ("//a[@class='close']/span")))

    def is_subject_exists(self, subject_name):
        subjects = self.driver.find_elements(By.XPATH, ("//div[@class='list-inner ng-scope']/ul/li"))
        subject = next((s for s in subjects if s.text == f'{subject_name}'), None)
        if subject is not None or len(subject) != 0:
            return True
        else:
            return False

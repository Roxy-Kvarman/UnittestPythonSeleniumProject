import Logger.Logger as L
import Helper.Helper as H
from Config.config import TestData
from Tests.TestBase import TestBase
from Pages.LoginPage import LoginPage


class ManageSubjectsTest(TestBase):

    subject_name = "subject_" + H.generator(5)
    color_index = H.generate_random_number(1,10)

    def test_manage_subjects(self):
        L.logging.info("##################### Test - " + self._testMethodName + " - Started #####################")

        L.logging.info("Logging in with email: " + TestData.EMAIL + ", password: " + TestData.PASSWORD)
        login_page = LoginPage(self.driver)

        L.logging.info("Open page: " + TestData.DASHBOARD_PAGE_TITLE)
        dashboard_page = login_page.log_in(TestData.EMAIL, TestData.PASSWORD)

        L.logging.info("Open page: " + TestData.SCHEDULE_PAGE_TITLE)
        schedule_page = dashboard_page.open_schedule_page()

        L.logging.info("Open Manage Subjects Form")
        manage_subjects_form = schedule_page.open_manage_subjects_form()

        L.logging.info("Open New Subject Form")
        new_subject_form = manage_subjects_form.open_new_subject_form()

        L.logging.info(f'Create new subject [{self.subject_name}]')
        new_subject_form.create_new_subject(self.subject_name, self.color_index)

        L.logging.info("Close Manage Subjects Form")
        manage_subjects_form.close_on_schedule_page()

        L.logging.info(f'Verify new subject [{self.subject_name}] is created')
        manage_subjects_form = schedule_page.open_manage_subjects_form()
        is_subject_created = manage_subjects_form.is_subject_exists(self.subject_name)

        H.assert_test(is_subject_created, f'Subject [{self.subject_name}] was not created on Scheduled Page')


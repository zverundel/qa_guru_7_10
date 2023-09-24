from qa_guru_7_10.data import users
from qa_guru_7_10.pages.registration_page import RegistrationPage


def test_successful_student_registration_form(browser_open_url):
    registration_page = RegistrationPage()

    registration_page.open()

    # WHEN
    registration_page.register_user(users.student)

    # THEN
    registration_page.should_register_user(users.student)
import os.path
from selene import browser, be, by, have
import tests


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')

    #WHEN
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_user_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def select_gender(self, value):
        browser.element(f'[value={value}] + label').click()
        return self

    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option').element_by(have.exact_text(month)).click()
        browser.element('.react-datepicker__year-select').all('option').element_by(have.exact_text(year)).click()
        browser.element(f'.react-datepicker__day--00{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def fill_hobby(self, value):
        browser.element('#hobbiesWrapper').element(by.text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(os.path.join(os.path.dirname(tests.__file__), f"resources/{value}")
            ))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)
        return self

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').click()

    def should_register_user(self, *result):
        browser.element('.table').all('td').even.should(
            have.exact_texts(result))
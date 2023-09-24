from qa_guru_7_10.pages.registration_page import RegistrationPage


def test_practice_form(browser_open_url):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    (
        registration_page
        .fill_first_name('Daniil')
        .fill_last_name('Zverev')
        .fill_user_email('test@gmail.ru')
        .select_gender('Male')
        .fill_user_number('1234567890')
        .fill_date_of_birth('1998', 'May', 4)

        .fill_subject('Maths')
        .fill_hobby('Sports')

        .upload_picture('test_picture.jpg')

        .fill_current_address('orehovo-zuevo, parcov, 15')
        .fill_state('NCR')
        .fill_city('Noida')
        .submit()
    )

    # THEN
    registration_page.should_register_user(
                'Daniil Zverev',
                'test@gmail.ru',
                'Male',
                '1234567890',
                '04 May,1998',
                'Maths',
                'Sports',
                'test_picture.jpg',
                'orehovo-zuevo, parcov, 15',
                'NCR Noida')

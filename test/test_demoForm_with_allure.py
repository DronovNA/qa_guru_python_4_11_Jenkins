import os

from selene import browser, be, command, have
import allure


@allure.title("Successful fill form")
def test_successful(setup_browser):
    base_url = "https://demoqa.com/automation-practice-form"

    with allure.step("Открыть главную страницу"):
        browser.open(base_url)

    with allure.step("Ввод имени и фамилии"):
        browser.element("#firstName").should(be.blank).type("Test")
        browser.element("#lastName").should(be.blank).type("Testovich")

    with allure.step("Ввод почтового ящика"):
        browser.element("#userEmail").should(be.blank).type("Test@example.com")

    with allure.step("Выбор пола"):
        browser.element('[for="gender-radio-2"]').should(be.clickable).click()

    with allure.step("Ввод номера телефона"):
        browser.element("#userNumber").should(be.blank).type("89997589856")

    with allure.step("Выбор даты рождения"):
        browser.execute_script("window.scrollBy(0, 500)")
        browser.element("#dateOfBirthInput").should(be.clickable).click()
        browser.element('[value="1998"]').should(be.clickable).click()
        browser.element(
            f".react-datepicker__day--020:not(.react-datepicker__day--outside-month)"
        ).should(be.clickable).click()

    with allure.step("Выбор школьного предмета"):
        browser.element(".subjects-auto-complete__input>input").should(be.blank).type(
            "sci"
        ).press_enter()

    with allure.step("Выбор хобби"):
        browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).perform(
            command.js.click
        )

    with allure.step("Добавление фото"):
        browser.element("#uploadPicture").send_keys(os.getcwd() + "\example.png")

    with allure.step("Ввод адреса проживания"):
        browser.element("#currentAddress").should(be.blank).type("Test test test")
        browser.element("footer").perform(command.js.remove)

    with allure.step("Выбрать государство"):
        browser.element("#state").should(be.clickable).click()
        browser.element('//div[text()="NCR"]').should(be.clickable).click()
        browser.element("#city").should(be.clickable).click()
        browser.element('//div[text()="Delhi"]').should(be.clickable).click()

    with allure.step("Подтвердить форму регистрации"):
        browser.element("#submit").submit()
        browser.element("#example-modal-sizes-title-lg").should(
            have.text("Thanks for submitting the form")
        )

    with allure.step("Проверить заполненные данные"):
        browser.all(".table-responsive td").by(
            have.exact_texts(
                "Test Testovich"
                "Test@example.com"
                "Female"
                "8999758985"
                "01 March,1998"
                "Computer Science"
                "Reading"
                "example.txt"
                "Test test test"
                "NCR Delhi"
            )
        )


# def test_form():
#     test_open(base_url)
#     test_fill_user_initials()
#     test_fill_user_email()
#     test_chose_user_gender()
#     test_fill_user_phone()
#     test_fill_user_date_born()
#     test_fill_user_subject()
#     test_chose_user_hobbies()
#     test_add_img()
#     test_fill_current_address()
#     test_type_state()
#     test_submit_form()
#     test_should_registered_user_with()

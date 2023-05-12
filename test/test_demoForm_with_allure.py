# import allure
# from allure_commons.types import Severity
# from selene import browser, command
# from selene import be, have
# import os
#
# url = "https://demoqa.com/automation-practice-form"
#
# @allure.tag('web')
# @allure.severity(Severity.NORMAL)
# @allure.label('owner', 'Dronov')
# @allure.feature(f'Заполнение формы на DemoQA')
# @allure.story('Лямбда шаги через with allure.step')
# @allure.link(url, name='Testing')
#
# @allure.step ('Открыть главную страницу')
# def test_open(setup_browser):
#     browser.open(url)
#
# @allure.step('Ввод имени и фамилии')
# def test_fill_user_initials():
#     browser.element("#firstName").should(be.blank).type("Test")
#     browser.element("#lastName").should(be.blank).type("Testovich")
# @allure.step('Ввод почтового ящика')
# def test_fill_user_email():
#     browser.element("#userEmail").should(be.blank).type("Test@example.com")
#
# @allure.step('Выбор пола')
# def test_chose_user_gender():
#     browser.element('[for="gender-radio-2"]').should(be.clickable).click()
#
# @allure.step('Ввод номера телефона')
# def test_fill_user_phone():
#     browser.element("#userNumber").should(be.blank).type("89997589856")
#
# @allure.step('Выбор даты рождения')
# def test_fill_user_date_born():
#     browser.execute_script("window.scrollBy(0, 500)")
#     browser.element("#dateOfBirthInput").should(be.clickable).click()
#     browser.element('[value="1998"]').should(be.clickable).click()
#     browser.element(f'.react-datepicker__day--020:not(.react-datepicker__day--outside-month)').should(
#         be.clickable
#     ).click()
#
# @allure.step('Выбор школьного предмета')
# def test_fill_user_subject():
#     browser.element('.subjects-auto-complete__input>input').should(be.blank).type("sci").press_enter()
#
# @allure.step('Выбор хобби')
# def test_chose_user_hobbies():
#     browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).perform(command.js.click)
#
# @allure.step('Добавление фото')
# def test_add_img():
#     browser.element("#uploadPicture").send_keys(os.getcwd() + '\example.png')
#
# @allure.step('Ввод адреса проживания')
# def test_fill_current_address():
#     browser.element("#currentAddress").should(be.blank).type("Test test test")
#     browser.element('footer').perform(command.js.remove)
#
# @allure.step('Выбрать государство')
# def test_type_state():
#     browser.element("#state").should(be.clickable).click()
#     browser.element('//div[text()="NCR"]').should(be.clickable).click()
#     browser.element("#city").should(be.clickable).click()
#     browser.element('//div[text()="Delhi"]').should(be.clickable).click()
#
# @allure.step('Подтвердить форму регистрации')
# def test_submit_form():
#     browser.element("#submit").submit()
#     browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
#
# @allure.step('Проверить заполненные данные')
# def test_should_registered_user_with():
#     browser.all(".table-responsive td").by(
#         have.exact_texts(
#             "Test Testovich"
#             "Test@example.com"
#             "Female"
#             "8999758985"
#             "01 March,1998"
#             "Computer Science"
#             "Reading"
#             "example.txt"
#             "Test test test"
#             "NCR Delhi"
#         )
#     )
#
#
# def test_form(setup_browser):
#     test_open(url)
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
#

import allure
from selene import have, by


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser
    first_name = "Alex"
    last_name = "Egorov"

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element("#firstName").set_value(first_name)
        browser.element("#lastName").set_value(last_name)
        browser.element("#userEmail").set_value("alex@egorov.com")
        browser.element("#genterWrapper").element(by.text("Other")).click()
        browser.element("#userNumber").set_value("1231231230")
        # browser.element("#dateOfBirthInput").click()
        # browser.element(".react-datepicker__month-select").s("July")
        # browser.element(".react-datepicker__year-select").selectOption("2008")
        # browser.element(".react-datepicker__day--030:not(.react-datepicker__day--outside-month)").click()
        browser.element("#subjectsInput").send_keys("Maths")
        browser.element("#subjectsInput").press_enter()
        browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
        # browser.element("#uploadPicture").uploadFromClasspath("img/1.png")
        browser.element("#currentAddress").set_value("Some street 1")
        browser.element("#state").click()
        browser.element("#stateCity-wrapper").element(by.text("NCR")).click()
        browser.element("#city").click()
        browser.element("#stateCity-wrapper").element(by.text("Delhi")).click()
        browser.element("#submit").click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        # browser.element(".table-responsive").should(
        #     have.texts(first_name, last_name, "alex@egorov.com", "Some street 1"))
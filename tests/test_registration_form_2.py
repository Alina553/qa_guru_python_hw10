import pytest
from selene import browser, have, by
from selene.core.command import js
from selenium import webdriver

from demoqa_tests.data.users import User
from demoqa_tests.pages.registration_page import RegistrationPage

browser.config.driver_options = webdriver.ChromeOptions()
browser.config.driver_options.binary_location = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)


def test_success_registration_form():
    registration_page = RegistrationPage()
    student = User(
        first_name="Alina",
        last_name="K",
        email="ayukazeka@gmail.com",
        gender="Female",
        phone_number="8999123212",
        birth_year="2002",
        birth_month="September",
        birth_day="17",
        subject="History",
        hobby="Sports",
        picture="student.jpeg",
        current_adress="Testovaya st. 43-33",
        state="NCR",
        city="Delhi",
    )

    registration_page.open()

    registration_page.register_user(student)

    registration_page.should_have_registered(student)


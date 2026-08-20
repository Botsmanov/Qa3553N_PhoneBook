import time

from conftest import driver
from pages.registration_page import RegistrationPage

VALID_EMAIL = "rahant@gmail.com"
VALID_PASSWORD = "Talito@96"


def test_regis_success(driver):
    registration_page = RegistrationPage(driver)

    registration_page.open_login_form()
    registration_page.fill_email(VALID_EMAIL)
    registration_page.fill_password(VALID_PASSWORD)
    registration_page.submit_reg()
from selenium.webdriver.common.by import By



class RegistrationPage:
    REGIS_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REG_BTN = (By.XPATH,"//button[@name='registration']")
    SIGN_OUT_BTN = (By.XPATH, "//*[text()='Sign Out']")

    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.REGIS_NAV_LINK).click()

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def submit_reg(self):
        self.driver.find_element(*self.REG_BTN).click()


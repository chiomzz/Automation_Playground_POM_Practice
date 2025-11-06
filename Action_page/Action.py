from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Locators_page.Locators import LoginLocators, NewCustomerLocators, AddCustomerLocators, LogoutLocator


class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def launch_browser(self, url):
        self.driver.get(url)

    def enter_email_address(self, email):
        email_address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.EMAIL_ADDRESS))
        email.send_keys(email)

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        password.send_keys(password)

    def click_submit(self):
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.SUBMIT))
        submit_button.click()





class NewCustomerScreen:
    def __init__(self, driver):
        self.driver = driver
    def click_new_customer(self):
        new_customer_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(NewCustomerLocators.NEW_CUSTOMER))
        new_customer_button.click()




class AddCustomerScreen:
    def __init__(self, driver):
        self.driver = driver

    def enter_customer_email(self, customer_email):
        customer_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.CUSTOMER_EMAIL))
        customer_email.send_keys(customer_email)

    def enter_firstname(self, firstname):
        firstname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.FIRSTNAME))
        firstname.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.LASTNAME))
        lastname.send_keys(lastname)

    def enter_city(self, city):
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.CITY))
        city.send_keys(city)

    def click_state(self):
        state_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.STATE))
        state_button.click()

    def click_selected_state(self):
        selected_state = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.SELECT_STATE))
        selected_state.click()

    def click_gender(self):
        gender_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.GENDER))
        gender_button.click()

    def promotional_list(self):
        promotional_list = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.PROMOTIONAL_LIST))
        promotional_list.click()

    def submit_customer(self):
        submit_customer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerLocators.SUBMIT_CUSTOMER))
        submit_customer.click()




class LogoutScreen:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocator.SIGN_OUT))
        logout_button.click()





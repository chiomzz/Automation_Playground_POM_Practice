from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_ADDRESS = (By.ID, 'email-id')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    SUBMIT = (By.XPATH, '//*[@id="submit-id"]')


class NewCustomerLocators:
    NEW_CUSTOMER = (By.ID, 'new-customer')


class AddCustomerLocators:
    CUSTOMER_EMAIL = (By.CSS_SELECTOR, '#EmailAddress')
    FIRSTNAME = (By.CSS_SELECTOR, '#FirstName')
    LASTNAME = (By.CSS_SELECTOR, '#LastName')
    CITY = (By.CSS_SELECTOR, '#City')
    STATE = (By.CSS_SELECTOR, '#StateOrRegion')
    SELECT_STATE = (By.CSS_SELECTOR, '#StateOrRegion > option:nth-child(46)')
    GENDER = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[6]/input[2]')
    PROMOTIONAL_LIST = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/div[7]/input')
    SUBMIT_CUSTOMER = (By.XPATH, '//*[@id="loginform"]/div/div/div/div/form/button')

class LogoutLocator:
    SIGN_OUT = (By.CSS_SELECTOR, 'body > nav > ul > li > a')




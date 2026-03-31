

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class Login_Page_Class:
    text_username_xpath =  "//input[@placeholder='Username']"
    text_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath =  "//button[@type='submit']"
    button_menu_xpath =  "//p[@class='oxd-userdropdown-name']"
    button_logout_xpath =  "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_username_xpath)))
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(username)

    def Enter_Password(self, password):
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def Click_login(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def Click_Menu(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.button_menu_xpath)))
        self.driver.find_element(By.XPATH, self.button_menu_xpath).click()

    def Click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_xpath).click()

    def verify_login(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.button_menu_xpath)))
            self.driver.find_element(By.XPATH, self.button_menu_xpath).click()
            return "Login Successful"
        except:
             return "Login Failed"









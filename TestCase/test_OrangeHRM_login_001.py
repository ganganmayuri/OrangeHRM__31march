import allure
import pytest

from PageObjects.Login_Page import Login_Page_Class

import Utilities.readConfig as ReadConfig
from Utilities import logger
from Utilities.logger import logger_class
from Utilities.readConfig import ReadConfig


@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_login_001:
    driver = None
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    login_url = ReadConfig.get_login_url()
    logger = logger_class.get_logger()

    def setup_logger(self):
        self.log = logger_class.get_logger()

    @allure.title("Verify OrangeHRM Login Page Title")
    @allure.description("Verify login page title is OrangeHRM")
    @allure.severity(allure.severity_level.CRITICAL)
    # @allure.step
    @allure.link
    @allure.issue
    @allure.testcase
    @allure.feature
    @allure.story
    @allure.tag
    @allure.label
    @pytest.mark.smoke
    @pytest.mark.regresion
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_verify_url_001(self):
        self.log.info("navigation to orangeHRM Login Page")
        self.driver.get(self.login_url)
        self.log.info("OrangeHRM Login Page Loaded")
        if self.driver.title == "OrangeHRM":
            self.log.info("OrangeHRM Login page URL verified")
            self.driver.save_screenshot("screenshots\\test_verify_url_pass.png")
            self.log.info("save screenshots Passed")
            allure.attach.file("screenshots\\test_verify_url_pass.png", name="Pass", attachment_type=allure.attachment_type.PNG)
            assert True
        else:
            self.log.error("Login Failed")
            self.driver.save_screenshot("screenshots\\test_verify_url_Fail.png")
            self.log.info("save screenshots Failed")
            allure.attach.file("screenshots\\test_verify_url_fail.png", name="Fail", attachment_type=allure.attachment_type.PNG)
            assert False
        self.log.info("test_verify_url_001 is completed")

    def test_OrangeHRM_login_002(self):
        self.driver.get(self.login_url)
        lp = Login_Page_Class(self.driver)
        lp.Enter_Username(self.username)
        lp.Enter_Password(self.password)
        lp.Click_login()
        if lp.verify_login():
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_login_pass.png")
            allure.attach.file("screenshots\\test_OrangeHRM_login_pass.png", name="Pass", attachment_type=allure.attachment_type.PNG)
            lp.Click_Menu()
            lp.Click_logout()
            assert True
        else:
            self.driver.save_screenshot("screenshots\\test_OrangeHRM_login_fail.png")
            allure.attach.file("screenshots\\test_OrangeHRM_login_fail.png", name="Pass", attachment_type=allure.attachment_type.PNG)
            assert False



# pytest -v -n=auto --html=Html_Reports\OrangeHRM.html --alluredir=Allure_Reports --browser chrome
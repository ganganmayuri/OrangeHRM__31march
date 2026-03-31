import allure
import pytest

from PageObjects.Login_Page import Login_Page_Class

from Utilities.logger import logger_class
from Utilities.readConfig import ReadConfig
from Utilities.XLUtils import XLUtils_class

@pytest.mark.usefixtures("driver_setup")
class Test_OrangeHRM_Login_DDT_002:
    driver = None

    login_url = ReadConfig.get_login_url()
    log = logger_class.get_logger()
    excel_file = ".\\TestData\\OrangeHRM_TestData.xlsx"
    sheet = "Sheet1"


    def test_OrangeHRM_login_DDT_003(self):
        self.log.info("Starting Test: Verify OrangeHRM loging functionality")
        row_count = XLUtils_class.get_row_count(self.excel_file, self.sheet )
        self.log.info(f"Total Rows in excel: {row_count}")
        result = []
        for i in range(2, row_count + 1):
            username = XLUtils_class.read_data(self.excel_file, self.sheet, i, 2)
            password = XLUtils_class.read_data(self.excel_file, self.sheet, i, 3)
            excepted_result = XLUtils_class.read_data(self.excel_file, self.sheet, i, 4)
            self.log.info(f"TestData: Username= {username}, Password= {password}, Excepted_Result = {excepted_result}")
            self.log.info("Navigating to OrangeHRM Login Page")
            self.driver.get(self.login_url)
            self.log.info("OrangeHRM login page loaded")
            lp = Login_Page_Class(self.driver)
            lp.Enter_Username(username)
            lp.Enter_Password(password)
            lp.Click_login()

            if lp.verify_login() == "Login Successful":
                self.log.info(f"Login Successful for username= {username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_login_DDT_003_pass_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_login_DDT_003_pass_{username}.png", name=f"test_OrangeHRM_login_DDT_003_pass_{username}", attachment_type= allure.attachment_type.PNG)
                lp.Click_Menu()
                lp.Click_logout()
                actual_result = "Login Successful"
            else:
                self.log.error(f"Login failed for Username={username}")
                self.driver.save_screenshot(f"screenshots\\test_OrangeHRM_login_DDT_003_fail_{username}.png")
                allure.attach.file(f"screenshots\\test_OrangeHRM_login_DDT_003_fail_{username}.png", name=f"test_OrangeHRM_login_DDT_003_fail_{username}", attachment_type=allure.attachment_type.PNG)
                actual_result = "Login Failed"

            if actual_result == excepted_result:
                self.log.info(f"test pass for Username={username}")
                test_status = "Pass"
                result.append("Pass")
            else:
                self.log.error(f"Test failed for username={username}")
                test_status = "Fail"
                result.append("Fail")
            XLUtils_class.write_data(self.excel_file, self.sheet, i, 5, test_status)
        self.log.info(f"Test Result: {result}")

        assert "Fail" not in result
        self.log.info("test_OrangeHRM_login_DDT_003 test completed")
        self.log.info("=============================================")


# pytest -v -n=auto --html=Html_Reports\OrangeHRM.html --alluredir=Allure_Reports --browser chrome
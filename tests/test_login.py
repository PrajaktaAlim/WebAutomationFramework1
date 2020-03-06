# Run project as below:
#$F:\Prajakta\Python\Programs\Udemy_Selenium_Python>python -m pytest
#from selenium import webdriver
#from WebAutomationFramework1.pages.login_page import Login_Page
#from WebAutomationFramework1.pages.home_page import Home_Page
from login import Login_Page
from home import Home_Page
from WebAutomationFramework1.utils import utils
#import pytest
import allure
import moment

#@pytest.mark.usefixtures("setup") -- Not necessary
class Test_Login:
    # @pytest.fixture(scope="class")
    # def setup(self):
    #     global driver
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.implicitly_wait(7)
    #     yield
    #     driver.quit()

    def test_login(self, chrome_browser):
        chrome_browser.get(utils.URL)
        login = Login_Page(chrome_browser)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()
        assert chrome_browser.title == "OrangeHRM"

    def test_logout(self, chrome_browser):
        homePg = Home_Page(chrome_browser)
        try:
            homePg.click_welcome()
            homePg.click_logout()
            assert chrome_browser.title == "OrangeHR"
        except AssertionError as ae:
            print("Assertion error occurred")
            #Get current time
            current_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S")
            #Get name of test function running currently
            test_name = utils.whoami()
            #Concat above strings to form the name of the screenshot
            screenshot_name = test_name + "_" + current_time
            allure.attach(chrome_browser.get_screenshot_as_png(), name=screenshot_name, attachment_type = allure.attachment_type.PNG)
            #To store the screenshot locally
            chrome_browser.get_screenshot_as_file("F:/Prajakta/Python/Programs/Udemy_Selenium_Python/WebAutomationFramework1/screenshots/" + screenshot_name + ".png")
            print(ae)
            raise


# if __name__ == "__main__":
#     pytest.main()

class Home_Page:
    welcome_link = "welcome"
    logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_linktext)

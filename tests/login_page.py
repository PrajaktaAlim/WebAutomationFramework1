class Login_Page:
    username_input_id = "txtUsername"
    password_input_id = "txtPassword"
    login_button_id = "btnLogin"

    def __init__(self, driver):
        self.driver = driver


    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_input_id).clear()
        self.driver.find_element_by_id(self.username_input_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click()
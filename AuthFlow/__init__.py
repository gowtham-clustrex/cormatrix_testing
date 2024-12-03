from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *


class LoginFlow:
    def __init__(self, driver: WebDriver) -> None:
        try:
            self.driver = driver
            self.username_and_password()
            Btn_press(self.driver, "Login")
        except Exception as e:
            print(e)

    def username_and_password(self):
        try:
            # username input
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.EditText[@text="Enter your user name"]',
                    )
                )
            ).send_keys(username)
            # password input
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (
                        AppiumBy.XPATH,
                        '//android.widget.EditText[@text="Enter your password"]',
                    )
                )
            ).send_keys(password)
        except TimeoutException or NoSuchElementException as e:
            print("Error is ", e)

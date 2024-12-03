from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *


class TabSwitching:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.open_all_tab()
        self.logout_user()

    def open_all_tab(self):
        tab_list = ["Home", "Notifications", "Schedule", "My Profile"]
        for tab in tab_list:
            Btn_press(self.driver, tab)
            sleep(4)

    def logout_user(self):
        sleep(3)
        Btn_press(self.driver, "Logout")

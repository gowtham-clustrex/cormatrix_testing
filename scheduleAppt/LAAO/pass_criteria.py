# PASS Criteria

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *


class PASSCriteria:
    def __init__(self, driver: WebDriver) -> None:
        try:
            self.driver = driver
            self.open_tab()
            self.form_handler()
            print("PASS Criteria pass")
        except Exception as e:
            print(e)
            print("PASS Criteria fail")

    def open_tab(self):
        Btn_press(self.driver, "PASS Criteria")

    def form_handler(self):
        Btn_press(self.driver, "31")
        get_next_element_from_text(self.driver, "Position").click()
        get_next_element_from_text(self.driver, "Anchor").click()
        self.driver.swipe(500, 1900, 500, 1400, 200)
        get_next_element_from_text(self.driver, "0°").send_keys("20")
        get_next_element_from_text(self.driver, "45°").send_keys("20")
        get_next_element_from_text(self.driver, "90°").send_keys("20")
        get_next_element_from_text(self.driver, "135°").send_keys("20")
        Btn_press(self.driver, "Leak")
        get_next_element_from_text(self.driver, "Leak Value (mm)").send_keys(20)
        Btn_press(self.driver, "No Leak")
        self.driver.swipe(500, 1100, 500, 1900, 200)
        if save_Btn_element(self.driver).is_enabled:
            save_Btn_element(self.driver).click()

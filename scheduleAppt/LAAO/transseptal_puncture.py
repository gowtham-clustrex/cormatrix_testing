from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
import random
from utils import *


class transseptalPuncture:
    def __init__(self, driver: WebDriver) -> None:
        try:
            self.driver = driver
            self.open_tab()
            self.fill_form()
            print("transseptalPuncture was passed")
        except Exception as e:
            print("Error is ", e)
            print("transseptalPuncture was failed")

    def get_all_text_element(Self):
        sleep(5)
        scroll_view = Self.driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.ScrollView[@resource-id="undefined.modal.list"]',
        )
        text_elements = scroll_view.find_elements(
            AppiumBy.XPATH, "//android.widget.TextView"
        )
        return text_elements

    def select_picker_value(self):
        sleep(4)
        list_element = self.get_all_text_element()
        ele = random.choice(list_element)
        ele.click()
        sleep(2)

    def open_tab(self):
        Btn_press(self.driver, "Transseptal Puncture")

    def fill_form(self):
        get_next_element_from_text(self.driver, "Access Sheath").click()
        self.select_picker_value()
        get_next_element_from_text(self.driver, "ACT (sec)").send_keys("400")
        get_next_element_from_text(self.driver, "Transseptal Access System").click()
        self.select_picker_value()
        get_next_element_from_text(self.driver, "TSP Recross").click()
        get_next_element_from_text(self.driver, "Atrial Septostomy Performed").click()
        sleep(3)
        self.driver.swipe(500, 1900, 500, 1400, 200)
        get_next_element_from_text(self.driver, "TSP Imaging").click()
        self.select_picker_value()
        get_next_element_from_text(self.driver, "Final TSP Location").click()
        self.select_picker_value()
        self.driver.swipe(500, 1900, 500, 1400, 200)
        get_next_element_from_text(
            self.driver, "Heparin Administered (units/mL)"
        ).click()
        self.driver.swipe(500, 1100, 500, 1900, 200)
        if save_Btn_element(self.driver).is_enabled:
            save_Btn_element(self.driver).click()

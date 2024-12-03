from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
import random
from utils import *


class Anesthesia:
    def __init__(self, driver: WebDriver):
        try:
            self.driver = driver
            self.open_anesthesia()
            self.general_handler()
            self.mac_handler()
            print("Anesthesia test pass")
        except Exception as e:
            print("Error", e)

    def open_anesthesia(self):
        Btn_press(self.driver, "Anesthesia")

    def general_handler(self):
        Btn_press(self.driver, "General")
        self.enter_ice_value()
        self.enter_tee_value()

    def mac_handler(self):
        Btn_press(self.driver, "MAC")
        self.enter_ice_value()
        self.enter_tee_value()

    def enter_tee_value(self):
        Btn_press(self.driver, "TEE")
        input_ele = get_next_element_from_text(
            self.driver, "Left Atrial Pressure (mmHg)"
        ).send_keys(20)
        data = get_next_element_from_text(self.driver, "Fluid bolus (mL)")
        data.click()
        list_element = self.get_all_text_element()
        ele = random.choice(list_element)
        ele.click()
        sleep(5)
        if save_Btn_element(self.driver).is_enabled():
            save_Btn_element(self.driver).click()

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

    def enter_ice_value(self):
        Btn_press(self.driver, "ICE")
        input_ele = get_next_element_from_text(self.driver, "ICE Catheter Type")
        input_ele.click()
        list_element = self.get_all_text_element()
        ele = random.choice(list_element)
        ele.click()
        sleep(4)
        input_ele2 = get_next_element_from_text(
            self.driver, "Left Atrial Pressure (mmHg)"
        )
        input_ele2.send_keys("50")
        data = get_next_element_from_text(self.driver, "Fluid bolus (mL)")
        data.click()
        list_element = self.get_all_text_element()
        ele = random.choice(list_element)
        ele.click()
        sleep(5)

        if save_Btn_element(self.driver).is_enabled():
            save_Btn_element(self.driver).click()

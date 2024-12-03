# Fluoroscopy & Contrast

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *


class Fluoroscopy:
    def __init__(self, driver: WebDriver) -> None:
        try:
            self.driver = driver
            self.open_tab()
            self.form_handler()
            print("Fluoroscopy & Contrast was passed ")
        except Exception as e:
            print(e)
            print("Fluoroscopy & Contrast was failed")

    def open_tab(self):
        Btn_press(self.driver, "Fluoroscopy & Contrast")

    def form_handler(self):
        get_next_element_from_text(self.driver, "Creatinine Value (mg/dL)").send_keys(
            "2.3"
        )
        get_next_element_from_text(self.driver, "Fluoro time (min)").send_keys("20")
        get_next_element_from_text(self.driver, "Fluoro total (mGy)").send_keys("890")
        get_next_element_from_text(self.driver, "Total Contrast (mL)").send_keys("890")
        if save_Btn_element(self.driver).is_enabled:
            save_Btn_element(self.driver).click()

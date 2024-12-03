from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *


class Anatomy:
    def __init__(self, driver: WebDriver):
        try:
            self.driver = driver
            self.Open_anatomy_tab()
            self.click_different_element()
            print("Anatomy Test Pass")
        except Exception as e:
            print("Error is", e)
            print("Anatomy Test Fails")

    def Open_anatomy_tab(self):
        Btn_press(self.driver, "LAA Anatomy")

    def click_different_element(self):
        list_data = ["Windsock", "Cactus", "Chicken Wing", "Cauliflower"]
        for data in list_data:
            print("helle", data)
            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, data).click()
            save_element = save_Btn_element(self.driver)
            if save_element.is_enabled():
                save_element.click()
                print(data, " was saved ")
                return

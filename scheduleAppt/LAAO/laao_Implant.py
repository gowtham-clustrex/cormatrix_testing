from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
import random
from utils import *


class LAAOImplant:
    def __init__(self, driver: WebDriver) -> None:
        try:
            self.driver = driver
            self.open_tab()
            self.form_handler()
            print("LAAO Implant is passed")

        except Exception as e:
            print(e)
            print("LAAO Implant is failed")

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
        Btn_press(self.driver, "LAAO Implant")

    def form_handler(self):
        sleep(3)
        get_next_element_from_text(self.driver, "Access Sheath").click()
        self.select_picker_value()
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Type")'
        ).click()
        self.select_picker_value()
        self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Size")'
        ).click()
        self.select_picker_value()
        get_next_element_from_text(self.driver, "Suitability Tug").click()
        recapture = get_next_element_from_text(self.driver, "Partial Recaptures")
        recapture.click()
        # if get_text_from_element(recapture).lower() == "yes":
        #     get_next_element_from_text(
        #         self.driver, "Number of partial recaptures"
        #     ).send_keys("20")
        #     get_next_element_from_text(self.driver, "Type of manipulations").send_keys(
        #         "20"
        #     )
        self.driver.swipe(500, 1900, 500, 1400, 200)
        device_deployed = get_next_element_from_text(
            self.driver, "Device Deployed in Body"
        )
        device_deployed.click()
        # if get_text_from_element(device_deployed).lower() == "no":
        # get_next_ele(device_deployed).send_keys("test")
        self.driver.swipe(500, 1900, 500, 1400, 200)

        case_abort = get_next_element_from_text(self.driver, "Case Aborted")
        case_abort.click()
        # if get_text_from_element(case_abort).lower() == "yes":
        #     get_next_ele(case_abort).send_keys("test")
        product = get_next_element_from_text(self.driver, "Product Chargable")
        product.click()
        # if get_text_from_element(product).lower() == "no":
        #     get_next_ele(product).send_keys("test")
        self.driver.swipe(500, 1100, 500, 1900, 200)
        if save_Btn_element(self.driver).is_enabled:
            save_Btn_element(self.driver).click()

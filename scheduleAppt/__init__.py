from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *
from scheduleAppt.LAAO import LAAOProcedure


class openSlot:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.open_schedule()
        self.open_schedule_detail()
        LAAOProcedure(driver)

    def open_schedule(self):
        try:
            ele = find_element_which_contain_text(self.driver, "Case Total")
            ele.click()
        except Exception as e:
            print(e)

    def open_schedule_detail(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.XPATH,
                    '//android.view.ViewGroup[@content-desc="Melissa Grey, 70, Y/O, F,  󱑎, 07:30 AM, Patient Rationale:, Prior GI bleed, Referring Provider:, Suzanne Holroyd, MD, Anticoagulation:, Apixaban"]',
                )
            )
        ).click()

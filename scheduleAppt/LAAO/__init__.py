from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import *
from utils import *
from scheduleAppt.LAAO.anatomy import Anatomy
from scheduleAppt.LAAO.anesthesia import Anesthesia
from scheduleAppt.LAAO.transseptal_puncture import transseptalPuncture
from scheduleAppt.LAAO.laao_Implant import LAAOImplant
from scheduleAppt.LAAO.pass_criteria import PASSCriteria
from scheduleAppt.LAAO.fluoroscopy import Fluoroscopy


class LAAOProcedure:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.open_LAAO_tab()
        Anatomy(driver)
        Anesthesia(driver)
        transseptalPuncture(driver)
        LAAOImplant(driver)
        PASSCriteria(driver)
        Fluoroscopy(driver)

    def open_LAAO_tab(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (
                    AppiumBy.ANDROID_UIAUTOMATOR,
                    'new UiSelector().text("LAAO Procedure")',
                )
            )
        ).click()

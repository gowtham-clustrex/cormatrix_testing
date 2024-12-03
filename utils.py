from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from config import *
from appium.webdriver.webdriver import WebDriver
from time import sleep


def Btn_press(driver: WebDriver, value: str):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, f'//android.widget.TextView[@text="{value}"]')
        )
    ).click()


def save_Btn_element(driver: WebDriver):
    save_element = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description(" 󰘛, Save")'
    )
    return save_element


def get_next_element_from_text(driver: WebDriver, text: str):
    current_element = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))',
    )
    next_element = driver.find_element(
        AppiumBy.XPATH, f'//*[@text="{text}"]/following-sibling::*[1]'
    )
    return next_element


def get_next_element_from_text_two(driver: WebDriver, text: str):
    current_element = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))',
    )
    next_element = driver.find_element(
        AppiumBy.XPATH, f'//*[@text="{text}"]/following-sibling::*[1]'
    )
    return next_element


def get_text_from_element(ele: WebDriver):
    list_ele = ele.find_elements(AppiumBy.XPATH, ".//android.widget.TextView")
    data = [i.text for i in list_ele]
    result = [item for item in data if item.lower() in ["yes", "no"]]
    print(result)
    return result[0]


def scroll_element(driver, text):
    driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))',
    )


def find_element_which_contain_text(driver: WebDriver, text: str):
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView("
                f'new UiSelector().textContains("{text}"))',
            )
        )
    )
    return element


def get_next_ele(current_element):
    # sleep(2)
    # current_element.send_keys("200")
    # return current_element
    # return current_element.find_element(AppiumBy.XPATH, "./following-sibling::*")

    try:
        next_input = current_element.find_element(
            AppiumBy.XPATH, "./following-sibling::android.widget.EditText"
        )
        return next_input
    except:
        print("No next input box found.")
        return None


def get_all_element_from_Scroll_element(driver: WebDriver):
    scroll_view = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (
                AppiumBy.CLASS_NAME,
                "android.widget.ScrollView",
            )
        )
    )
    # scroll_view = driver.find_element(AppiumBy.CLASS_NAME, )
    child_elements = scroll_view.find_elements(AppiumBy.XPATH, ".//*")
    return child_elements

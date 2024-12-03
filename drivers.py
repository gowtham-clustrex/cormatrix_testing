from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from config import *


def get_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.automation_name = "UiAutomator2"
    options.app = f"{os.getcwd()}/apps/app-dev.apk"
    options.app_package = identifier
    options.app_activity = f"{identifier}.MainActivity"
    options.no_reset = True
    options.newCommandTimeout = 300
    driver = webdriver.Remote("http://localhost:4723", options=options)
    return driver, options


def quit_driver(driver, options):
    driver.remove_app(options.app_package)
    driver.quit()

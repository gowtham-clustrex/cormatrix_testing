from AuthFlow import LoginFlow
from scheduleAppt import openSlot
from drivers import get_driver, quit_driver
from time import sleep

if __name__ == "__main__":
    try:
        driver, opt = get_driver()
        LoginFlow(driver)
        openSlot(driver)
        sleep(5)
    except Exception as e:
        print("Error is", e)
    finally:
        print("Test was completed")
        # if driver and opt:
        #     quit_driver(driver, opt)

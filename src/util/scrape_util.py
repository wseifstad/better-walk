import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import constants

SCREENSHOT_DIR = constants.BASE_DIR + "src/screenshots/"

def initChromeDriver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 10000)
    driver.set_page_load_timeout(100000)
    driver.set_window_size(1024, 1024)
    driver.switch_to_window(driver.current_window_handle)
    driver.implicitly_wait(5)
    return driver


def getTrashUrl(address):
    base_url = "http://www1.nyc.gov/assets/dsny/site/collectionSchedule/"
    address_url = address.replace(" ", "%20")
    url = base_url + address_url
    return url


def getTrashDays(address, screenshot=False):
    """
    Creat URL from address
    query the DOT website
    create list of trash days

    Returns list of trash days for address, None otherwise
    """
    try:

        print(address)
        url = getTrashUrl(address)
        driver = initChromeDriver()
        driver.get(url)
        collection_days_table_soup = driver.find_element_by_id("desktopTable")
        collection_days_table_html = collection_days_table_soup.get_attribute('outerHTML')
        collection_days_df = pd.read_html(collection_days_table_html)[0]
        trash_days_df = collection_days_df.iloc[0]
        trash_days_list = []
        for index, value in trash_days_df.iteritems():
            if value == "GARBAGE":
                trash_days_list.append(index)
        if screenshot:
            getTrashDaysScreenshot(driver, address)
        driver.close()
        print("scraped trash days: %s" % trash_days_list)
        print("-"*30)
        return trash_days_list

    except Exception, e:
        print(e)
        print("-"*30)
        driver.close()
        return None


def getTrashDaysScreenshot(driver, address):
    """
    Save screenshot of trash days for address
    Beware, takes a while and screenshots take up ~2GB of space

    Returns True if function screenshotted successfully, False otherwise
    """
    try:
        driver.save_screenshot(SCREENSHOT_DIR + address + '.png')
        print("screenshot success")
        return True

    except Exception, e:
        print(e)
        print("screenshot failed")
        return False

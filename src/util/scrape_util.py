import os.path
import pandas as pd
from geopy.geocoders import GoogleV3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import APIkeys
import constants

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

def getTrashDays(address, driver, screenshot=False):
    """
    Create URL from address
    query the NYDOT website
    create list of trash days

    Returns list of trash days for address, None otherwise
    """
    try:
        print(address)
        url = getTrashUrl(address)
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
        print("scraped trash days: %s" % trash_days_list)
        return trash_days_list
    except Exception, e:
        print(e)
        print("-"*30)
        return None

def getTrashDaysScreenshot(driver, address):
    """
    Save screenshot of trash days for address
    Beware, takes a while and screenshots take up ~2GB of space

    Returns True if function screenshotted successfully, False otherwise
    """
    SCREENSHOT_DIR = constants.BASE_DIR + "src/screenshots/"
    try:
        driver.save_screenshot(SCREENSHOT_DIR + address + '.png')
        print("screenshot success")
        return True

    except Exception, e:
        print(e)
        print("screenshot failed")
        return False

def geocode(address):
    geo = GoogleV3(api_key = APIkeys.geocode_API_key)
    try:
        code = geo.geocode(address)
        print("geocoded: %s, %s" % (code.latitude, code.longitude))
        return code.latitude, code.longitude
    except Exception, e:
        print(e)
        print("geocode failed")
        print("-"*30)
        return None, None

def writeCSV(object_list):
    """create pandas dataframe and write to csv"""
    dict_list = []
    address_df = pd.DataFrame(columns = ["address","lat","lng","trash_days"])
    for address in object_list:
        for day in address.get_trash_days():
            dict_list.append(
                {
                "address": address.get_address(),
                "lat": address.get_lat(),
                "lng": address.get_lng(),
                "trash_day": day
                }
            )
    address_df = pd.DataFrame(dict_list)
    
    #First, check to make sure you are not overwriting a preexisting file.
    CSV_PATH = constants.BASE_DIR + "/src/address_df"
    if os.path.isfile(CSV_PATH + ".csv"):
        suffix = 1
        while os.path.isfile(CSV_PATH + str(suffix) + ".csv"):
            suffix += 1
        address_df.to_csv(CSV_PATH + str(suffix) + ".csv", index = False)
    else:
        address_df.to_csv(CSV_PATH + ".csv", index = False)
    return

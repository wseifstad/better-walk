#Import adress csv, iterate a query on the DOT website, and save info in new csv

import pandas as pd
from requests import get
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import subprocess

# import urllib2
# from bs4 import BeautifulSoup as BS
## BeautifulSoup not working because page runs JavaScript

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
addressList = pd.read_csv("/Users/williamseife/Documents/GitHub/better-walk/Addresses11215.csv")
testurl = "http://www1.nyc.gov/assets/dsny/site/collectionSchedule/160%2015th%20Street,%20Brooklyn,%20NY,%20USA"


def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data

def getTrashDays(test = True):
    '''Iterate through Addresses, query the DOT website, and create list of trash days'''
    
    driver.switch_to_window(driver.current_window_handle)
    
    if test == True:
        driver.get(testurl)
        driver.implicitly_wait(10)
        trash_icons = driver.find_elements_by_class_name("garbageIcon")
    
        ## Attempt to double click the day of the week,
        ## and then copy it to system clipboard via command + c 
        ## In Firefox, the double click does not properly highlight.
        ## In Chrome, the double click highlights, but nothing is copied.
        for icon in trash_icons:
            ActionChains(driver) \
                .move_to_element_with_offset(icon,5,-30) \
                .double_click() \
                .send_keys(Keys.COMMAND,'c') \
                .pause(1) \
                .perform()

        ## Attempt to right click (context_click) the day of the week,
        ## and then copy it to system clipboard via keying arrow down
        ## to the copy option and hitting enter.
        ## the arrows fail to interact with the right click menu options
        ## in both Chrome and Firefox.

        # for icon in trash_icons: 
        #     ActionChains(driver) \
        #        .move_to_element_with_offset(icon,5,-30) \
        #        .context_click() \
        #        .send_keys(Keys.ARROW_DOWN) \
        #        .send_keys(Keys.ARROW_DOWN) \
        #        .send_keys(Keys.RETURN) \
        #        .pause(1) \
        #        .perform()
            print(getClipboardData())

    else:
        for index, row in addressList.iterrows():
            CurrentAddress = str(row["Address"])
            Number, Street, Type = CurrentAddress.split(" ")
            url = "http://www1.nyc.gov/assets/dsny/site/collectionSchedule/" + Number + "%20" + Street + "%20" + Type + "%20Brooklyn%20NY%2011215%20USA"
            driver.get(url)
            driver.implicitly_wait(10)
            trash_icons = driver.find_elements_by_class_name("garbageIcon")
        
            ## Attempt to double click the day of the week,
            ## and then copy it to system clipboard via command + c 
            ## In Firefox, the double click does not properly highlight.
            ## In Chrome, the double click highlights, but nothing is copied.
            for icon in trash_icons:
                ActionChains(driver) \
                    .move_to_element_with_offset(icon,5,-30) \
                    .double_click() \
                    .send_keys(Keys.COMMAND,'c') \
                    .pause(1) \
                    .perform()

            ## Attempt to right click (context_click) the day of the week,
            ## and then copy it to system clipboard via keying arrow down
            ## to the copy option and hitting enter.
            ## the arrows fail to interact with the right click menu options
            ## in both Chrome and Firefox.

            # for icon in trash_icons: 
            #     ActionChains(driver) \
            #        .move_to_element_with_offset(icon,5,-30) \
            #        .context_click() \
            #        .send_keys(Keys.ARROW_DOWN) \
            #        .send_keys(Keys.ARROW_DOWN) \
            #        .send_keys(Keys.RETURN) \
            #        .pause(1) \
            #        .perform()

                print(getClipboardData())
                time.sleep(1)
    
    driver.close()

def getTrashScreenshots(test = True):
    '''Save Screenshots of DOT webpages for picture analysis instead of webpage scraping.
        Beware, takes a while and screenshots take up ~2GB of space'''
    
    driver.switch_to_window(driver.current_window_handle)

    if test == True:
        driver.get(testurl)
        driver.implicitly_wait(10)
        trash_icons = driver.find_elements_by_class_name("garbageIcon")
        driver.save_screenshot('/Users/williamseife/Documents/GitHub/better-walk/screenshots/' + str(CurrentAddress) + '.png')
    else:
        for index, row in addressList.iterrows():
            CurrentAddress = str(row["Address"])
            Number, Street, Type = CurrentAddress.split(" ")
            testurl = "http://www1.nyc.gov/assets/dsny/site/collectionSchedule/132%2015th%20Street,%20Brooklyn,%20NY,%20USA"
            url = "http://www1.nyc.gov/assets/dsny/site/collectionSchedule/" + Number + "%20" + Street + "%20" + Type + "%20Brooklyn%20NY%2011215%20USA"
            driver.get(url)
            driver.implicitly_wait(10)
            driver.save_screenshot('/Users/williamseife/Documents/GitHub/better-walk/screenshots/' + str(CurrentAddress) + '.png')
    
    driver.close()

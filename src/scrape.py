import pandas as pd
import constants
import util.plot_util as plot_util
import util.scrape_util as scrape_util
from model import Address


def run():
    """
    Step 1) Import address csv.
    Step 2) Choose address.
    Step 3) Query addresss url and scrape trash days.
    Step 4) Geocode address to get latitude and longitude.

    creates list of Address objects containing lat,lng, and trash_days
    """

    driver = scrape_util.initChromeDriver()
    object_list = []

    address_list_path = constants.BASE_DIR + "/src/Addresses11215.csv"
    address_list = pd.read_csv(address_list_path)[:2]
    print("searching %s addresses" % len(address_list.index))

    for index, row in address_list.iterrows():
        #Scrape NYDOT website for trash_days
        address = str(row["Address"]) + ", Brooklyn, NY, USA"
        print("checking address %s of %s" % (str(index+1) , len(address_list)))
        trash_days = scrape_util.getTrashDays(address, driver, screenshot=False)
        if trash_days == None:
            continue

        #Geocode address.
        lat,lng = scrape_util.geocode(address)
        if None in (lat,lng):
            continue

        #Initialize Address object and add to list only if scrape and geocode are successful.
        object_list.append(Address(address,lat,lng,trash_days))
    
    #save address dataframe as a CSV file
    scrape_util.writeCSV(object_list)

    driver.close()

if __name__ == "__main__":
    run()

import pandas as pd
import constants
import util.plot_util as plot_util
import util.scrape_util as scrape_util
from model import address_obj

CSV_PATH = constants.BASE_DIR + "src/address_with_days1.csv"

def run():
    """
    Step 1) Import address csv.
    Step 2) Choose address.
    Step 3) Query addresss url for trash days.
    Step 4) Geocode address to get latitude and longitude

    creates list of address objects containing lat,lng, and trash_days
    """

    driver = scrape_util.initChromeDriver()
    object_list = []

    address_list_path = constants.BASE_DIR + "src/Addresses11215.csv"
    address_list = pd.read_csv(address_list_path)[:7]
    print("searching %s addresses" % len(address_list.index))

    for index, row in address_list.iterrows():
        
        #Scrape NYDOT website for trash_days
        address = str(row["Address"]) + ", Brooklyn, NY, USA"
        print("checking address %s of %s" % (str(index+1) , len(address_list)))
        trash_days = scrape_util.getTrashDays(address, driver, screenshot=False)

        #Geocode address to get lat and lng
        if trash_days != None:
            print("geocoding  %s" % (address))
            lat,lng = plot_util.geocode(address)
        else:
            lat,lng = None, None

        if trash_days is not None and lat is not None and lng is not None:
            object_list.append(address_obj(address,lat,lng,trash_days))
            print("object created")
            print("-"*30)
        else:
            print("object failed")
            print("-"*30)

    driver.close()
    
    #print test to show objects in list:
    for i in object_list:
        print(i.get_address())
        print("lat: " + str(i.get_lat()))
        print("lon: " + str(i.get_lng()))
        print("trash_days " + str(i.get_trash_days()))
        print("*"*30)

    


if __name__ == "__main__":
    run()

import pandas as pd
import numpy as np
import constants
import util.scrape_util as scrape_util
from model import Address


def run():
    """
    Step 1) Import address with days csv.
    Step 2) Choose address.
    Step 3) Geocode address to get latitude and longitude.
    Step 4) Save as CSV

    """
    address_list = pd.read_csv("address_with_days.csv")[:]

    #address_list = address_list.assign('lat'=pd.Series(np.zeros(len(address_list.index.get_values())),index=address_list.index))
    #address_list = address_list.assign('lng'=pd.Series(np.zeros(len(address_list.index.get_values())),index=address_list.index))

    lat_dict = {}
    lng_dict = {}
    geocode_dict = {}
    for index, row in address_list.iterrows():
        if row['address'] in geocode_dict:
            lat_dict[index] = geocode_dict[row['address']][0]
            lng_dict[index] = geocode_dict[row['address']][1]
        else:
            lat,lng = scrape_util.geocode(row['address'])
            if 'stop' in (lat,lng):
                print('final index: %s', index-1)
                break
            if None in (lat,lng):
                continue

            geocode_dict[row['address']] = [lat,lng]

            lat_dict[index] = lat
            lng_dict[index] = lng
    

    address_list["lat"] = pd.Series(lat_dict)
    address_list["lng"] = pd.Series(lng_dict)
    
    
    scrape_util.writeGeoCSV(address_list)

if __name__ == "__main__":
    run()

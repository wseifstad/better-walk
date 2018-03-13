import pandas as pd
import util.plot_util as plot_util



address_list = pd.read_csv("src/address_with_days.csv")[:]

def run():
    for day in plot_util.days_of_week:
        lat_list = []
        lon_list = []

        day_list = address_list.address[address_list["trash_day"] == day]
        
        for address in day_list:
            print("%s: geocoding  %s" % (day,address))
            try:
                lat,lon = plot_util.geocode(address)
                lat_list.append(lat)
                lon_list.append(lon)
                print("-"*30)
            except Exception, e:
                print(e)
                print("geocode failed")
                print("-"*30)

        plot_util.scatterPlot_and_writeHTML(day,lat_list,lon_list)

if __name__ == "__main__":
    run()
        

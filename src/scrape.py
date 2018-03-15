import pandas as pd
import util.scrape_util as scrape_util
import constants
import time

start_time = time.time()

CSV_PATH = constants.BASE_DIR + "src/address_with_days1.csv"

def run():
    """
    Step 1) Import address csv.
    Step 2) Choose address.
    Step 3) Query addresss url for trash days.

    Returns trash_df : pandas df with "address" and "trash_day" columns.
    Addresses with multiple trash days are split into a new line for each day.
    """
    trash_days_dict = {}
    test_flag = False
    driver = scrape_util.initChromeDriver()

    if test_flag:
        trash_days_dict = {}
        test_address = "160 15th Street, Brooklyn, NY, USA"
        trash_days = scrape_util.getTrashDays(test_address, driver, screenshot=False)
        trash_days_dict[test_address] = trash_days

    else:
        address_list_path = constants.BASE_DIR + "src/Addresses11215.csv"
        address_list = pd.read_csv(address_list_path)[:10]
        print("searching %s addresses" % len(address_list.index))

        for index, row in address_list.iterrows():
            address = str(row["Address"]) + ", Brooklyn, NY, USA"
            print("checking address %s of %s" % (str(index+1) , len(address_list)))
            print("program has been running for %s seconds" % str(time.time() - start_time))
            trash_days = scrape_util.getTrashDays(address, driver, screenshot=False)
            trash_days_dict[address] = trash_days
        
        ## clear addresses with NoneType trash_days
        clean_dict = {k: v for k, v in trash_days_dict.iteritems() if v is not None} 

        trash_df = pd.DataFrame.from_dict(clean_dict,orient="index") \
            .sort_index() \
            .stack() \
            .reset_index(level=1,drop=True) \
            .reset_index()
        trash_df.columns = ['address','trash_day']

        trash_df.to_csv(CSV_PATH, index = False)
        print("total time = %s seconds" % str(time.time() - start_time))
        driver.close()
        return trash_df
    


if __name__ == "__main__":
    run()

import pandas as pd
import util.scrape_util as scrape_util
import constants

def run():
    """
    Step 1) Import address csv.
    Step 2) Choose address.
    Step 3) Query addresss url for trash days.
    """
    trash_days_list = []
    test_flag = False

    if test_flag:
        trash_days_dict = {}
        test_address = "160 15th Street, Brooklyn, NY, USA"
        trash_days = scrape_util.getTrashDays(test_address, screenshot=True)
        trash_days_dict[test_address] = trash_days
        trash_days_list.append(trash_days_dict)

    else:
        address_list_path = constants.BASE_DIR + "src/Addresses11215.csv"
        address_list = pd.read_csv(address_list_path)[0:3]
        print("searching %s addresses" % len(address_list.index))

        for index, row in address_list.iterrows():
            trash_days_dict = {}
            address = str(row["Address"]) + ", Brooklyn, NY, USA"
            print("checking address %s" % str(index+1))
            trash_days = scrape_util.getTrashDays(address, screenshot=False)
            trash_days_dict[address] = trash_days
            trash_days_list.append(trash_days_dict)


if __name__ == "__main__":
    run()

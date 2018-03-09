# better-walk
Attempt to optimize a walk of a certain distance by avoiding trash, construction, etc.

Currently not functioning. Need different way to select correct day of the week, because copy-paste method does not work in either browser.

Addresses obtained from https://www.melissadata.com/lookups/zipstreet.asp?InData=11215&c=3&l=U   
Address list currently only has numbered streets in 11215 zip code.

Current Dependencies:
1. pandas
2. reqeusts
3. selenium
4. selenium webdriver for Chrome or Firefox (make sure to download in PATH): 
	- Firefox webdriver: https://github.com/mozilla/geckodriver/releases
	- Chrome webdriver: https://sites.google.com/a/chromium.org/chromedriver/downloads

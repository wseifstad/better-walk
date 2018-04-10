# better-walk
Attempt to optimize a walk of a certain distance by avoiding trash set out on the curb.

Current functionality is just a web scrape of the NYDOT website to obtain the trash days for 11215.
No walk optimization, yet.

Addresses obtained from https://www.melissadata.com/lookups/zipstreet.asp?InData=11215&c=3&l=U   
Address list currently only has numbered streets in 11215 zip code.


# Installation

Clone the repo onto your machine with the following command:

$ git clone https://github.com/wseife/better-walk.git


# Dependencies

We use virtualenv to manage dependencies, if you have it installed you can run
the following commands from the root code directory to create the environment and
activate it:

$ virtualenv venv
$ source venv/bin/activate

Then you can run the following to install dependencies:

$ pip install -r requirements.txt

See https://virtualenv.pypa.io/en/stable/ for more information.

In addition, you need to have chromedriver installed in $PATH for selenium to work:

See https://sites.google.com/a/chromium.org/chromedriver/downloads for installation and information.


# Google Maps API key

In order to run the script, you need Google Maps Geocoding and a Google Maps JavaScript API keys.

You can create a project and obtain one for free at the following links:
https://developers.google.com/maps/documentation/geocoding/
https://developers.google.com/maps/documentation/javascript/

Then, create a file "APIkeys.py" in the /src directory with the following structure:

```python
geocode_API_key = "[insert API key]"
javascript_API_key = "[insert API key]"
```

# Usage

The master program script is 'src/scrape.py'. For example:

$ python src/scrape.py

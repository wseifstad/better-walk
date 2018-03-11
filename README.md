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


# Configuration

In order to configure the system you'll need a constants.py file. It should live
in the 'src' folder and its contents should include the following:

BASE_DIR = '/path/to/root/dir/'

Let's explain these in detail:

BASE_DIR is the path to the root code directory on your local machine.


# Usage

The master program script is 'src/scrape.py'. For example:

$ python src/scrape.py

# Tesla Delivery

Script to get the estimated delivery of a Tesla. Will throw out a mac system alert with the result.

## Usage

1. Have Python3 (note the path to use in the cron)
2. Install [pyppeteer](https://pypi.org/project/pyppeteer/) `pip3 install pyppeteer`
3. Fill out the [config.json](config.json)
   1. Url is for the page of the vehicle you're tracking
4. Try running the script `python3 tesla_delivery.py`
5. Create a cron to run the script, this is mine (run at 10am on Monday through Friday)
   1. `0 10 * * 1-5 /usr/local/bin/python3 /Users/tevanc/tesla_delivery/tesla_delivery.py`

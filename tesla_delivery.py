import asyncio
import json
import os

from datetime import date
from pyppeteer import launch

with open(os.path.join(os.path.dirname(__file__), "config.json"), "r") as config_file:
    config = json.loads(config_file.read())

selectors = {
    "username": "#form-input-identity",
    "password": "#form-input-credential",
    "login": "#form-submit-continue",
    "my_order": "#dashboard-product-list > div:nth-child(4) > table > tbody > tr > td.model-name > div > div > a",
    "delivery_date": "#prod-final-deliver-desk-product-info > article:nth-child(2) > div > span > div > h6",
}


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto(config["url"])

    await page.waitForSelector(selectors["username"], timeout=20000)
    await page.type(selectors["username"], config["username"])
    await page.type(selectors["password"], config["password"])
    await page.click(selectors["login"])
    
    await page.waitForSelector(selectors["my_order"], timeout=20000)
    await page.goto(config["url"])
    
    await page.waitForSelector(selectors["delivery_date"], timeout=20000)
    delivery_date = await page.evaluate(
        f"""document.querySelector("{selectors["delivery_date"]}").innerText"""
    )
    os.system(f"osascript -e 'display alert \"{date.today()}\n{delivery_date}\"'")
    await browser.close()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

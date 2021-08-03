import asyncio
import json
import os
import time

from datetime import date
from pyppeteer import launch

timeout = 60000

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
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(config["url"], timeout=timeout)

    await page.waitForSelector(selectors["username"], timeout=timeout)
    time.sleep(2)
    await page.type(selectors["username"], config["username"])
    time.sleep(2)
    await page.type(selectors["password"], config["password"])
    time.sleep(2)
    await page.click(selectors["login"])

    await page.waitForSelector(selectors["my_order"], timeout=timeout)
    await page.goto(config["url"])

    await page.waitForSelector(selectors["delivery_date"], timeout=timeout)
    delivery_date = await page.evaluate(
        f"""document.querySelector("{selectors["delivery_date"]}").innerText"""
    )
    await browser.close()

    alert_text = f"{date.today()}\n{delivery_date}"

    with open(os.path.join(os.path.dirname(__file__), "output.log"), "a") as output_file:
        output_file.write(f"{alert_text}\n")

    os.system(f"osascript -e 'display alert \"{alert_text}\"'")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

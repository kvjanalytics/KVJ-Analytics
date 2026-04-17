import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # open the local html file
        await page.goto("file:///c:/Users/kj%20anand/Downloads/Quiz%20DD/tmp_table.html")
        # take a screenshot of just the table element
        table = page.locator("table")
        await table.screenshot(path="recreational_sales_table.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

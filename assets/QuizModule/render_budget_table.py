import asyncio
from playwright.async_api import async_playwright

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
  body {
    background-color: white;
    font-family: Arial, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }
  table {
    border-collapse: collapse;
    width: 650px;
    font-size: 16px;
  }
  th, td {
    border: 1.5px solid black;
    padding: 8px 12px;
    text-align: left;
  }
  td:last-child, th:last-child {
    text-align: center;
  }
  th {
    font-weight: bold;
    font-size: 18px;
  }
</style>
</head>
<body>

<table>
  <tr>
    <th>Source category</th>
    <th>Spend Category</th>
    <th>Amount</th>
  </tr>
  <tr><td>Total Monthly Budget</td><td>Total Monthly Budget</td><td>1000</td></tr>
  <tr><td>Total Monthly Budget</td><td>Gym Membership</td><td>100</td></tr>
  <tr><td>Total Monthly Budget</td><td>Rent</td><td>200</td></tr>
  <tr><td>Total Monthly Budget</td><td>Food & Entertainment</td><td>700</td></tr>
  <tr><td>Food & Entertainment</td><td>Food cost</td><td>400</td></tr>
  <tr><td>Food & Entertainment</td><td>Entertainment Cost</td><td>300</td></tr>
  <tr><td>Entertainment Cost</td><td>Movie Theater and Play</td><td>200</td></tr>
  <tr><td>Entertainment Cost</td><td>Other</td><td>100</td></tr>
</table>

</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        table = page.locator("table")
        await table.screenshot(path="budget_sankey_table.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

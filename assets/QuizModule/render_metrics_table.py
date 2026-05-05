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
    padding: 20px;
    margin: 0;
  }
  .container {
    padding: 20px;
    background: white;
  }
  table {
    border-collapse: collapse;
    font-size: 14px;
    color: #1e293b;
  }
  th, td {
    border: 1px solid #94a3b8;
    padding: 8px 12px;
    text-align: center;
  }
  th {
    background-color: #f8fafc;
    font-weight: bold;
  }
  .row-label {
    text-align: left;
    font-weight: bold;
    background-color: #f8fafc;
  }
  .metric-row {
    font-style: italic;
    color: #475569;
  }
</style>
</head>
<body>
<div class="container" id="capture">
    <table>
      <tr>
        <th class="row-label">Region</th>
        <th>Quarter 1</th>
        <th>Quarter 2</th>
        <th>Quarter 3</th>
        <th>Quarter 4</th>
      </tr>
      <tr><td class="row-label">North</td><td>25000</td><td>30000</td><td>40000</td><td>50000</td></tr>
      <tr><td class="row-label">South</td><td>35000</td><td>45000</td><td>40000</td><td>55000</td></tr>
      <tr><td class="row-label">East</td><td>35000</td><td>32500</td><td>41000</td><td>52500</td></tr>
      <tr><td class="row-label">West</td><td>34500</td><td>30000</td><td>42500</td><td>55000</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 1</td><td>129500</td><td>137500</td><td>163500</td><td>212500</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 2</td><td>35000</td><td>45000</td><td>42500</td><td>55000</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 3</td><td>25000</td><td>30000</td><td>40000</td><td>50000</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 4</td><td>35000</td><td>30000</td><td>40000</td><td>55000</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 5</td><td>32375</td><td>34375</td><td>40875</td><td>53125</td></tr>
      <tr class="metric-row"><td class="row-label">Metric 6</td><td>34750</td><td>31250</td><td>40500</td><td>53750</td></tr>
    </table>
</div>
</body>
</html>
"""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_content(html_content)
        # Wait a bit for layout
        await page.wait_for_timeout(100)
        elem = page.locator("#capture")
        await elem.screenshot(path="recreated_table.png")
        await elem.screenshot(path="quarterly_sales_metrics.png")
        await elem.screenshot(path="metrics_table2.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

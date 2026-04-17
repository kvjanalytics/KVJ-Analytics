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
    flex-direction: column;
    align-items: center;
    padding: 30px;
    margin: 0;
  }
  table {
    border-collapse: collapse;
    font-size: 16px;
    color: #1e293b;
    margin-bottom: 30px;
  }
  th, td {
    border: 1px solid #1e293b;
    padding: 6px 12px;
    text-align: left;
  }
  th {
    background-color: #badcf0;
    font-weight: bold;
    text-align: center;
  }
  td:last-child {
    text-align: center;
  }
  
  .pivot-table {
    width: 350px;
  }
  .pivot-table th {
    background-color: white;
    font-weight: normal;
  }
  .pivot-table .label-bg {
    background-color: #f7d6af; /* Light orange */
  }
</style>
</head>
<body>
<div id="capture" style="padding: 20px; background: white;">
    <!-- Raw Data Table -->
    <table>
      <tr>
        <th>School</th>
        <th>Class</th>
        <th>Format</th>
        <th>Certified Teachers</th>
      </tr>
      <tr><td>School A</td><td>Networking</td><td>In-Person</td><td>6</td></tr>
      <tr><td>School A</td><td>Networking</td><td>Virtual</td><td>5</td></tr>
      <tr><td>School A</td><td>Data Analytics</td><td>In-Person</td><td>2</td></tr>
      <tr><td>School A</td><td>Data Analytics</td><td>Virtual</td><td>3</td></tr>
      <tr><td>School B</td><td>Networking</td><td>In-Person</td><td>9</td></tr>
      <tr><td>School B</td><td>Networking</td><td>Virtual</td><td>7</td></tr>
      <tr><td>School B</td><td>Data Analytics</td><td>In-Person</td><td>2</td></tr>
      <tr><td>School B</td><td>Data Analytics</td><td>Virtual</td><td>4</td></tr>
    </table>

    <!-- Pivot Table -->
    <table class="pivot-table">
      <tr>
        <td style="border:none"></td>
        <td style="text-align:center">Label 1</td>
        <td style="text-align:center">Label 2</td>
      </tr>
      <tr>
        <td class="label-bg">Label 3</td>
        <td>11</td>
        <td>5</td>
      </tr>
      <tr>
        <td class="label-bg">Label 4</td>
        <td>16</td>
        <td>6</td>
      </tr>
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
        elem = page.locator("#capture")
        await elem.screenshot(path="pivot_table_matching.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

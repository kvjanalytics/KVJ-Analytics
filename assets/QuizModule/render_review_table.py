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
    width: 700px;
    font-size: 16px;
  }
  th, td {
    border: 1px solid black;
    padding: 8px;
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
    <th>Product</th>
    <th>Review Score</th>
    <th>Reviewer ID</th>
    <th>Industry</th>
    <th>Ethnicity</th>
  </tr>
  <tr><td>AX-150</td><td>74</td><td>123</td><td>Education</td><td>Asian</td></tr>
  <tr><td>BK-330</td><td>82</td><td>124</td><td>Finance</td><td>Latino orHispanic</td></tr>
  <tr><td>BK-315</td><td>79</td><td>125</td><td>Health care</td><td>Native Hawaiian or pacific Islander</td></tr>
  <tr><td>CX-290</td><td>86</td><td>126</td><td>Other</td><td>African-American</td></tr>
  <tr><td>BD-250</td><td>61</td><td>127</td><td>Finance</td><td>Other</td></tr>
  <tr><td>CD-140</td><td>35</td><td>128</td><td>Food service</td><td>Caucasian</td></tr>
  <tr><td>AX-310</td><td>84</td><td>129</td><td>Education</td><td>Caucasian</td></tr>
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
        await table.screenshot(path="disaggregation_dataset_v4.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

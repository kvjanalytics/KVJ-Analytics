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
  .container {
    width: 700px;
    border: 1px solid #e2e8f0;
    padding: 20px;
  }
  h2 {
    text-align: center;
    color: #475569;
    margin-top: 0;
  }
  .chart {
    position: relative;
    padding-left: 80px;
    padding-top: 20px;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 10px;
    margin-bottom: 20px;
  }
  .group {
    margin-bottom: 15px;
    position: relative;
  }
  .label {
    position: absolute;
    left: -80px;
    top: 50%;
    transform: translateY(-50%);
    width: 70px;
    text-align: right;
    color: #475569;
    font-size: 14px;
  }
  .bar-container {
    height: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 2px;
  }
  .bar {
    height: 12px;
  }
  .orange { background-color: #f97316; }
  .blue { background-color: #1a6285; }
  
  .axis {
    display: flex;
    justify-content: space-between;
    margin-left: 80px;
    font-size: 12px;
    color: #64748b;
    margin-bottom: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    color: #475569;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 8px;
    text-align: center;
  }
  th { font-weight: normal; }
  td:first-child { text-align: left; }
  
  .legend-item { display: inline-flex; align-items: center; margin-right: 15px; }
  .box { width: 12px; height: 12px; margin-right: 5px; }
  .legend { text-align: center; margin-top: 20px; font-size: 14px; color: #475569;}
</style>
</head>
<body>

<div class="container" id="capture">
  <h2>Online & Instore purchase</h2>
  
  <div class="chart">
    <div class="group">
      <div class="label">Std Dev</div>
      <div class="bar-container">
        <div class="bar orange" style="width: calc(66/250 * 100%)"></div>
        <div class="bar blue" style="width: calc(122/250 * 100%)"></div>
      </div>
    </div>
    <div class="group">
      <div class="label">Mode</div>
      <div class="bar-container">
        <div class="bar orange" style="width: calc(199/250 * 100%)"></div>
        <div class="bar blue" style="width: calc(199/250 * 100%)"></div>
      </div>
    </div>
    <div class="group">
      <div class="label">Median</div>
      <div class="bar-container">
        <div class="bar orange" style="width: calc(190/250 * 100%)"></div>
        <div class="bar blue" style="width: calc(215/250 * 100%)"></div>
      </div>
    </div>
    <div class="group">
      <div class="label">Mean</div>
      <div class="bar-container">
        <div class="bar orange" style="width: calc(188/250 * 100%)"></div>
        <div class="bar blue" style="width: calc(228/250 * 100%)"></div>
      </div>
    </div>
  </div>
  
  <div class="axis">
    <span>$-</span>
    <span>$50</span>
    <span>$100</span>
    <span>$150</span>
    <span>$200</span>
    <span>$250</span>
  </div>
  
  <table>
    <tr>
      <th style="border:none"></th>
      <th>Mean</th>
      <th>Median</th>
      <th>Mode</th>
      <th>Std Dev</th>
    </tr>
    <tr>
      <td><span class="box orange" style="display:inline-block"></span> Instore</td>
      <td>$188</td>
      <td>$190</td>
      <td>$199</td>
      <td>$66</td>
    </tr>
    <tr>
      <td><span class="box blue" style="display:inline-block"></span> Online</td>
      <td>$228</td>
      <td>$215</td>
      <td>$199</td>
      <td>$122</td>
    </tr>
  </table>
  
  <div class="legend">
    <div class="legend-item"><span class="box orange"></span> Instore</div>
    <div class="legend-item"><span class="box blue"></span> Online</div>
  </div>
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
        await elem.screenshot(path="purchase_stats_chart.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

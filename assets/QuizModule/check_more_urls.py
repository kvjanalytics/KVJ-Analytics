import requests

urls = [
    "https://img.icons8.com/color/96/bar-chart.png",
    "https://img.icons8.com/dusk/96/bar-chart.png",
    "https://img.icons8.com/fluency/96/investment.png",
    "https://img.icons8.com/fluency/96/total-sales.png",
    "https://img.icons8.com/fluency/96/increase.png"
]

for url in urls:
    try:
        r = requests.head(url, timeout=5)
        print(f"{url}: {r.status_code}")
    except Exception as e:
        print(f"{url}: {e}")

import requests

urls = [
    "https://img.icons8.com/fluency/96/column-chart.png",
    "https://img.icons8.com/fluency/96/bar-chart.png",
    "https://img.icons8.com/fluency/96/vertical-bar-chart.png",
    "https://img.icons8.com/fluency/96/statistics.png",
    "https://img.icons8.com/fluency/96/funnel-chart.png",
    "https://img.icons8.com/fluency/96/funnel.png",
    "https://img.icons8.com/fluency/96/filter.png",
    "https://img.icons8.com/fluency/96/waterfall-chart.png",
    "https://img.icons8.com/fluency/96/waterfall.png",
    "https://img.icons8.com/fluency/96/staircase.png"
]

for url in urls:
    try:
        r = requests.head(url, timeout=5)
        print(f"{url}: {r.status_code}")
    except Exception as e:
        print(f"{url}: {e}")

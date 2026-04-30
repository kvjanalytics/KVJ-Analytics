import requests
urls = [
    "https://img.icons8.com/color/96/sorting-options.png",
    "https://img.icons8.com/color/96/filter.png",
    "https://img.icons8.com/color/96/slice.png",
    "https://img.icons8.com/color/96/data-in-both-directions.png",
    "https://img.icons8.com/color/96/plus.png",
    "https://img.icons8.com/color/96/cut.png",
    "https://img.icons8.com/color/96/merge.png"
]
for url in urls:
    try:
        r = requests.head(url, timeout=5)
        print(f"{url}: {r.status_code}")
    except Exception as e:
        print(f"{url}: error {e}")

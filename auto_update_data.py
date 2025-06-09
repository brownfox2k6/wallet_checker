import requests, json, os

BASE = "https://etherscan.io/accounts.aspx/GetTableEntriesBySubLabel"
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# headers common
UA = "Mozilla/5.0"


def fetch_exchange(limit=100, start=0):
    sess = requests.Session()
    # initial GET to set cookies
    sess.get("https://etherscan.io/accounts/label/exchange", headers={"User-Agent": UA})
    payload = {
        "labelModel": {"id": "", "label": "exchange", "subCategoryId": 0},
        "dataTableModel": {"draw":1, "columns":[], "order":[{"column":1,"dir":"desc"}],
                            "start": start, "length": limit,
                            "search": {"value": "", "regex": False}}
    }
    hdrs = {
        "User-Agent": UA,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": "application/json; charset=UTF-8",
        "Referer": "https://etherscan.io/accounts/label/exchange",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://etherscan.io"
    }
    res = sess.post(BASE, headers=hdrs, data=json.dumps(payload))
    res.raise_for_status()
    data = res.json().get("d", {})
    return [r["address"].lower() for r in data.get("aaData", [])]


if __name__ == "__main__":
    addrs = fetch_exchange(500)
    path = os.path.join(DATA_DIR, "exchange_whitelist.json")
    with open(path, "w") as f:
        json.dump(sorted(set(addrs)), f, indent=2)
    print(f"Saved {len(addrs)} addresses to {path}")

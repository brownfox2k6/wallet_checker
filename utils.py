from requests import get


API_KEY = "your_api_key"


def get_url(**kwargs):
    url = "https://api.etherscan.io/v2/api?"
    url += "".join(f"&{key}={value}" for key, value in kwargs.items() if value)
    url += f"&apikey={API_KEY}"
    return url


def get_data_from_url(url):
    response = get(url)
    data = response.json()
    return data["result"]


def wei_to_ether(wei: int | str) -> float:
    """
    Convert Wei to Ether:
    based on https://etherscan.io/unitconverter, 1 Ether = 1e18 Wei
    """
    return int(wei) / 1e18

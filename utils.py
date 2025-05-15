API_KEY = "your_api_key"

def get_url(**kwargs):
  url = "https://api.etherscan.io/v2/api?" + ''.join(f'&{key}={value}' for key, value in kwargs.items())
  return url
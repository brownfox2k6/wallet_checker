import requests, utils

def get_balance(chainid, module, action, address, tag, apikey):
  url = utils.get_url(chainid=chainid, module=module, action=action, address=address, tag=tag, apikey=apikey)
  gwei = int(requests.get(url).json()["result"])
  eth = gwei // 10**18
  return eth
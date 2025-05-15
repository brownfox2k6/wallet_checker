import requests
from utils import *


def get_ether_balance_single_address(address: str, chainid: int = 1, tag: str = "latest") -> float:
  """
  [Get Ether Balance for a Single Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-a-single-address)

  Returns: Ether balance of `address`
  """
  url = get_url(chainid=chainid, module="account", action="balance", address=address, tag=tag)
  response = requests.get(url)
  data = response.json()
  ether = wei_to_ether(data["result"])
  return ether


def get_ether_balance_multiple_addresses(addresses: list[str], chainid: int = 1, tag: str = "latest") -> list[float]:
  """
  [Get Ether Balance for Multiple Addresses in a Single Call](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-multiple-addresses-in-a-single-call)

  Returns: A list of Ether balances corresponding to each address in addresses.
  """
  address = ','.join(addresses)
  url = get_url(chainid=chainid, module="account", action="balancemulti", address=address, tag=tag)
  response = requests.get(url)
  data = response.json()
  ether_values = []
  for item in data["result"]:
    ether = wei_to_ether(item["balance"])
    ether_values.append(ether)
  return ether_values
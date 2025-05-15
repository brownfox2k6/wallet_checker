import requests
from utils import *


def get_ether_balance_single_address(address: str, chainid: int = 1, tag: str = "latest") -> float:
  """
  [Get Ether Balance for a Single Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-a-single-address) \n
  Returns: Ether balance of `address`
  """
  url = get_url(chainid=chainid, module="account", action="balance", address=address, tag=tag)
  response = requests.get(url)
  data = response.json()
  ether = wei_to_ether(data["result"])
  return ether


def get_ether_balance_multiple_addresses(addresses: list[str], chainid: int = 1, tag: str = "latest") -> list[float]:
  """
  [Get Ether Balance for Multiple Addresses in a Single Call](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-multiple-addresses-in-a-single-call) \n
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


def get_normal_transactions() -> list[dict]:
  pass


def get_internal_transactions_by_address() -> list[dict]:
  pass


def get_internal_transactions_by_transaction_hash() -> list[dict]:
  pass


def get_internal_transactions_by_block_range() -> list[dict]:
  pass


def get_erc20_token_transfer_events() -> list[dict]:
  pass


def get_erc721_token_transfer_events() -> list[dict]:
  pass


def get_erc1155_token_transfer_events() -> list[dict]:
  pass


def get_address_funded_by() -> list[dict]:
  pass


def get_blocks_validated() -> list[dict]:
  pass


def get_beacon_chain_withdrawals() -> list[dict]:
  pass

from utils import *


def get_ether_balance_single_address(
    address: str, chainid: int = 1, tag: str = "latest"
) -> float:
    """
    [Get Ether Balance for a Single Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-a-single-address) \n
    Returns: the Ether balance of a given address.
    """
    url = get_url(
        chainid=chainid, module="account", action="balance", address=address, tag=tag
    )
    data = get_data_from_url(url)
    ether = wei_to_ether(data)
    return ether


def get_ether_balance_multiple_addresses(
    addresses: list[str], chainid: int = 1, tag: str = "latest"
) -> list[float]:
    """
    [Get Ether Balance for Multiple Addresses in a Single Call](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-ether-balance-for-multiple-addresses-in-a-single-call) \n
    Returns: the balance of the accounts from a list of addresses
    """
    address = ",".join(addresses)
    url = get_url(
        chainid=chainid,
        module="account",
        action="balancemulti",
        address=address,
        tag=tag,
    )
    data = get_data_from_url(url)
    ether_values = []
    for item in data:
        ether = wei_to_ether(item["balance"])
        ether_values.append(ether)
    return ether_values


def get_normal_transactions(
    address: str,
    chainid: int = 1,
    startblock: int = 0,
    endblock: int = 99999999,
    page: int = 1,
    offset: int = 10,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get a list of 'Normal' Transactions By Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-a-list-of-normal-transactions-by-address) \n
    Returns: the list of transactions performed by an address, with optional pagination
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="txlist",
        address=address,
        startblock=startblock,
        endblock=endblock,
        page=page,
        offset=offset,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_internal_transactions_by_address(
    address: str,
    chainid: int = 1,
    startblock: int = 0,
    endblock: int = 99999999,
    page: int = 1,
    offset: int = 10,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get a list of 'Internal' Transactions by Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-a-list-of-internal-transactions-by-address) \n
    Returns: the list of internal transactions performed by an address, with optional pagination
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="txlistinternal",
        address=address,
        startblock=startblock,
        endblock=endblock,
        page=page,
        offset=offset,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_internal_transactions_by_transaction_hash(
    txhash: str, chainid: int = 1
) -> list[dict]:
    """
    [Get 'Internal Transactions' by Transaction Hash](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-internal-transactions-by-transaction-hash) \n
    Returns: the list of internal transactions performed within a transaction
    """
    url = get_url(
        chainid=chainid, module="account", action="txlistinternal", txhash=txhash
    )
    data = get_data_from_url(url)
    return data


def get_internal_transactions_by_block_range(
    startblock: int,
    endblock: int,
    chainid: int = 1,
    page: int = 1,
    offset: int = 10,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get "Internal Transactions" by Block Range](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-internal-transactions-by-block-range) \n
    Returns: the list of internal transactions performed within a block range, with optimal pagination
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="txlistinternal",
        startblock=startblock,
        endblock=endblock,
        page=page,
        offset=offset,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_erc20_token_transfer_events(
    contract_address: str = "",
    address: str = "",
    chainid: int = 1,
    page: int = 1,
    offset: int = 10,
    startblock: int = 0,
    endblock: int = 99999999,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get a list of 'ERC20 - Token Transfer Events' by Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-a-list-of-erc20-token-transfer-events-by-address) \n
    Returns: the list of ERC-20 tokens transferred by an address, with optional filtering by token contract \n
    Usage:
        - ERC-20 transfers from an **address**, specify the `address` parameter
        - ERC-20 transfers from a **contract address**, specify the `contract address` parameter
        - ERC-20 transfers from an **address** filtered by a **token contract**, specify both `address` and `contract address` parameter
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="tokentx",
        contractaddress=contract_address,
        address=address,
        page=page,
        offset=offset,
        startblock=startblock,
        endblock=endblock,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_erc721_token_transfer_events(
    contract_address: str = "",
    address: str = "",
    chainid: int = 1,
    page: int = 1,
    offset: int = 10,
    startblock: int = 0,
    endblock: int = 99999999,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get a list of 'ERC721 - Token Transfer Events' by Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-a-list-of-erc721-token-transfer-events-by-address) \n
    Returns: the list of ERC-721 (NFT) tokens transferred by an address, with optional filtering by token contract \n
    Usage:
        - ERC-721 transfers from an **address**, specify the `address` parameter
        - ERC-721 transfers from a **contract address**, specify the `contract address` parameter
        - ERC-721 transfers from an **address** filtered by a **token contract**, specify both `address` and `contract address` parameter
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="tokennfttx",
        contractaddress=contract_address,
        address=address,
        page=page,
        offset=offset,
        startblock=startblock,
        endblock=endblock,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_erc1155_token_transfer_events(
    contract_address: str = "",
    address: str = "",
    chainid: int = 1,
    page: int = 1,
    offset: int = 10,
    startblock: int = 0,
    endblock: int = 99999999,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get a list of 'ERC1155 - Token Transfer Events' by Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-a-list-of-erc1155-token-transfer-events-by-address) \n
    Returns: the list of ERC-1155 (Multi Token Standard) tokens transferred by an address, with optional filtering by token contract \n
    Usage:
        - ERC-1155 transfers from an **address**, specify the `address` parameter
        - ERC-1155 transfers from a **contract address**, specify the `contract address` parameter
        - ERC-1155 transfers from an **address** filtered by a **token contract**, specify both `address` and `contract address` parameter
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="token1155tx",
        contractaddress=contract_address,
        address=address,
        page=page,
        offset=offset,
        startblock=startblock,
        endblock=endblock,
        sort=sort,
    )
    data = get_data_from_url(url)
    return data


def get_address_funded_by(address: str, chainid: int = 1) -> dict:
    """
    [Get Address Funded By](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-address-funded-by) \n
    Returns: the address that funded an address, and its relative age
    """
    url = get_url(chainid=chainid, module="account", action="fundedby", address=address)
    data = get_data_from_url(url)
    return data


def get_blocks_validated(
    address: str, blocktype: str, chainid: int = 1, page: int = 1, offset: int = 10
) -> list[dict]:
    """
    [Get list of Blocks Validated by Address](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-list-of-blocks-validated-by-address) \n
    Returns: a list of blocks validated by an address
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="getminedblocks",
        address=address,
        blocktype=blocktype,
        page=page,
        offset=offset,
    )
    data = get_data_from_url(url)
    return data


def get_beacon_chain_withdrawals(
    address: str,
    chainid: int = 1,
    startblock: int = 0,
    endblock: int = 99999999,
    page: int = 1,
    offset: int = 10,
    sort: str = "asc",
) -> list[dict]:
    """
    [Get Beacon Chain Withdrawals by Address and Block Range](https://docs.etherscan.io/etherscan-v2/api-endpoints/accounts#get-beacon-chain-withdrawals-by-address-and-block-range) \n
    Returns: the beacon chain withdrawals made to an address
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="txsBeaconWithdrawal",
        address=address,
        startblock=startblock,
        endblock=endblock,
        page=page,
        offset=offset,
        sort=sort,
    )

import requests
from utils import get_url, wei_to_ether


def get_token_supply(contract_address: str, chainid: int = 1) -> int:
    """
    Get ERC20-Token TotalSupply by ContractAddress
    Returns the current amount of an ERC-20 token in circulation.
    
    Args:
        contract_address: The contract address of the ERC-20 token
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        Total supply of the token in its smallest decimal representation
    """
    url = get_url(chainid=chainid, module="stats", action="tokensupply", contractaddress=contract_address)
    response = requests.get(url)
    data = response.json()
    return int(data["result"])


def get_token_balance(contract_address: str, address: str, chainid: int = 1, tag: str = "latest") -> int:
    """
    Get ERC20-Token Account Balance for TokenContractAddress
    Returns the current balance of an ERC-20 token of an address.
    
    Args:
        contract_address: The contract address of the ERC-20 token
        address: The address to check for token balance
        chainid: Chain ID (default: 1 for Ethereum mainnet)
        tag: The block number to check balance at (default: "latest")
    
    Returns:
        Token balance in its smallest decimal representation
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="tokenbalance",
        contractaddress=contract_address,
        address=address,
        tag=tag
    )
    response = requests.get(url)
    data = response.json()
    return int(data["result"])


def get_token_holders(contract_address: str, page: int = 1, offset: int = 10, chainid: int = 1) -> list[dict]:
    """
    Get Token Holder List by Contract Address
    Returns the current ERC20 token holders and number of tokens held.
    
    Args:
        contract_address: The contract address of the ERC-20 token
        page: Page number for pagination
        offset: Number of records per page
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        List of dictionaries containing TokenHolderAddress and TokenHolderQuantity
    """
    url = get_url(
        chainid=chainid,
        module="token",
        action="tokenholderlist",
        contractaddress=contract_address,
        page=page,
        offset=offset
    )
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_token_holder_count(contract_address: str, chainid: int = 1) -> int:
    """
    Get Token Holder Count by Contract Address
    Returns a simple count of the number of ERC20 token holders.
    
    Args:
        contract_address: The contract address of the ERC-20 token
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        Number of token holders
    """
    url = get_url(
        chainid=chainid,
        module="token",
        action="tokenholdercount",
        contractaddress=contract_address
    )
    response = requests.get(url)
    data = response.json()
    return int(data["result"])


def get_address_token_holdings(address: str, page: int = 1, offset: int = 100, chainid: int = 1) -> list[dict]:
    """
    Get Address ERC20 Token Holding
    Returns the ERC-20 tokens and amount held by an address.
    
    Args:
        address: The address to check for token holdings
        page: Page number for pagination
        offset: Number of records per page
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        List of dictionaries containing token information including:
        - TokenAddress
        - TokenName
        - TokenSymbol
        - TokenQuantity
        - TokenDivisor
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="addresstokenbalance",
        address=address,
        page=page,
        offset=offset
    )
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_address_nft_holdings(address: str, page: int = 1, offset: int = 100, chainid: int = 1) -> list[dict]:
    """
    Get Address ERC721 Token Holding
    Returns the ERC-721 tokens and amount held by an address.
    Note: This endpoint is throttled to 2 calls/second regardless of API Pro tier.
    
    Args:
        address: The address to check for NFT holdings
        page: Page number for pagination
        offset: Number of records per page
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        List of dictionaries containing NFT information including:
        - TokenAddress
        - TokenName
        - TokenSymbol
        - TokenQuantity
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="addresstokennftbalance",
        address=address,
        page=page,
        offset=offset
    )
    response = requests.get(url)
    data = response.json()
    return data["result"]


def get_address_nft_inventory(
    address: str,
    contract_address: str,
    page: int = 1,
    offset: int = 100,
    chainid: int = 1
) -> list[dict]:
    """
    Get Address ERC721 Token Inventory By Contract Address
    Returns the ERC-721 token inventory of an address, filtered by contract address.
    Note: This endpoint is throttled to 2 calls/second regardless of API Pro tier.
    
    Args:
        address: The address to check for NFT inventory
        contract_address: The ERC-721 token contract address to check for inventory
        page: Page number for pagination
        offset: Number of records per page (limited to 1000 records per query)
        chainid: Chain ID (default: 1 for Ethereum mainnet)
    
    Returns:
        List of dictionaries containing NFT inventory information including:
        - TokenAddress
        - TokenId
    """
    url = get_url(
        chainid=chainid,
        module="account",
        action="addresstokennftinventory",
        address=address,
        contractaddress=contract_address,
        page=page,
        offset=offset
    )
    response = requests.get(url)
    data = response.json()
    return data["result"] 
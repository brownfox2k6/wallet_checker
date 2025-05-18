from utils import *


def check_contract_execution_status(txhash: str, chainid: int = 1) -> tuple[bool, str]:
    """
    [Check Contract Execution Status](https://docs.etherscan.io/etherscan-v2/api-endpoints/stats#check-contract-execution-status) \n
    Returns: a tuple of bool and str:
        bool: True for successful transactions, False otherwise
        str: error description
    """
    url = get_url(
        chainid=chainid, module="transaction", action="getstatus", txhash=txhash
    )
    data = get_data_from_url(url)
    is_successful = data["isError"] == "0"
    error_description = data["errDescription"]
    return (is_successful, error_description)


def check_transaction_receipt_status(txhash: str, chainid: int = 1) -> bool:
    """
    [Check Transaction Receipt Status](https://docs.etherscan.io/etherscan-v2/api-endpoints/stats#check-transaction-receipt-status) \n
    Returns: True for successful transactions, False otherwise \n
    Note: Only applicable for post Byzantium Fork transactions
    """
    url = get_url(
        chainid=chainid,
        module="transaction",
        action="gettxreceiptstatus",
        txhash=txhash,
    )
    data = get_data_from_url(url)
    is_successful = data["status"] == "1"
    return is_successful

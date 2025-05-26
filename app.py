import streamlit as st
import pandas as pd
from accounts import (
    get_ether_balance_single_address,
    get_ether_balance_multiple_addresses,
    get_normal_transactions,
    get_internal_transactions_by_address,
    get_internal_transactions_by_transaction_hash,
    get_erc20_token_transfer_events,
    get_erc721_token_transfer_events,
    get_erc1155_token_transfer_events,
    get_address_funded_by,
    get_blocks_validated,
    get_beacon_chain_withdrawals,
)
from tokens import (
    get_token_supply,
    get_token_balance,
    get_token_holders,
    get_token_holder_count,
    get_address_token_holdings,
    get_address_nft_holdings,
    get_address_nft_inventory,
)
from transactions import (
    check_contract_execution_status,
    check_transaction_receipt_status,
)

st.set_page_config(page_title="Ethereum Wallet Checker", layout="wide")
st.title("Ethereum Wallet Checker")

category = st.sidebar.selectbox("Category", ["Accounts", "Tokens", "Transactions"])

if category == "Accounts":
    action = st.sidebar.selectbox("Action", [
        "Ether Balance (Single)",
        "Ether Balance (Multiple)",
        "Normal Transactions",
        "Internal Transactions by Address",
        "Internal Transactions by Tx Hash",
        "ERC20 Transfer Events",
        "ERC721 Transfer Events",
        "ERC1155 Transfer Events",
        "Address Funded By",
        "Blocks Validated",
        "Beacon Chain Withdrawals",
    ])

    if action == "Ether Balance (Single)":
        address = st.text_input("Address")
        chainid = st.number_input("Chain ID", min_value=1, value=1)
        tag = st.selectbox("Tag", ["latest", "pending", "earliest"])
        if st.button("Get Balance"):
            try:
                bal = get_ether_balance_single_address(address, chainid, tag)
                st.metric("Balance", f"{bal:.6f} ETH")
            except Exception as e:
                st.error(e)

    elif action == "Ether Balance (Multiple)":
        addrs = st.text_area("Addresses (comma-separated or each on a line)")
        chainid = st.number_input("Chain ID", min_value=1, value=1, key="multi_chain")
        tag = st.selectbox("Tag", ["latest", "pending", "earliest"], key="multi_tag")
        if st.button("Get Balances"):
            try:
                addr_lines = [a.strip().split(',') for a in addrs.split() if a.strip()]
                addr_list = []
                for line in addr_lines:
                    addr_list.extend(line)
                bals = get_ether_balance_multiple_addresses(addr_list, chainid, tag)
                st.table({addr: f"{bal:.6f} ETH" for addr, bal in zip(addr_list, bals)})
            except Exception as e:
                st.error(e)

    elif action == "Normal Transactions":
        address = st.text_input("Address")
        start = st.number_input("Start Block", value=0)
        end = st.number_input("End Block", value=99999999)
        page = st.number_input("Page", min_value=1, value=1)
        offset = st.number_input("Offset", min_value=1, value=10)
        sort = st.selectbox("Sort", ["asc", "desc"])
        if st.button("Fetch"):
            try:
                txs = get_normal_transactions(address, 1, start, end, page, offset, sort)
                df = pd.DataFrame(txs)
                st.dataframe(df)
            except Exception as e:
                st.error(e)

    elif action == "Internal Transactions by Address":
        address = st.text_input("Address")
        start = st.number_input("Start Block", value=0, key="int_addr_start")
        end = st.number_input("End Block", value=99999999, key="int_addr_end")
        page = st.number_input("Page", min_value=1, value=1, key="int_addr_page")
        offset = st.number_input("Offset", min_value=1, value=10, key="int_addr_offset")
        sort = st.selectbox("Sort", ["asc", "desc"], key="int_addr_sort")
        if st.button("Fetch"):
            try:
                txs = get_internal_transactions_by_address(address, 1, start, end, page, offset, sort)
                df = pd.DataFrame(txs)
                st.dataframe(df)
            except Exception as e:
                st.error(e)

    elif action == "Internal Transactions by Tx Hash":
        txhash = st.text_input("Transaction Hash")
        if st.button("Fetch"):
            try:
                txs = get_internal_transactions_by_transaction_hash(txhash, 1)
                df = pd.DataFrame(txs)
                st.dataframe(df)
            except Exception as e:
                st.error(e)

    elif action in ["ERC20 Transfer Events", "ERC721 Transfer Events", "ERC1155 Transfer Events"]:
        contract = st.text_input("Contract Address (optional)")
        address = st.text_input("Address (optional)")
        start = st.number_input("Start Block", value=0, key="erc_start")
        end = st.number_input("End Block", value=99999999, key="erc_end")
        page = st.number_input("Page", min_value=1, value=1, key="erc_page")
        offset = st.number_input("Offset", min_value=1, value=10, key="erc_offset")
        sort = st.selectbox("Sort", ["asc", "desc"], key="erc_sort")
        if st.button("Fetch Events"):
            try:
                if action == "ERC20 Transfer Events":
                    data = get_erc20_token_transfer_events(contract, address, 1, page, offset, start, end, sort)
                elif action == "ERC721 Transfer Events":
                    data = get_erc721_token_transfer_events(contract, address, 1, page, offset, start, end, sort)
                else:
                    data = get_erc1155_token_transfer_events(contract, address, 1, page, offset, start, end, sort)
                st.write(data)
            except Exception as e:
                st.error(e)

    elif action == "Address Funded By":
        address = st.text_input("Address")
        if st.button("Fetch"):
            try:
                st.json(get_address_funded_by(address, 1))
            except Exception as e:
                st.error(e)

    elif action == "Blocks Validated":
        address = st.text_input("Address")
        blocktype = st.selectbox("Block Type", ["blocks", "uncles"])
        page = st.number_input("Page", min_value=1, value=1, key="blk_page")
        offset = st.number_input("Offset", min_value=1, value=10, key="blk_offset")
        if st.button("Fetch"):
            try:
                st.json(get_blocks_validated(address, blocktype, 1, page, offset))
            except Exception as e:
                st.error(e)

    elif action == "Beacon Chain Withdrawals":
        address = st.text_input("Address")
        start = st.number_input("Start Block", value=0, key="beacon_start")
        end = st.number_input("End Block", value=99999999, key="beacon_end")
        page = st.number_input("Page", min_value=1, value=1, key="beacon_page")
        offset = st.number_input("Offset", min_value=1, value=10, key="beacon_offset")
        sort = st.selectbox("Sort", ["asc", "desc"], key="beacon_sort")
        if st.button("Fetch"):
            try:
                st.json(get_beacon_chain_withdrawals(address, 1, start, end, page, offset, sort))
            except Exception as e:
                st.error(e)

elif category == "Tokens":
    action = st.sidebar.selectbox("Action", [
        "Token Total Supply",
        "Token Balance",
        "Token Holders List",
        "Token Holder Count",
        "Address Token Holdings",
        "Address NFT Holdings",
        "Address NFT Inventory",
    ])

    if action == "Token Total Supply":
        contract = st.text_input("Contract Address")
        if st.button("Fetch Supply"):
            try:
                supply = get_token_supply(contract, 1)
                st.success(f"Total Supply: {supply}")
            except Exception as e:
                st.error(e)

    elif action == "Token Balance":
        contract = st.text_input("Contract Address")
        address = st.text_input("Address")
        chainid = st.number_input("Chain ID", min_value=1, value=1)
        tag = st.text_input("Tag", value="latest")
        if st.button("Fetch Balance"):
            try:
                bal = get_token_balance(contract, address, chainid, tag)
                st.success(f"Balance: {bal}")
            except Exception as e:
                st.error(e)

    elif action == "Token Holders List":
        contract = st.text_input("Contract Address")
        page = st.number_input("Page", min_value=1, value=1, key="th_page")
        offset = st.number_input("Offset", min_value=1, value=10, key="th_offset")
        if st.button("Fetch"):
            try:
                holders = get_token_holders(contract, page, offset, 1)
                st.dataframe(holders)
            except Exception as e:
                st.error(e)

    elif action == "Token Holder Count":
        contract = st.text_input("Contract Address")
        if st.button("Fetch Count"):
            try:
                count = get_token_holder_count(contract, 1)
                st.success(f"Holders: {count}")
            except Exception as e:
                st.error(e)

    elif action == "Address Token Holdings":
        address = st.text_input("Address")
        page = st.number_input("Page", min_value=1, value=1, key="ath_page")
        offset = st.number_input("Offset", min_value=1, value=100, key="ath_offset")
        if st.button("Fetch"):
            try:
                holdings = get_address_token_holdings(address, page, offset, 1)
                st.dataframe(holdings)
            except Exception as e:
                st.error(e)

    elif action == "Address NFT Holdings":
        address = st.text_input("Address")
        page = st.number_input("Page", min_value=1, value=1, key="anh_page")
        offset = st.number_input("Offset", min_value=1, value=100, key="anh_offset")
        if st.button("Fetch"):
            try:
                nfts = get_address_nft_holdings(address, page, offset, 1)
                st.dataframe(nfts)
            except Exception as e:
                st.error(e)

    elif action == "Address NFT Inventory":
        address = st.text_input("Address")
        contract = st.text_input("Contract Address")
        page = st.number_input("Page", min_value=1, value=1, key="ani_page")
        offset = st.number_input("Offset", min_value=1, value=100, key="ani_offset")
        if st.button("Fetch"):
            try:
                inv = get_address_nft_inventory(address, contract, page, offset, 1)
                st.dataframe(inv)
            except Exception as e:
                st.error(e)

else:  # Transactions
    action = st.sidebar.selectbox("Action", [
        "Contract Execution Status",
        "Transaction Receipt Status",
    ])

    if action == "Contract Execution Status":
        txhash = st.text_input("Transaction Hash")
        chainid = st.number_input("Chain ID", min_value=1, value=1)
        if st.button("Check"):
            try:
                success, err = check_contract_execution_status(txhash, chainid)
                if success:
                    st.success("Transaction succeeded")
                else:
                    st.error(f"Failed: {err}")
            except Exception as e:
                st.error(e)

    elif action == "Transaction Receipt Status":
        txhash = st.text_input("Transaction Hash")
        chainid = st.number_input("Chain ID", min_value=1, value=1, key="rc_chain")
        if st.button("Check"):
            try:
                ok = check_transaction_receipt_status(txhash, chainid)
                if ok:
                    st.success("Receipt status: Success")
                else:
                    st.error("Receipt status: Failed")
            except Exception as e:
                st.error(e)

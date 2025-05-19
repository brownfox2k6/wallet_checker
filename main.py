import tokens;
import os
import json

if __name__ == "__main__":
    # Example 1: Get USDT balance for Vitalik's wallet
    vitalik_usdt_balance = tokens.get_token_balance(
        contract_address="0xdAC17F958D2ee523a2206206994597C13D831ec7",  # USDT
        address="0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"  # Vitalik's wallet
    )
    print(f"\nVitalik's USDT Balance: {vitalik_usdt_balance / 1e6:.2f} USDT")  # USDT has 6 decimals

    # Example 2: Get all token holdings for Binance hot wallet
    binance_holdings = tokens.get_address_token_holdings(
        address="0x28C6c06298d514Db089934071355E5743bf21d60"
    )
    print("\nBinance Hot Wallet Holdings:")
    # Print raw response first to see the format
    print("Raw response:", json.dumps(binance_holdings, indent=2))
    
    # Example 3: Get UNI token holders
    uni_holders = tokens.get_token_holders(
        contract_address="0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984",  # UNI
        page=1,
        offset=10
    )
    print("\nTop 10 UNI Token Holders:")
    # Print raw response first to see the format
    print("Raw response:", json.dumps(uni_holders, indent=2))

    # Example 4: Get NFT holdings for a wallet
    # This address has some Bored Ape NFTs
    nft_wallet = "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
    nft_holdings = tokens.get_address_nft_holdings(address=nft_wallet)
    print("\nNFT Holdings:")
    # Print raw response first to see the format
    print("Raw response:", json.dumps(nft_holdings, indent=2))

import os
from web3 import Web3
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# RPC URLs for BSC & Ethereum
BSC_RPC = "https://bsc-dataseed.binance.org/"
ETH_RPC = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura Project ID

# Token contract addresses mapped to their respective blockchain
TOKENS = {
    "BabyDoge": ("0xc748673057861a797275CD8A068AbB95A902e8de", BSC_RPC),
    "USDT (BSC)": ("0x55d398326f99059fF775485246999027B3197955", BSC_RPC),
    "USDT (ETH)": ("0xdAC17F958D2ee523a2206206994597C13D831ec7", ETH_RPC),
    "USDC (ETH)": ("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", ETH_RPC),
    "DAI (ETH)": ("0x6B175474E89094C44Da98b954EedeAC495271d0F", ETH_RPC),  # DAI Stablecoin
    "Chainlink (ETH)": ("0x514910771AF9Ca656af840dff83E8264EcF986CA", ETH_RPC),  # Chainlink Token
    "Shiba Inu (ETH)": ("0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE", ETH_RPC),  # Shiba Inu Token
    "PancakeSwap (BSC)": ("0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82", BSC_RPC),  # PancakeSwap Token
    "BakeryToken (BSC)": ("0xAD29AbB318791D579433D831ed122aFeAf29dcfe", BSC_RPC),  # BakeryToken
}

# Token contract ABI (only for `balanceOf` and `decimals`)
TOKEN_ABI = [
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "stateMutability": "view", "type": "function"},
]

def get_token_balance(wallet_address, token_address, rpc_url):
    """Fetch the token balance for a given wallet and contract address."""
    web3 = Web3(Web3.HTTPProvider(rpc_url))

    # Check if connected
    if not web3.is_connected():
        print(f"Error: Could not connect to {rpc_url}")
        return None

    try:
        contract = web3.eth.contract(
            address=web3.to_checksum_address(token_address), 
            abi=TOKEN_ABI
        )
        decimals = contract.functions.decimals().call()  # Fetch token decimals
        balance = contract.functions.balanceOf(web3.to_checksum_address(wallet_address)).call()
        return balance / (10 ** decimals)  # Convert balance using decimals
    except Exception as e:
        print(f"Error fetching balance for {wallet_address} on {token_address}: {e}")
        return None

def get_bnb_balance(wallet_address):
    """Fetch the BNB balance of a given wallet."""
    web3 = Web3(Web3.HTTPProvider(BSC_RPC))
    
    if not web3.is_connected():
        print("Error: Could not connect to BSC node")
        return None

    try:
        balance = web3.eth.get_balance(web3.to_checksum_address(wallet_address))  # Get native BNB balance
        return balance / (10 ** 18)  # Convert from Wei to BNB
    except Exception as e:
        print(f"Error fetching BNB balance for {wallet_address}: {e}")
        return None

if __name__ == "__main__":
    wallets_file = "C:\\Users\\Pc\\Desktop\\fresh_wallets.txt"

    try:
        with open(wallets_file, "r") as file:
            wallets = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: Wallet file not found at {wallets_file}")
        exit()

    for wallet in wallets:
        print(f"\n🔍 Checking balances for: {wallet}")

        # Convert wallet address to checksum format
        wallet = Web3.to_checksum_address(wallet)

        # Check native BNB balance
        bnb_balance = get_bnb_balance(wallet)
        if bnb_balance is not None:
            if bnb_balance > 0:
                print(f"{Fore.RED}BNB: {bnb_balance:.6f}")
            else:
                print(f"BNB: {bnb_balance:.6f}")
        else:
            print(f"BNB: ❌ Error fetching balance")

        # Check token balances
        for token_name, (contract_address, rpc_url) in TOKENS.items():
            balance = get_token_balance(wallet, contract_address, rpc_url)
            if balance is not None:
                if balance > 0:
                    print(f"{Fore.RED}{token_name}: {balance:.6f}")
                else:
                    print(f"{token_name}: {balance:.6f}")
            else:
                print(f"{token_name}: ❌ Error fetching balance")

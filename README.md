# Multi-Crypto-wallet-checker
multiscript
# Wallet Balance Checker

## Overview
This Python script checks the balances of multiple cryptocurrency wallets for various tokens on the Binance Smart Chain (BSC) and Ethereum blockchain. It fetches balances for both native coins (BNB) and selected ERC-20/BEP-20 tokens using Web3.py.

## Features
- Reads wallet addresses from a text file (`fresh_wallets.txt`).
- Connects to Binance Smart Chain (BSC) and Ethereum Mainnet via RPC.
- Retrieves balances for:
  - Native BNB on BSC.
  - ERC-20/BEP-20 tokens like USDT, USDC, DAI, Chainlink, Shiba Inu, PancakeSwap, BakeryToken, and BabyDoge.
- Displays balances in the terminal, highlighting non-zero balances in red for easy identification.
- Handles errors for missing wallets, network issues, and smart contract calls.

## Requirements
- Python 3.x
- Required Python packages:
  - `web3`
  - `colorama`
  - `os`

Install dependencies using:
```sh
pip install web3 colorama
```

## Usage
1. **Edit the wallet file**:
   - Add wallet addresses (one per line) to `C:\Users\Pc\Desktop\fresh_wallets.txt`.
2. **Run the script**:
   ```sh
   python script.py
   ```
3. **View the results**:
   - The script will display each wallet's balance.
   - If a wallet has funds, the balance will appear in **red**.

## Configuration
- **RPC URLs**:
  - The script uses `https://bsc-dataseed.binance.org/` for BSC and an Infura RPC URL for Ethereum.
  - Replace `YOUR_INFURA_PROJECT_ID` in the script with your Infura API key.

- **Supported Tokens**:
  - You can add more token contract addresses in the `TOKENS` dictionary within the script.

## Example Output
```
🔍 Checking balances for: 0x123...ABC
BNB: 0.005000
USDT (BSC): 25.000000
Shiba Inu (ETH): 0.000000
```

If a wallet has a balance greater than 0, the output will be in **red** for easy spotting.

## Troubleshooting
- **Error: Wallet file not found**: Ensure `fresh_wallets.txt` exists at the specified path.
- **Could not connect to BSC node**: Check your internet connection or try a different RPC.
- **Error fetching balance**: Ensure the wallet address and contract address are correct.

## Disclaimer
This script is for informational purposes only. Use at your own risk.


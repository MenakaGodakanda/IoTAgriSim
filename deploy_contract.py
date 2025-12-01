from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Set the default account
w3.eth.default_account = w3.eth.accounts[0]

# Load the contract ABI and bytecode
with open('contract_abi.json', 'r') as abi_file:
    abi = json.load(abi_file)
with open('contract_bytecode.txt', 'r') as bytecode_file:
    bytecode = bytecode_file.read().strip()

# Create the contract instance
Contract = w3.eth.contract(abi=abi, bytecode=bytecode)

# Deploy the contract
tx_hash = Contract.constructor().transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Contract deployed at address: {tx_receipt.contractAddress}")

# Save the contract address to a file
with open('contract_address.txt', 'w') as address_file:
    address_file.write(tx_receipt.contractAddress)

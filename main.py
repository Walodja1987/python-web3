import os
import abis.diva_abi as diva_abi
from web3 import Web3
import addresses
from diva_functions import getPoolParameters
from termcolor import colored

# Load relevant variables from .env file
NETWORK = os.environ.get("NETWORK")
RPC_URL = os.environ.get("RPC_" + NETWORK.upper())

# print(colored(NETWORK, 'blue'))

# Get web3 instance
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Connect to DIVA
diva_contract = w3.eth.contract(
    address = addresses.diva_contract_addresses[NETWORK], abi=diva_abi.abi)

# print(diva_contract.functions.__dict__)

if __name__ == "__main__":
    pool_id = 300
    # res = diva_contract.functions.getPoolParameters(pool_id).call()
    # print(res[0])
    getPoolParameters(pool_id, NETWORK, diva_contract)
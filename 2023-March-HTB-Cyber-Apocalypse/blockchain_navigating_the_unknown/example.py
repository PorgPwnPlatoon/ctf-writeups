import pprint

from web3 import Web3, AsyncWeb3
from solcx import compile_source

w3 = Web3(Web3.HTTPProvider('http://206.189.112.129:30596'))

print(f"connected: {w3.is_connected()}")


def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()

   return compile_source(source,output_values=['abi','bin'])


def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

source_file = 'Setup.sol'
compiled_sol = compile_source_file(source_file)


address = '0xFD9e19130E8B3DF1C85eB838362C44A250343d8F'
address = '0xd304F9EA526CF09E707900A47d9376931fC06B8D'

contract_id, contract_interface = compiled_sol.popitem()

contract_instance = w3.eth.contract(address=address, abi=contract_interface["abi"])

gas_estimate = contract_instance.functions.updateSensors(10).estimate_gas()
print(f'Gas estimate to transact with setVar: {gas_estimate}')

tx_hash = contract_instance.functions.updateSensors(10).transact()
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])

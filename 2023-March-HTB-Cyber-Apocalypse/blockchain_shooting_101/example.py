import pprint

from web3 import Web3, AsyncWeb3
from solcx import compile_source

w3 = Web3(Web3.HTTPProvider('http://138.68.162.218:32054'))

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

address = '0x706fF8dd6Dbb3bc264Ae6C0fC9C56c19edC35886'
contractAddress = '0x30403a638187e1c458B451570cCEca5b634aDcbb'

contract_id, contract_interface = compiled_sol.popitem()

contract_instance = w3.eth.contract(address=contractAddress, abi=contract_interface["abi"])

#gas_estimate = contract_instance.functions.updateSensors(10).estimate_gas()
#print(f'Gas estimate to transact with setVar: {gas_estimate}')
#FALLBACK
'''
tx_hash = w3.eth.send_transaction({'to': contractAddress, 'from': address, 'data': '0x41414141'})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
'''
#RECEIVE
'''
try:
    tx_hash = w3.eth.send_transaction({'to': contractAddress, 'from': address})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction receipt mined:")
    pprint.pprint(dict(receipt))
    print("\nWas transaction successful?")
    pprint.pprint(receipt["status"])
except:
    pass
'''
tx_hash = contract_instance.functions.third().transact()
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])

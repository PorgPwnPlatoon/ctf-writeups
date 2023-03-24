import pprint

from web3 import Web3, AsyncWeb3
from solcx import compile_source

w3 = Web3(Web3.HTTPProvider('http://104.248.169.177:32038'))

print(f"connected: {w3.is_connected()}")
print(w3.eth.accounts[0])
print(w3.eth.accounts[1])

def compile_source_file(file_path):
   with open(file_path, 'r') as f:
      source = f.read()

   return compile_source(source,output_values=['abi','bin-runtime'])


def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin-runtime']).constructor().transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

source_file = 'FortifiedPerimeter.sol'
compiled_sol = compile_source_file(source_file)

source_file2 = 'MyEntrant.sol'
entrant_sol = compile_source_file(source_file2)

private_key     =  '0x3f4f895b21c334b2dae05a6ce5eccfb6f730a47c26a8d429698366bc7262e3f5'
address         =  '0xF12E70bD5B79c3B4306A13a6029fb8f5B22Efb5F'
target_contract =  '0x35B3C8E89707DE2dEaB49cf27A70Ab4D4899110C'
setup_contract  =  '0x00e9Cd563757598dbC4EB2081f0276060ddBB497'

contract_id, contract_interface2 = compiled_sol.popitem()

entrant_contract_id, entrant_interface = entrant_sol.popitem()
print(f"entrant_contract_id : {entrant_contract_id}")
print(entrant_interface["abi"])
print(entrant_interface["bin-runtime"])

entrant_contract_id, entrant_interface = entrant_sol.popitem()
print(f"entrant_contract_id : {entrant_contract_id}")
print(entrant_interface["abi"])
print(entrant_interface["bin-runtime"])
'''
entrant_address = deploy_contract(w3, entrant_interface)
print(f"Deployed contract_id: {contract_id} to: {entrant_address}")
print(f"entrant_contract_id : {entrant_contract_id}")
print(f"entrant_address : {entrant_address}")

contract_instance = w3.eth.contract(address=target_contract, abi=contract_interface2["abi"])
my_entrant_instance = w3.eth.contract(address=entrant_address, abi=entrant_interface["abi"])

for func in my_entrant_instance.functions:
    print(func)

print()

tx_hash = my_entrant_instance.functions.proxyenter().transact()
#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
pprint.pprint(w3.eth.get_transaction(tx_hash))

print("------")
'''
'''
tx = contract_instance.functions.enter().build_transaction({'from': entrant_address})
signed_trans = w3.eth.account.sign_transaction(tx, private_key=private_key)

#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(signed_trans)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
'''
'''
print("------")

tx = contract_instance.functions.lastEntrant().call()
#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(tx)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
#pprint.pprint(w3.eth.get_transaction

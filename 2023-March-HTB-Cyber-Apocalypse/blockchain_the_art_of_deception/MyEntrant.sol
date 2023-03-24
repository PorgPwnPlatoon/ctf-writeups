pragma solidity ^0.8.18;

import "./FortifiedPerimeter.sol";

contract MyEntrant is Entrant {
	
	HighSecurityGate public highSecurityGate;
	bool initialised;

	constructor(address _highSecurityGateAddress) {
		highSecurityGate = HighSecurityGate(_highSecurityGateAddress);
		initialised = false;
	}

	function name() external returns (string memory) {
		if(initialised) {
			return "Pandora";
		} else {
			initialised = true;
			return "Orion";
		}
	}

	function proxyenter() external {
		highSecurityGate.enter();
	}
}

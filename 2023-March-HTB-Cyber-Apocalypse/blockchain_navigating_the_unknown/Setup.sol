pragma solidity ^0.8.18;

import {Unknown} from "./Unknown.sol";

contract Setup {
    Unknown public immutable TARGET;

    constructor() {
        TARGET = new Unknown();
    }

    function isSolved() public view returns (bool) {
        return TARGET.updated();
    }
}


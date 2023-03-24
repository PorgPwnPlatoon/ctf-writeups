# Blockchain: The art of deception

As with the other Blockchain challenges we were provided with two IP and port combinations:

* First would just `nc <ip> -p <port>' - which provided all the account/contract address and private keys

* Second was IP/Port to put it solution.py script

Once again for this challenge I used the following python libraries:

- web3py     - for interaction with blockchain - see: https://web3py.readthedocs.io/en/stable/examples.html
- py-solc-x  - for compiling the sol contract fiels - see: https://solcx.readthedocs.io/en/latest/

From the `Setup.sol` file we can see the aim for this challenge:

```
return TARGET.strcmp(TARGET.lastEntrant(), "Pandora");
```

We need to get the target contract to have lastEntrant field == "Pandora"

The target contract in this challenge was `HighSecurityGate`, which has an `enter` function that basicaly casts the `msg.sender` into an `Entrant` and calls it's `name()` function. This is then passed through a required `_isAuthorized` function. If this failes the "intruder detected" is output by contract toherwise our target variable `lastEntrant` is set.

The contract has a list of x3 names that are authorized and just does a string of `msg.sender` against each ["Orion", "Nova", "Eclipse"]

A lot of reading had to be done at this point regards what `msg.sender` is, how casting works i.e. `Entrant(msg.sender)`, then how inheritence works, and then how to deploy a new contract....

But in the end our `solution.py` demonstrates the following:

1. We created a new contract `MyEntrant` which:
  1. Is an implementation of `Entrant` (so has a `name()` function) 
  2. Also provides a hook/proxy to the `HighSecurityGate.enter()` function

This means we can deploy this additional contract, it is intialised with the reference to the original TARGET contract (`HighSecurityGate`), when the `proxyenter()` function is called by our standard account this makes a request to the reference TARGET `enter()` function but this call will be made with our contracts address as `msg.sender`. This means the TARGET contract will cast `msg.sender` back to an instance of our contract and call our `name()` function which initially returns `Orion` (an authorized name) to pass auth check, and then on second call to set `lastEntrant` it will return `Pandora`.




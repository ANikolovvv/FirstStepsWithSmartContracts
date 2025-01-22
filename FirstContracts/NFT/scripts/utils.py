from brownie import accounts, network, config
from typing import Optional


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]

def get_account(index: Optional[int] = None, id: Optional[str] = None):
  
    if index is not None:
        return accounts[index]

    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]

    if id is not None:
        return accounts.load(id)

    return accounts.add(config["wallets"]["from_key"])

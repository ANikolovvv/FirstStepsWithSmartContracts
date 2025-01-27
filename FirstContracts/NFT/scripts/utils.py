from brownie import accounts, network, config
from typing import Optional

LOCAL_BLOCKCHAINS = ["hardhat", "development", "ganache"]

def get_account(index: Optional[int] = None, id: Optional[str] = None):
    if index is not None:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAINS:
        return accounts[0]
    if id is not None:
        return accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    raise Exception("No valid account configuration found")
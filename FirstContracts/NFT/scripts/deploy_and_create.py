from utils import get_account
from brownie import NFT


sample_token_uri = (
    "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()  
    nft = NFT.deploy({"from": account})  

    print(f"NFT contract deployed at: {nft.address}")


def main():
    deploy_and_create()

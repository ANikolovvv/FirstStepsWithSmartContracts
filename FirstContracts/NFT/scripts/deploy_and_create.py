from utils import get_account
from brownie import NFT


sample_token_uri = (
    "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW?filename=st-bernard.png",
)


def deploy_and_create():
    account = get_account()  
    nft = NFT.deploy({"from": account})
    tx=nft.createNFT(sample_token_uri,{"from": account})
    tx.wait(1);  

    print(f"NFT contract deployed at: {nft.address}")
    return nft


def main():
    deploy_and_create()

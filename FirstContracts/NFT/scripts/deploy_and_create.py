from brownie import NFT, accounts, network, config
from utils import get_account
import json
import requests

SAMPLE_METADATA = {
    "name": "REX",
    "description": "An adorable REX pup!",
    "image": "https://ipfs.io/ipfs/QmUPjADFGEKmfohdTaNcWhp7VGk26h5jXDA7v3VtTnTLcW",
    "attributes": [{"trait_type": "cuteness", "value": 100}]
}

IPFS_PIN_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
PINATA_HEADERS = {
    "pinata_api_key": config["pinata"]["api_key"],
    "pinata_secret_api_key": config["pinata"]["api_secret"]
}

def deploy_and_create():
    try:
        account = get_account()
        
        # Deploy contract with base URI
        nft = NFT.deploy("ipfs://", {"from": account})
        if not nft.address:
            raise ValueError("Contract deployment failed")
        
        # Upload metadata to IPFS
        response = requests.post(
            IPFS_PIN_URL,
            headers=PINATA_HEADERS,
            json=SAMPLE_METADATA
        )
        response.raise_for_status()
        ipfs_hash = response.json()["IpfsHash"]
        token_uri = f"ipfs://{ipfs_hash}"
        
        # Mint NFT
        tx = nft.createNFT(token_uri, {"from": account})
        tx.wait(1)
        
        # Verify
        assert nft.ownerOf(0) == account.address
        print(f"Success! NFT Contract: {nft.address}")
        return nft
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    deploy_and_create()
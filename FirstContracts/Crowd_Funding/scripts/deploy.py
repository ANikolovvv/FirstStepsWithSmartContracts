from brownie import accounts, config,CrowdFunding , network


def deploy_crowd_funding():
     account = get_account()
     price_feed_address = "0x694AA1769357215DE4FAC081bf1f309aDC325306"
     crownd_funding=CrowdFunding.deploy(price_feed_address,{"from":account})
     print(f"Contract deployed to {crownd_funding.address}")
  

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_crowd_funding()
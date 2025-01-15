from brownie import CrowdFunding, accounts, network, config
import pytest

# Constants for testing
MINIMUM_USD = 50 * 10**18


@pytest.fixture
def deploy_contract():
    
    account = accounts[0]

    # Use the price feed address from the config
    if network.show_active() in ["development", "ganache-local"]:
        price_feed_address = "0x0000000000000000000000000000000000000000"  # Replace with mock or dummy address if needed
    else:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]

    # Deploy the CrowdFunding contract
    crowdfunding = CrowdFunding.deploy(price_feed_address, {"from": account})
    return crowdfunding


def test_deployment(deploy_contract):
    
    crowdfunding = deploy_contract
    owner = crowdfunding.owner()
    assert owner == accounts[0], "Owner should be the deployer account"


def test_funding(deploy_contract):
    
    crowdfunding = deploy_contract
    account = accounts[1]
    initial_balance = account.balance()

    # Fund the contract
    eth_to_send = crowdfunding.getEntranceFee() + 1  # Slightly more than minimum
    crowdfunding.funding({"from": account, "value": eth_to_send})

    assert crowdfunding.addressToAmountFunded(account) == eth_to_send
    assert account.balance() < initial_balance, "Account balance should decrease"


def test_get_conversion_rate(deploy_contract):
   
    crowdfunding = deploy_contract
    eth_amount = 1 * 10**18  # 1 ETH
    conversion_rate = crowdfunding.getConversionRate(eth_amount)

    assert conversion_rate > 0, "Conversion rate should be greater than zero"


def test_withdraw(deploy_contract):
   
    crowdfunding = deploy_contract
    owner = accounts[0]
    funder = accounts[1]

    # Fund the contract
    eth_to_send = crowdfunding.getEntranceFee() + 1
    crowdfunding.funding({"from": funder, "value": eth_to_send})

    # Withdraw funds
    initial_balance = owner.balance()
    crowdfunding.withdraw({"from": owner})

    # Check that the contract balance is zero
    assert crowdfunding.balance() == 0, "Contract balance should be zero after withdrawal"

    # Check that the owner received the funds
    assert owner.balance() > initial_balance, "Owner should receive the withdrawn funds"

    # Verify that funders are reset
    assert crowdfunding.addressToAmountFunded(funder) == 0, "Funders' contributions should be reset"


def test_only_owner_can_withdraw(deploy_contract):
  
    crowdfunding = deploy_contract
    non_owner = accounts[1]

    with pytest.raises(Exception, match="Only the owner can call this function"):
        crowdfunding.withdraw({"from": non_owner})

// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract CrowdFunding {
    address public owner;
    address[] public funders;
    mapping(address => uint256) public addressToAmountFunded;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    function funding() public payable {
        uint256 minimumUSD = 50 * 10**18; // Minimum threshold is 50 USD
        require(
            getConversionRate(msg.value) >= minimumUSD,
            "You need to spend at least 50 USD worth of ETH!"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return uint256(price) * 10**10; // Convert to 18 decimal places
    }

    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();
        return (ethPrice * ethAmount) / 10**18;
    }

    function getEntranceFee() public view returns (uint256) {
        uint256 minimumUSD = 50 * 10**18;
        uint256 ethPrice = getPrice();
        uint256 precision = 1 * 10**18;
        return (minimumUSD * precision) / ethPrice;
    }

    function withdraw() public onlyOwner {
        for (uint256 i = 0; i < funders.length; i++) {
            addressToAmountFunded[funders[i]] = 0;
        }
        payable(owner).transfer(address(this).balance);
        funders = new address[](0);
    }
}

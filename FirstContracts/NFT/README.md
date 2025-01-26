# NFT Smart Contract

This is a smart contract implementing the **ERC-721** standard for **Non-Fungible Tokens (NFTs)** using **Solidity**. The contract includes basic functionality for creating NFT tokens with unique **token URIs** and supports burning tokens.


## Description

This smart contract implements the **ERC-721** standard for **Non-Fungible Tokens (NFTs)** and uses **OpenZeppelin** libraries for safety and standard implementations.

The contract’s main features include:

- **Minting NFTs**: The `createNFT` function allows users to mint new NFT tokens with a unique **token URI**.
- **Burning NFTs**: The contract supports a function to burn tokens if needed.
- **Unique Identifiers**: Each NFT has a unique **tokenId** that increments with each newly minted NFT.

## Deployment

1. Install the required dependencies:

```bash
npm install @openzeppelin/contracts

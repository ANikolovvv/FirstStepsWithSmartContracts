// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract NFT is ERC721URIStorage, AccessControl {
    uint256 public tokenCounter;
    string public baseURI;
    bytes32 public constant MINTER_ROLE = keccak256("MINTER_ROLE");

    event NFTMinted(address indexed to, uint256 tokenId, string tokenURI);

    constructor(string memory _baseURI) ERC721("Rex", "DOG") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(MINTER_ROLE, msg.sender);
        baseURI = _baseURI;
    }

    function createNFT(string memory tokenURI) public onlyRole(MINTER_ROLE) returns (uint256) {
        uint256 newTokenId = tokenCounter++;
        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, string(abi.encodePacked(baseURI, tokenURI)));
        emit NFTMinted(msg.sender, newTokenId, tokenURI);
        return newTokenId;
    }

    function setBaseURI(string memory _newBaseURI) public onlyRole(DEFAULT_ADMIN_ROLE) {
        baseURI = _newBaseURI;
    }

    function _burn(uint256 tokenId) internal override(ERC721URIStorage) {
        super._burn(tokenId);
    }

    function supportsInterface(bytes4 interfaceId) public view override(ERC721URIStorage, AccessControl) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
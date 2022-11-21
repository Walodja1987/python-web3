abi = '''[
  {
    "inputs": [
      { "internalType": "uint256", "name": "_poolId", "type": "uint256" },
      {
        "internalType": "uint256",
        "name": "_finalReferenceValue",
        "type": "uint256"
      },
      { "internalType": "bool", "name": "_allowChallenge", "type": "bool" }
    ],
    "name": "setFinalReferenceValue",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "_poolId",
        "type": "uint256"
      }
    ],
    "name": "getPoolParameters",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint256",
            "name": "floor",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "inflection",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "cap",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "gradient",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "collateralBalance",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "finalReferenceValue",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "capacity",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "statusTimestamp",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "shortToken",
            "type": "address"
          },
          {
            "internalType": "uint96",
            "name": "payoutShort",
            "type": "uint96"
          },
          {
            "internalType": "address",
            "name": "longToken",
            "type": "address"
          },
          {
            "internalType": "uint96",
            "name": "payoutLong",
            "type": "uint96"
          },
          {
            "internalType": "address",
            "name": "collateralToken",
            "type": "address"
          },
          {
            "internalType": "uint96",
            "name": "expiryTime",
            "type": "uint96"
          },
          {
            "internalType": "address",
            "name": "dataProvider",
            "type": "address"
          },
          {
            "internalType": "enum LibDIVAStorage.Status",
            "name": "statusFinalReferenceValue",
            "type": "uint8"
          },
          {
            "internalType": "string",
            "name": "referenceAsset",
            "type": "string"
          }
        ],
        "internalType": "struct LibDIVAStorage.Pool",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]
'''
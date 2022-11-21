import os

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")

# View function
def getPoolParameters(pool_id, network, contract):
    # print(contract.functions)
    try: 
        res = contract.functions.getPoolParameters(int(pool_id)).call()
        return res
    except Exception as err:
        print("Some error occured")
        return

# State modifying function
"""
def retrieveData(pool_id, network, my_contract):
    queryDataArgs = eth_abi.encode_abi(["int", "address", "int"], [int(pool_id), tellor.divaDiamond[network], int(config.chain_id[network])])
    queryData = eth_abi.encode_abi(["string", "bytes"], ["DIVAProtocol", queryDataArgs])
    queryId = keccak.new(digest_bits=256)
    queryId.update(queryData)
    values = []

    try:
        count = my_contract.functions.getNewValueCountbyQueryId('0x' + queryId.hexdigest()).call()
        for idx in range(count):
            timestmp = my_contract.functions.getTimestampbyQueryIdandIndex('0x' + queryId.hexdigest(), idx).call()
            data = my_contract.functions.retrieveData('0x' + queryId.hexdigest(), timestmp).call()
            disp = my_contract.functions.isDisputed('0x' + queryId.hexdigest(), timestmp).call()  # Later we have to use the function isInDispute()
            val = eth_abi.decode_abi(['uint256', 'uint256'],data)
            values.append([float(web3.Web3.fromWei(val[0], 'ether')), float(web3.Web3.fromWei(val[1], 'ether')), timestmp, disp])
        return values

    except Exception as err:
        printb("Failure: ", err.args[0])
        return
"""


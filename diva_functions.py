import os

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")

# View function
def getPoolParameters(pool_id, network, contract):
    # print(contract.functions)
    try: 
        print(contract.functions.__dict__)
        res = contract.functions.getPoolParameters(int(pool_id)).call()
        return res
    except Exception as err:
        print("Some error occured")
        return

# State modifying function
# TODO


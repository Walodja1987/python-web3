import os

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
PUBLIC_KEY = os.environ.get("PUBLIC_KEY")

# View function
def getPoolParameters(pool_id, contract):
    try: 
        res = contract.functions.getPoolParameters(pool_id).call()
        return res
    except Exception as err:
        print("Some error occured", err.args)
        return

# State modifying function
# TODO


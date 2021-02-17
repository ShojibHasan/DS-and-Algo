# import hashlib
# hash = hashlib.sha256("secret message".encode()).hexdigest()
# print(hash)

from Block import Block
blockchain =[]
genesis_block = Block("Chancellor on the brink....",["Satoshi sent 1 BTC to IVAN","Maria sent 5 BTC to Jenny","Satoshi sent 5 BTC to Hal Finney"])


first_block = Block("Chancellor on the brink....",["Satoshi sent 5 BTC to Hal Finney"])
second_block = Block("Chancellor on the brink....",["Satoshi sent 5 BTC to Hal Finney"])
if first_block.block_hash==second_block.block_hash:
    print("same Block")
else:
    print("Not same Block")
# print(first_block.block_hash)

# print(genesis_block.block_hash)

# cbe3d8752934802fed9ccac0d9e0f660751dd30c7e92b86d94d3885ee822f87d
# 538073411c8113e39d3e20f812cbf27389c45ec499dced6e337fa6a68e72aa81

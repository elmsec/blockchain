from blockchain import Blockchain, Transaction


elmacoin = Blockchain()
ts_0 = Transaction(amount=100, sender=None, receiver='::can::')
ts_1 = Transaction(amount=20.8, sender='::can::', receiver='::lara::')
ts_2 = Transaction(amount=23.7, sender='::lara::', receiver='::can::')

print('add transaction...')
elmacoin.add_transaction(ts_0)
elmacoin.add_transaction(ts_1)
elmacoin.add_transaction(ts_2)
print('done.', end='\n\n')

print('mine_pending_transactions...')
elmacoin.mine_pending_transactions('::can::')
print('balance: ', elmacoin.get_address_balance('::can::'), end='\n\n')

print('mine_pending_transactions...')
elmacoin.mine_pending_transactions('::can::')
print('balance: ', elmacoin.get_address_balance('::can::'))

# print('Adding new block...')
# elmacoin.add_block(block_1)
# print(block_1)

# print('Adding new block...')
# elmacoin.add_block(block_2)
# print(block_2)

# print('Checking the chain validity...')
# print('It is valid!' if elmacoin.is_valid() else 'It is invalid!')

# elmacoin.latest_block.amount = 10000
# print('Checking the chain validity again after changing data...')
# print('It is valid!' if elmacoin.is_valid() else 'It is invalid!')

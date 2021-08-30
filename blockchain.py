import time
import hashlib


class Transaction():
    def __init__(self, amount, sender, receiver):
        self.amount = amount
        self.sender = sender
        self.receiver = receiver
        self.timestamp = time.time()

    def calculate_hash(self):
        d = self.__dict__.copy()
        return hashlib.sha256(str(d).encode()).hexdigest()

    def sign(self):
        # tx_hash = self.calculate_hash()
        # sign hash
        pass

    def __str__(self):
        return (
            f'amount: {self.amount}\t sender: {self.sender}\t'
            f'receiver: {self.receiver}')


class Block:
    def __init__(self, transactions=[]):
        self.transactions = transactions
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.previous_hash = None

    def calculate_hash(self):
        d = self.__dict__.copy()
        d.pop('hash', None)
        return hashlib.sha256(str(d).encode()).hexdigest()

    def mine(self, difficulty=1):
        while self.hash[:difficulty] != difficulty * '0':
            self.nonce += 1
            self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain = [self.add_first_block()]
        self.difficulty = 3
        self.pending_transactions = []
        self.mining_award = 10

    def mine_pending_transactions(self, miner_address):
        # block.previous_hash = self.latest_block.hash
        block = Block(self.pending_transactions)
        block.mine(self.difficulty)
        self.chain.append(block)

        self.pending_transactions = []
        reward_ts = Transaction(self.mining_award, None, miner_address)
        self.add_transaction(reward_ts)

    def get_address_balance(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    balance -= transaction.amount

                if transaction.receiver == address:
                    balance += transaction.amount
        return balance

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def add_first_block(self):
        return Block()

    @property
    def latest_block(self):
        return self.chain[-1]

    def is_valid(self):
        until = len(self.chain)
        for i in range(1, until):
            block = self.chain[i]
            previous_block = self.chain[i - 1]

            if block.hash != block.calculate_hash():
                return False

            if block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        return '\n'.join([str(block) for block in self.chain])

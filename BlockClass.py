import hashlib as hash_er


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hash_er.sha256()
        temp = str(self.index) + \
               str(self.timestamp) + \
               str(self.data) + \
               str(self.previous_hash)
        sha.update(temp.encode('utf-8'))
        return sha.hexdigest()

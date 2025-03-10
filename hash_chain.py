class HashChain:
    def __init__(self, seed=None):
        self.random_generator = random.Random(seed)
        self.chain = [self.random_generator.randint(0, 2**32 - 1)]

    def next(self):
        self.chain.append(sha256(self.chain[-1].to_bytes(4, 'big')).digest())
        return int.from_bytes(self.chain[-1], 'big')

    def get_all_hashes(self):
        return self.chain
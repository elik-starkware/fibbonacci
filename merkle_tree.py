from hashlib import sha256

class MerkleTree:
    def __init__(self, leaves: list[int]):
        assert len(leaves) & (len(leaves) - 1) == 0, "Leaves must be a power of 2"
        self.leaves = leaves
        self.tree = []
        self.root = self._build_tree()

    def get_path(self, leaf_index: int) -> list[int]:
        path = []
        layer_index = 0
        path.append(self.tree[layer_index][leaf_index])
        while layer_index < len(self.tree) - 1:
            path.append(self.tree[layer_index][leaf_index + 1 if leaf_index % 2 == 0 else leaf_index - 1])
            layer_index += 1
            leaf_index = leaf_index // 2
        return path


    def _build_tree(self) -> list[int]:
        curr_layer = [sha256(str(leaf).encode()).hexdigest() for leaf in self.leaves]
        self.tree.append(curr_layer)
        while len(curr_layer) > 1:
            next_layer = self._build_layer(curr_layer)
            self.tree.append(next_layer)
            curr_layer = next_layer
        return curr_layer[0]
        

    def _build_layer(self, layer: list[int]) -> list[int]:
        new_layer = []
        for i in range(0, len(layer), 2):
            new_layer.append(sha256((layer[i]+ layer[i + 1]).encode()).hexdigest())
        return new_layer

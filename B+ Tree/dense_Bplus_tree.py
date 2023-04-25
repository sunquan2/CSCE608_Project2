
class dense_tree:
    def __init__(self, order):
        self.order = order
        self.root = dense_tree_nodes(order)

    def insert(self, num):
        if not self.root.isFull():
            # add the function to insert the item
            pass



class dense_tree_nodes:
    def __init__(self, order):
        self.nodes = []
        self.order = order
        self.isleaf = True
        self.parent = None

    def isFull(self):
        return len(self.nodes) == self.order

    def insert(self, num):
        if not self.isFull():




class dense_tree:
    def __init__(self, order):
        self.order = order
        self.root = dense_tree_nodes(order)

    def insert(self, num):
        new_root = self.root.insert(num, is_root = True)
        if new_root == None:
            return
        else:
            self.root = new_root



class dense_tree_nodes:
    def __init__(self, order):
        self.keys = []
        self.pointer = []
        self.order = order
        self.isleaf = True

    def isFull(self):
        return len(self.keys) == self.order

    # insert on page 40 of slide 17
    def insert(self, num, is_root):
        if self.isleaf:
            if len(self.keys) <= self.order:
                self.keys.append(num)
                self.keys.sort()
                print("inserted " + str(num))
                return None
            else:
                newlist = self.nodes.append(num)
                newlist.sort()
                left = newlist[:len(newlist)/2]
                right = newlist[len(newlist)/2:]
                if is_root == False:
                    self.keys = left
                    if len(self.pointer) > 0:
                        cur_pointer = self.pointer[-1]
                    new_leaf = dense_tree_nodes(self.order)
                    new_leaf.keys = right
                    new_leaf.pointer.append(cur_pointer)
                    self.pointer = new_leaf
                    print("inserted " + str(num) + " made new leaf")
                    return new_leaf
                else:
                    new_root = dense_tree_nodes(self.order)
                    new_root.keys = [right[0]]
                    new_root.isleaf = False
                    left_leaf = dense_tree_nodes(self.order)
                    left_leaf.keys = left
                    right_leaf = dense_tree_nodes(self.order)
                    right_leaf.keys = right
                    left_leaf.pointer = right_leaf
                    new_root.pointer = [left_leaf, right_leaf]
                    print("inserted " + str(num) + " made new root")
        else:








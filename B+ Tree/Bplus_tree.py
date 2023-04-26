
class Bplus_tree:
    def __init__(self, order):
        self.order = order
        self.root = tree_nodes(order)

    def insert(self, num):
        new_root = self.root.insert(num, is_root = True)
        if new_root == None:
            return
        else:
            self.root = new_root

    def delete(self, num):
        ########################################
        # Complete this function
        ########################################
        return

    def dense_construct(self, input_array):
        # the input cannot be none
        if type(input_array) != list or len(input_array) == 0:
            print("error, invalid input")
        # at the first time of call, sort all inputs
        if type(input_array[0]) == int:
            input_array.sort()
        if len(input_array) <= self.order:
            # if input size is small, we can construct the root
            if type(input_array[0]) == int:
                # case 1, the root is also the leaf
                self.root.keys = input_array
                print("dense tree constructed, single level")
                return
            else:
                # case 2, the root is not the leaf
                self.root.pointer = input_array
                for i in range(len(input_array) - 1):
                    self.root.keys.append(input_array[i].get_largest())
                self.root.isleaf = False
                print("dense tree constructed, multiple levels")
                return
        else:
            # if the input size is large, we should reduce the size of the inputs by constructing one layer
            # this will reduce the input size by 1/order
            if type(input_array[0]) == int:
                # case 1. we are building the leaf layer, the inputs are all numbers
                new_input_array = []
                while len(input_array) > 2 * self.order:
                    cur_node = tree_nodes(self.order)
                    cur_node.keys = input_array[:self.order]
                    input_array = input_array[self.order:]
                    new_input_array.append(cur_node)
                    if len(new_input_array) > 0:
                        new_input_array[-1].pointer.append(cur_node)
                index_sep = int(len(input_array)/2)
                left = tree_nodes(self.order)
                left.keys = input_array[:index_sep]
                if len(new_input_array) > 0:
                    new_input_array[-1].pointer.append(left)
                right = tree_nodes(self.order)
                right.keys = input_array[index_sep:]
                left.pointer.append(right)
                new_input_array.append(left)
                new_input_array.append(right)
                # recursively call the same function with new inputs, new inputs are list of nodes
                return self.dense_construct(new_input_array)
            else:
                # case 2, we are building a non-leaf layer, the inputs lists are list of tree nodes
                new_input_array = []
                while len(input_array) > 2 * self.order:
                    cur_node = tree_nodes(self.order)
                    # step 1. Set the cur node to non-leaf
                    cur_node.isleaf = False
                    # cur_node will be the new node, which cannot be leaf
                    # step 2. insert keys
                    # the number of keys should be one smaller than the number of pointers
                    # the cur_node is supposed to be full, therefore, the number of keys shuold be
                    # self.order - 1
                    for i in range(self.order - 1):
                        cur_node.keys.append(input_array[i].get_largest())
                    # step 3. insert pointers
                    cur_node.pointer = input_array[:self.order]
                    input_array = input_array[self.order:]
                    new_input_array.append(cur_node)
                # the remaining inputs are too short to fit in more than 2
                index_sep = int(len(input_array) / 2)
                left = tree_nodes(self.order)
                left.isleaf = False
                left.pointer = input_array[:index_sep]
                for i in range(index_sep - 1):
                    left.keys.append(left.pointer[i].get_largest())
                new_input_array.append(left)
                right = tree_nodes(self.order)
                right.isleaf = False
                right.pointer = input_array[index_sep:]
                for i in range(len(right.pointer) - 1):
                    right.keys.append(right.pointer[i].get_largest())
                new_input_array.append(right)
                return self.dense_construct(new_input_array)

    def sparse_construct(self, input_array):
        # the input cannot be none
        if type(input_array) != list or len(input_array) == 0:
            print("error, invalid input")
        # at the first time of call, sort all inputs
        if type(input_array[0]) == int:
            input_array.sort()
        if len(input_array) <= self.order:
            # if input size is small, we can construct the root
            if type(input_array[0]) == int:
                # case 1, the root is also the leaf
                self.root.keys = input_array
                print("sparse tree constructed, single level")
                return
            else:
                # case 2, the root is not the leaf
                self.root.pointer = input_array
                for i in range(len(input_array) - 1):
                    self.root.keys.append(input_array[i].get_largest())
                self.root.isleaf = False
                print("sparse tree constructed, multiple levels")
                return
        else:
            # if the input size is large, we should reduce the size of the inputs by constructing one layer
            # this will reduce the input size by 1/order
            # we are constructing the non-root
            if type(input_array[0]) == int:
                # case 1. we are building the leaf layer, the inputs are all numbers
                # the difference between the dense construct is that the non-root part
                # we will construct as much nodes that are half the size of order as possible
                new_input_array = []
                while len(input_array) > self.order:
                    cur_node = tree_nodes(self.order)
                    cur_node.keys = input_array[:int(self.order/2)+1]
                    input_array = input_array[int(self.order/2)+1:]
                    if len(new_input_array) > 0:
                        new_input_array[-1].pointer.append(cur_node)
                    new_input_array.append(cur_node)
                # last nodes, put all together
                left = tree_nodes(self.order)
                left.keys = input_array
                # different from the dense, we only have one node, there is no right
                if len(new_input_array) > 0:
                    new_input_array[-1].pointer.append(left)
                new_input_array.append(left)
                # recursively call the same function with new inputs, new inputs are list of nodes
                return self.sparse_construct(new_input_array)
            else:
                # case 2, we are building a non-leaf layer, the inputs lists are list of tree nodes
                new_input_array = []
                while len(input_array) > self.order:
                    cur_node = tree_nodes(self.order)
                    # step 1. Set the cur node to non-leaf
                    cur_node.isleaf = False
                    # cur_node will be the new node, which cannot be leaf
                    # step 2. insert keys
                    # the number of keys should be one smaller than the number of pointers
                    # the cur_node is supposed to be full, therefore, the number of keys shuold be
                    # self.order - 1
                    for i in range(int(self.order / 2)):
                        cur_node.keys.append(input_array[i].get_largest())
                    # step 3. insert pointers
                    cur_node.pointer = input_array[:int(self.order / 2)+1]
                    input_array = input_array[int(self.order / 2)+1:]
                    new_input_array.append(cur_node)
                # the remaining inputs will fit in one last node
                left = tree_nodes(self.order)
                left.isleaf = False
                left.pointer = input_array
                for i in range(len(input_array) - 1):
                    left.keys.append(left.pointer[i].get_largest())
                new_input_array.append(left)
                # likewise there is no right
                return self.sparse_construct(new_input_array)

    def search(self, num):
        ########################################
        # Complete this function
        ########################################
        return

    def range_search(self, range):
        ########################################
        # Complete this function
        ########################################
        return

class tree_nodes:
    def __init__(self, order):
        self.keys = []
        self.pointer = []
        self.order = order
        self.isleaf = True

    def isFull(self):
        return len(self.keys) == self.order

    def get_largest(self):
        if len(self.keys) == 0:
            return None
            print("Error, current node is empty")
        else:
            return max(self.keys)

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
                    new_leaf = tree_nodes(self.order)
                    new_leaf.keys = right
                    new_leaf.pointer.append(cur_pointer)
                    self.pointer = new_leaf
                    print("inserted " + str(num) + " made new leaf")
                    return new_leaf
                else:
                    new_root = tree_nodes(self.order)
                    new_root.keys = [right[0]]
                    new_root.isleaf = False
                    left_leaf = tree_nodes(self.order)
                    left_leaf.keys = left
                    right_leaf = tree_nodes(self.order)
                    right_leaf.keys = right
                    left_leaf.pointer = right_leaf
                    new_root.pointer = [left_leaf, right_leaf]
                    print("inserted " + str(num) + " made new root")
        else:
            #################################
            # to be completed, refer to page 40
            #################################
            return








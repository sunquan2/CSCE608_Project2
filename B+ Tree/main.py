import random
import Bplus_tree

# 1. generate 10000 random numbers
def gen_10000_rand():
    random_numbers = []
    for i in range(10000):
        random_numbers.append(random.randint(100000, 200000))
    return random_numbers

random_numbers = gen_10000_rand()
# 2. Building B+ Trees
Collection_C = random_numbers[:5000]
print(Collection_C)

# Test dense B+ tree construct
'''
test_dense = Bplus_tree.Bplus_tree(13)
test_dense.dense_construct(Collection_C)
print(test_dense)
print(test_dense.root.keys)
print(test_dense.root.pointer)
print(test_dense.root.isleaf)
print(test_dense.root.order)
print(test_dense.root.pointer[0].keys)
print(test_dense.root.pointer[0].pointer)
print(test_dense.root.pointer[0].isleaf)
print(test_dense.root.pointer[0].order)
print(test_dense.root.pointer[1].keys)
print(test_dense.root.pointer[1].pointer)
print(test_dense.root.pointer[1].isleaf)
print(test_dense.root.pointer[1].order)
'''

# Test sparse B+ tree construct
test_sparse = Bplus_tree.Bplus_tree(13)
test_sparse.sparse_construct(Collection_C)
print(test_sparse)
print(test_sparse.root.keys)
print(test_sparse.root.pointer)
print(test_sparse.root.isleaf)
print(test_sparse.root.order)
print(test_sparse.root.pointer[0].keys)
print(test_sparse.root.pointer[0].pointer)
print(test_sparse.root.pointer[0].isleaf)
print(test_sparse.root.pointer[0].order)
print(test_sparse.root.pointer[1].keys)
print(test_sparse.root.pointer[1].pointer)
print(test_sparse.root.pointer[1].isleaf)
print(test_sparse.root.pointer[1].order)
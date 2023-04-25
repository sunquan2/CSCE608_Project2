import random
import dense_Bplus_tree
import sparse_Bplus_tree

# 1. generate 10000 random numbers
random_numbers = []
for i in range(10000):
    random_numbers.append(random.randint(100000, 200000))
print(random_numbers)

# 2. Building B+ Trees
Collection_C = random_numbers[:30]
Collection_C

test_dense = 0
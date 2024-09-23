# 순열 
from itertools import permutations
data = ['A', 'B', 'C']

result = list(permutations(data,3))
print(result)

# 조합
from itertools import combinations
data = ['A', 'B', 'C']

result = list(combinations(data,3))
print(result)

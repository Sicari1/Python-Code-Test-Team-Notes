
# Python Coding Test Cheat Sheet

## 1. Basic Builtin Functions

### abs(), all(), any()
- `abs(x)`: Returns the absolute value of a number.
- `all(iterable)`: Returns `True` if all elements in the iterable are true.
- `any(iterable)`: Returns `True` if any element in the iterable is true.

### dir(object)
- Shows all methods and properties of the specified object.
```python
dir([1,2,3,4])  # Shows all list methods
```

### format(value, format_spec)
- Formats a value according to the specified format.
- Examples:
  - `format(1000000, ',')` → `'1,000,000'` (comma-separated)
  - `format(1000000, 'e')` → `'1.000000e+06'` (scientific notation)
  - `format(1000000, 'x')` → `'f4240'` (hexadecimal)
  - `format(1000000, '!>20,.4f')` → `'!!!!1,000,000.0000'` (width and fill)

## 2. filter(function, iterable)
- Filters elements based on a condition.
```python
def is_even(value):
    return value % 2 == 0

list(filter(is_even, range(20)))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
list(filter(lambda x: x % 2 == 0, range(20)))  # Same as above
[i for i in range(20) if i % 2 == 0]  # List comprehension alternative
```

## 3. map(function, iterable)
- Applies a function to each item in the iterable.
```python
list(map(lambda x: x**2, range(20)))  # Squares each number in the range
```

## 4. zip(*iterables)
- Combines elements from multiple iterables.
```python
list(zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4], [10, 20, 30, 40], 'ABCD'))
# Output: [('a', 1, 10, 'A'), ('b', 2, 20, 'B'), ('c', 3, 30, 'C'), ('d', 4, 40, 'D')]
```

## 5. Sorting with sorted and sort
- `sorted()` returns a new sorted list, while `sort()` modifies the list in place.
```python
L = [10, 5, 4, 3, 7, 6]
L.sort()  # Modifies L directly
sorted([10, 5, 4, 3, 7, 6])  # Returns a new sorted list
```

### sorted() Examples:
```python
sorted(testCaseOne, key=len, reverse=True)
sorted(testCaseTwo, key=str.lower)
sorted(testCaseThree, key=lambda x: x[1])
```

## 6. List and Tuple Operations
- `append()`, `clear()`, `copy()`, `count()`, `extend()`, `index()`, `insert()`, `pop()`, `remove()`

### Queue / Stack Structure:
```python
# Queue (FIFO)
L = []
L.append(10)
L.pop(0)

# Stack (LIFO)
L.append(10)
L.pop()
```

### Tuple Specific Methods
- `t.count()` and `t.index()` are available, with time complexity `O(n)`.

## 7. Dictionary and Set Operations

### Dictionary
- `keys()`, `values()`, `items()`
```python
d = {'one': '하나', 'two':'둘'}
del d['one']  # Efficient deletion
d['one'] = '하나'  # Adding an item
```

### Set
- Operations: `add()`, `union()`, `intersection()`, `difference()`, `discard()`
```python
A = {'A', 'B', 'C'}
B = {'A', 'B', 'D'}
print(A.difference(B))  # {'C'}
print(A.intersection(B))  # {'A', 'B'}
```

## List Comprehension and Type Conversion
```python
[int(i) for i in '1 2 3 4 5 6 7'.split()]
list(map(int, '1 2 3 4 5 6 7'.split()))
```

## BFS and DFS Basics

### BFS (Breadth-First Search)
```python
from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
```

### DFS (Depth-First Search)
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, visited)
    return visited
```

## Sorting Algorithms for Coding Tests
- **Bubble Sort**: `O(n^2)`
- **Selection Sort**: `O(n^2)`
- **Insertion Sort**: `O(n^2)`
- **Merge Sort**: `O(n log n)`
- **Quick Sort**: Average `O(n log n)`

### Quick Sort Example:
```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

## Practice Problems

1. **BFS & DFS Implementation**: Start node traversal with BFS and DFS.
2. **Sorting Challenges**: Custom sorting according to given constraints.
3. **Data Structure Operations**: Problem-solving using lists, tuples, dictionaries, and sets.
4. **Filter and Map Practice**: Filtering or mapping lists with specific conditions.

### For Improvement
- Practice classic BFS/DFS on platforms like [LeetCode](https://leetcode.com), [Baekjoon](https://www.acmicpc.net), and [Programmers](https://programmers.co.kr).


# Sorting and `lambda` functions in Python

In coding tests, sorting based on specific elements within a list is common. This guide covers several ways to sort lists using `lambda` functions and custom `key` functions in Python.

## Basic Sorting Example

You can use the `sorted()` function or `list.sort()` method with the `key` argument to specify the sorting criterion.

### Example 1: Sorting by the First Element (`x[0]`)

```python
points = [(3, 4), (1, 2), (5, 1)]

# Sort by the first element (x[0])
sorted_by_first = sorted(points, key=lambda x: x[0])
print(sorted_by_first)  # Output: [(1, 2), (3, 4), (5, 1)]
```

### Example 2: Sorting by the Second Element (`x[1]`)

```python
points = [(3, 4), (1, 2), (5, 1)]

# Sort by the second element (x[1])
sorted_by_second = sorted(points, key=lambda x: x[1])
print(sorted_by_second)  # Output: [(5, 1), (1, 2), (3, 4)]
```

## Using a Custom Key Function

Sometimes, you might want to define a key function separately instead of using a `lambda` function.

```python
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

# Sorting by the second element using a custom key function
print(sorted(array, key=my_key))  # Output: [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
```

## Using `lambda` for One-Time Functions

If the function is used only once, `lambda` is useful for defining the sorting criteria inline:

```python
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# Sorting by the second element using a lambda function
print(sorted(array, key=lambda x: x[1]))  # Output: [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
```

## Applying to Multiple Lists

The `map()` function can be used alongside `lambda` for operations on multiple lists:

```python
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))  # Output: [7, 9, 11, 13, 15]
```

## Sorting for Coding Tests

In coding tests, the following sorting techniques might be useful:
1. **Sorting tuples or lists by specific elements**: `sorted(list, key=lambda x: x[index])`
2. **Sorting dictionaries by values**: `sorted(dict.items(), key=lambda item: item[1])`
3. **Custom sorting logic**: Define a function or use `lambda` as needed.

### Example: Sorting a List of Dictionaries

```python
students = [
    {'name': 'John', 'age': 20},
    {'name': 'Jane', 'age': 22},
    {'name': 'Doe', 'age': 21}
]

# Sorting by age
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)  # Output: [{'name': 'John', 'age': 20}, {'name': 'Doe', 'age': 21}, {'name': 'Jane', 'age': 22}]
```

Remember, `sorted()` returns a new sorted list, while `list.sort()` sorts the list in place.


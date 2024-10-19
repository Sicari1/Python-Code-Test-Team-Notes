## Summary of Lambda Functions and Sorted

### sorted(반복가능한 객체, key = lambda x(반복가능한객체의 각 요소) : 반환하는 값)
- The first argument of `sorted()` is an iterable (such as a list, tuple, or dictionary keys), and each element is passed to the lambda function.
- The lambda function returns a value used as the sorting key.

### Example of sorting with lambda:
- Sorting numbers by absolute value:
    ```python
    sorted(numbers, key=lambda x: abs(x))
    ```

- Sorting strings by their length:
    ```python
    sorted(words, key=lambda x: len(x))
    ```

### genre_songs Example with Tuple Sorting:
- In `genre_songs[genre]`, each element is a tuple with `(play count, song ID)`.
- To sort by play count in descending order and by song ID in ascending order:
    ```python
    genre_songs[genre].sort(key=lambda x: (-x[0], x[1]))
    ```

### extend vs append:
- `append`: Adds an element to the end of a list. If the element is a list, the entire list is added as one element.
    ```python
    a.append([4, 5])  # Output: [1, 2, 3, [4, 5]]
    ```

- `extend`: Extends the list by adding each element from another list individually.
    ```python
    a.extend([4, 5])  # Output: [1, 2, 3, 4, 5]
    ```


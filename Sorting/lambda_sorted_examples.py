# Sorted with Lambda Example:
# sorted(반복가능한 객체, key = lambda x(반복가능한객체의 각 요소) : 반환하는 값) 에 따라 정렬
# The first argument to sorted() is an iterable, and each element of the iterable is passed to the lambda function.
# The lambda function returns a value used for sorting the elements.

# Example 1: Sorting numbers by absolute value
numbers = [-10, 5, -7, 2, -3, 8, -1]
sorted_numbers = sorted(numbers, key=lambda x: abs(x))
print("Sorted by absolute value:", sorted_numbers)
# Output: [-1, 2, -3, 5, -7, 8, -10]

# Example 2: Sorting strings by length
words = ["apple", "banana", "kiwi", "cherry", "blueberry"]
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted by string length:", sorted_words)
# Output: ['kiwi', 'apple', 'cherry', 'banana', 'blueberry']

# Example 3: Sorting tuples by the second value, descending
pairs = [(1, 9), (3, 6), (5, 3), (7, 2), (4, 8)]
sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
print("Sorted by second tuple value, descending:", sorted_pairs)
# Output: [(1, 9), (4, 8), (3, 6), (5, 3), (7, 2)]

# Sorting within genre_songs
# genre_songs[genre] has tuples in the format (play count, song ID)
genre_songs = {
    "classic": [(800, 3), (500, 0), (150, 2)],
    "pop": [(2500, 4), (600, 1)]
}
# Sorting by play count (descending), then by song ID (ascending)
for genre in genre_songs:
    genre_songs[genre].sort(key=lambda x: (-x[0], x[1]))
    print(f"Sorted songs in {genre}: {genre_songs[genre]}")
# Output:
# Sorted songs in classic: [(800, 3), (500, 0), (150, 2)]
# Sorted songs in pop: [(2500, 4), (600, 1)]

# Extend vs Append Example
a = [1, 2, 3]
a.append([4, 5])
print("After append:", a)  # Output: [1, 2, 3, [4, 5]]

a = [1, 2, 3]
a.extend([4, 5])
print("After extend:", a)  # Output: [1, 2, 3, 4, 5]

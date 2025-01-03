
### 오늘의 문제
아래 코드는 옷의 조합을 계산하는 문제를 해결합니다. 각 종류의 의상별로 경우의 수를 계산한 뒤 곱셈으로 모든 조합을 구하고, 아무것도 선택하지 않는 경우를 제외하기 위해 마지막에 1을 뺍니다.

```python
def solution(clothes):
    answer = 1
    from collections import defaultdict
    A = defaultdict(list)
    
    for cloth in clothes:
        name, kind = cloth[0], cloth[1]
        A[kind].append(name)
    
    for value in A.values():
        answer *= len(value) + 1
    return answer - 1
```

### defaultdict에 대한 설명
`defaultdict`는 키가 존재하지 않을 때 기본값을 자동으로 생성하는 딕셔너리입니다.

```python
from collections import defaultdict

A = defaultdict(list)
A['shirts'].append('red shirt')  # 'shirts': ['red shirt'] 생성
A['pants'].append('blue jeans')  # 'pants': ['blue jeans'] 생성
print(A)  # 출력: {'shirts': ['red shirt'], 'pants': ['blue jeans']}
```

기본 딕셔너리를 사용하면 다음과 같이 수동 초기화가 필요합니다.

```python
A = {}
for cloth in clothes:
    name, kind = cloth[0], cloth[1]
    if kind not in A:
        A[kind] = []  # 키가 없으면 빈 리스트로 초기화
    A[kind].append(name)
```

### sort와 key=lambda
`sort()`와 `sorted()`는 리스트를 정렬할 때 사용됩니다. `key=lambda`를 사용하면 사용자 지정 기준으로 정렬할 수 있습니다.

```python
numbers = [-4, -1, 0, 3, 10]
numbers.sort(key=lambda x: abs(x))
print(numbers)  # 출력: [0, -1, 3, -4, 10]

strings = ["banana", "pie", "apple", "orange"]
strings.sort(key=lambda x: len(x))
print(strings)  # 출력: ['pie', 'apple', 'banana', 'orange']
```

`sorted()`는 원본을 유지하면서 정렬된 새 리스트를 반환합니다.

```python
numbers = [3, 1, 4, 1, 5, 9]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # 출력: [9, 5, 4, 3, 1, 1]
```

### 딕셔너리 주요 함수
1. `keys()`는 모든 키를 반환합니다.
```python
my_dict = {"name": "Alice", "age": 25}
print(my_dict.keys())  # 출력: dict_keys(['name', 'age'])
```
2. `values()`는 모든 값을 반환합니다.
```python
print(my_dict.values())  # 출력: dict_values(['Alice', 25])
```
3. `items()`는 키-값 쌍을 반환합니다.
```python
print(my_dict.items())  # 출력: dict_items([('name', 'Alice'), ('age', 25)])
```
4. `get()`는 키가 없을 때 기본값을 반환합니다.
```python
print(my_dict.get("city", "Unknown"))  # 출력: Unknown
```
5. `update()`는 딕셔너리에 새 키-값 쌍을 추가합니다.
```python
my_dict.update({"city": "New York"})
print(my_dict)  # 출력: {'name': 'Alice', 'age': 25, 'city': 'New York'}
```
6. `pop()`는 지정된 키를 제거하고 값을 반환합니다.
```python
age = my_dict.pop("age")
print(age)  # 출력: 25
```

### 딕셔너리 정렬
딕셔너리를 키, 값 또는 조건에 따라 정렬할 수 있습니다.

```python
unsorted_dict = {"b": 3, "a": 1, "c": 2}
sorted_by_key = dict(sorted(unsorted_dict.items(), key=lambda x: x[0]))
sorted_by_value = dict(sorted(unsorted_dict.items(), key=lambda x: x[1]))
print(sorted_by_key)  # 출력: {'a': 1, 'b': 3, 'c': 2}
print(sorted_by_value)  # 출력: {'a': 1, 'c': 2, 'b': 3}
```

### 코딩 테스트에서 유용한 딕셔너리 활용 예제
1. 등장 횟수 세기
```python
from collections import Counter
data = ["apple", "banana", "apple"]
counter = Counter(data)
print(counter)  # 출력: Counter({'apple': 2, 'banana': 1})
```
2. 최대값 찾기
```python
scores = {"Alice": 90, "Bob": 85, "Charlie": 95}
max_score = max(scores.items(), key=lambda x: x[1])
print(max_score)  # 출력: ('Charlie', 95)
```
3. 조건에 따른 필터링
```python
students = {"Alice": 90, "Bob": 85, "Charlie": 95}
high_scores = {k: v for k, v in students.items() if v > 90}
print(high_scores)  # 출력: {'Charlie': 95}
```
4. 기본값 활용
```python
from collections import defaultdict
A = defaultdict(int)
A["apple"] += 1
print(A)  # 출력: defaultdict(<class 'int'>, {'apple': 1})
```
5. 리스트를 딕셔너리로 변환
```python
fruits = ["apple", "banana", "orange"]
fruit_dict = {fruit: len(fruit) for fruit in fruits}
print(fruit_dict)  # 출력: {'apple': 5, 'banana': 6, 'orange': 6}
```

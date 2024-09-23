# 한 번만 쓰고 말 함수를 사용할 때 유용하다.
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x:x[1]))

# 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a,b: a + b, list1, list2)

print(list(result))

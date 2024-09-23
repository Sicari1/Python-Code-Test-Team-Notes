# Basic readline
## Example 1
a, b, c = map(int, input().split())

## Example 2
n = int(input))
data = list(map(int, input().split()))

print(n)
print(data)
              
# Faster
## Example 1
import sys
data = sys.stdin.readline().rstrip()
print(data)


# rstrip
## sys.stdin.readline()을 하면 한 줄을 그대로 받아오기 때문에 "5\n" 과 같이 엔터도 받아오게 되어 int()할 수 없게 된다.
## 그래서 .rstrip()을 사용해서 \n을 제거해주는 것.
## map(int, sys.stdin.readline().split())을 하면 split() 함수가 '' 공백을 기준으로 '\n'과 관계없이 글자를 구분해주기 때문에 .rstrip()을 사용할 필요가 없다.

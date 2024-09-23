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

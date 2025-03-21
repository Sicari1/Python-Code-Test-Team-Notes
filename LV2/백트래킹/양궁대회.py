from itertools import combinations_with_replacement
from collections import Counter

# 주어진 조합에서 각각의 점수 계산
def calculate_score(combi, info):
  score1, score2 = 0, 0
  for i in range(1, 11):
    if info[10 - i] < combi.count(i): # 점수별 개수 비교
      score1 += i
    elif info[10 - i] > 0:
      score2 += i
  return  score1, score2

# 최대 차이와 조합 저장
def calculate_best_combination(n, info):
  max_diff = 0
  max_comb = {}

for combi in combinations_with_replacement(range(11), n):
  cnt = Counter(combi) # 조합 튜플에서 등장한 숫자의 개수를 계산하여 딕셔너리 형태로 반환
  score1, score2 = calculate_score(combi, info)
  diff = score1 - score2

  if diff > max_diff:
    max_diff = diff
    max_comb = cont

return max_diff, max_comb

def solution(n, info):
  max_diff, max_comb = calculate_best_combination(n, info):

  if max_diff > 0:
    answer = [0] * 11
    for score in max_comb:
      answer[10 - score] = max_comb[score]
    return answer
  else:
    return [-1]



'''
결론: 문제를 보면 이렇게 생각하는 연습을 하자!
1️⃣ 핵심 목표 먼저 찾기
✔️ "라이언이 n발을 쏴서 어피치를 이길 수 있는 조합을 찾기"

2️⃣ 탐색 방법 결정
✔️ "완전 탐색 필요 → 중복 조합(combinations_with_replacement) 사용"

3️⃣ 개별 계산 함수 만들기
✔️ calculate_score() → 현재 조합에서 라이언과 어피치의 점수를 계산

4️⃣ 최적 조합을 찾는 함수 구현
✔️ calculate_best_combination() → 최대 점수 차이를 찾기

5️⃣ 최종적으로 정답 형식으로 변환
✔️ solution() → max_comb을 [0, 0, ...] 형태로 변환


🔥 문제를 처음 맞닥뜨렸을 때 느끼는 막막함과 압박감을 해소하려면?
이게 가장 자연스러운 감정이야! 하지만, 이걸 줄이는 방법이 있어.
핵심은 **문제를 "잘게 쪼개서 하나씩 해결하는 연습"**을 하는 거야.
즉, 한 번에 완벽하게 풀려고 하지 말고, 문제를 구조적으로 분석하는 습관을 들이면 돼.

✅ 1. "압박감"을 해소하는 방법 → "문제를 구조적으로 나누는 연습"
🔹 처음 문제를 보면 막막한 이유는?

**"한 번에 정답을 내야 한다"**는 부담감
**"어디서부터 시작해야 할지 모른다"**는 불안감
**"이 문제가 익숙하지 않다"**는 두려움
💡 이걸 해결하려면? 👉 "당장 코드 짜지 말고 문제를 3~5개의 작은 조각으로 나누는 연습을 하자!"
👉 **"작은 조각부터 하나씩 해결하는 연습"**을 하면, 전체적으로 자연스럽게 정리된다.

🎯 예제: N-Queen 문제에서 처음 막막할 때
✔️ 처음엔 "N-Queen 어떻게 풀어?" 막막할 수 있음
✔️ 하지만, 이렇게 쪼개면?
✔️ "퀸을 한 줄씩 놓는 구조" → "백트래킹이 필요하네!"
✔️ "같은 열과 대각선 체크해야 함" → "is_safe() 함수 만들면 되겠네!"
✔️ "백트래킹을 쓰려면 DFS 구조로 탐색해야겠네!"
✔️ "모든 경우를 탐색하고 정답을 리턴하면 되네!"

🚀 이제 갑자기 문제의 난이도가 확 떨어진 것처럼 보일 거야!
이런 구조화 연습을 계속하면, 문제를 처음 봤을 때도 막막함이 줄어들 거야!

✅ 2. "구현력이 부족하다면?" → "코딩하는 습관을 바꾸자!"
문제를 구조화해서 논리적으로 이해했어도, 구현이 어렵다면 "구현 연습"이 부족한 거야!
구현 실력을 올리려면 3가지 방법이 있어!

🚀 1️⃣ "패턴을 찾아서 템플릿을 익혀라!"
코딩을 잘하는 사람들은 비슷한 유형의 문제를 풀 때 동일한 패턴을 사용함!
✔️ 예를 들어, "완전 탐색" 문제를 보면 **"DFS 또는 백트래킹 패턴"**이 떠올라야 함.
✔️ "최대 점수 차이를 구하는 문제"를 보면 "정렬 또는 DP" 패턴이 떠올라야 함.
✔️ 이런 패턴을 익히려면 같은 유형의 문제를 최소 3~5개 풀어봐야 함!

💡 👉 연습 방법:
✅ 백트래킹 문제 5개를 정해서 패턴 분석
✅ DFS/BFS 문제 5개를 정해서 패턴 분석
✅ 그리디 문제 5개를 정해서 패턴 분석

🚀 이런 식으로 유형을 익히면, 새로운 문제를 봤을 때 "아, 이건 백트래킹이겠네!" 하고 바로 접근 가능해짐!

🚀 2️⃣ "일부 기능만 먼저 구현하는 연습을 해라!"
많은 사람들이 "한 번에 문제를 완성하려고 해서" 막힘.
그러지 말고, 문제에서 필요한 기능을 먼저 구현하고 테스트하는 습관을 들이자.

💡 👉 예제: 점수 계산이 핵심이라면?
✅ calculate_score() 먼저 구현하고 실행해보기
✅ 결과가 맞는지 확인한 후, 이제 combinations_with_replacement() 적용해보기
✅ 마지막으로 solution()을 완성하기

🚀 이렇게 하면 코드가 길어져도 "조각조각 완성"할 수 있음!

🚀 3️⃣ "직접 손으로 써보면서 생각하는 연습을 하라!"
✔️ 코드를 바로 작성하려 하지 말고, 종이에 흐름을 적어보자!
✔️ for문이 어디서 도는지, dfs()가 어떻게 호출되는지 흐름을 그려보면 논리가 정리됨.
✔️ 특히 재귀(백트래킹, DFS, 분할정복) 문제는 무조건 손으로 트리 구조를 그려야 이해가 잘 됨!

🎯 이제 정리해보자!
1️⃣ "압박감을 줄이려면?"

문제를 바로 해결하려 하지 말고, 작은 단위로 나눠서 해결하자!
"이 문제는 크게 3가지 부분으로 나뉜다!" 하고 구조화하는 연습
2️⃣ "구현 실력을 늘리려면?"

비슷한 유형 문제를 최소 3~5개 풀면서 패턴 익히기!
한 번에 풀려고 하지 말고, 먼저 부분 기능부터 구현해보기!
손으로 흐름을 정리하고, 생각을 정리한 후 코드로 옮기기!
🚀 이제 실천해보자!
✔️ 지금 풀고 있는 문제에서 **"핵심 로직을 먼저 구현하고 테스트하는 방식"**으로 해보자!
✔️ 유형별로 문제를 5개 정도 연속으로 풀면서 패턴을 익혀보자!
✔️ 코드를 바로 짜려 하지 말고, 손으로 문제를 정리하는 연습을 하자!

이걸 반복하면,
"이 문제 처음 보는데... 막막하지 않네?"
"구현도 한 번에 되는 느낌이네?"
이런 순간이 올 거야! 🚀🔥

💡 이제 실행에 옮겨보자! "문제를 풀면서 새로운 방식으로 접근해보는 것"이 가장 중요해! 💡

'''

# 1. 아이디어 : 
# 장르별 재생수를 적절한 자료구조 형식으로 변환.
# 장르별 재생수 합을 구하여 가장 많이 재생된 장르순으로 정렬해야함. 
# 가장 많이 재생된 장르부터 상위 2개, 장르에 곡이 1개 일경우는 1개 씩 해서 베스트 앨범에 수록하면 됨. 근데 원래 인덱스 번호를 반환해야함.

# 2. 시간 복잡도 : 최대 1만개, 정렬 NlogN + 기타등등 이라 NlogN 벗어나지 않을 듯. 최대는 N^2 언저리도 가능은 해보임.
# 3. 자료 구조 : 이런 데이터는 처음에 defaultdict 구조로 받는 것이 좋은 것 같음.

from collections import defaultdict


def solution(genres, plays):
    answer = []
    # 1. 장르별 재생 횟수와 노래 정보(고유 번호, 재생 횟수) 저장
    genre_total_plays = defaultdict(int)
    genre_songs = defaultdict(list)
    
    # 장르별 재생 횟수 합계와 노래별 정보를 기록
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        genre_total_plays[genre] += play
        genre_songs[genre].append((play, i))
                
    # 2. 장르별 재생 횟수를 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_total_plays.keys(), key=lambda g: genre_total_plays[g], reverse=True) 
    
    # 3. 각 장르에서 재생 횟수별로 정렬 후, 상위 2곡씩만 추출
    for genre in sorted_genres:
        # 장르 내에서 노래를 재생 횟수 내림차순, 재생 횟수가 같으면 고유 번호 오름차순으로 정렬
        genre_songs[genre].sort(key=lambda x: (-x[0], x[1])) # genre_songs[genre]라고 하면 (),(),() 이런 형식으로 들어가있지?, 그리고 여기도 정렬 함수 쓰는거 진짜 어렵네 ㅜ, 혹시 시험치다가 까먹으면 대체 방법있나? 직관적이고 쉬운걸로 ㅠ
        # 상위 2곡 추출
        answer.extend([song[1] for song in genre_songs[genre][:2]]) # extend랑 append랑 뭐가 다른가?, # 이 코드 설명좀
    
    # sorted이거 쓰면서 key랑 lambda 하는거 연습문제 달라고해서 연습해야할듯.
    return answer


#     defaultdict 만들고 , genres, plays를 동시에 하나씩 돌면서 (map 사용하면 될 것 같음)
    
#     classic : 500, 150, 800 이 들어가긴하는데 인덱스도 같이 들어가야할듯 
#             그러면 (0, 500), (2,150) 이런식으로 넣고
#             genre_name[0] = index
#             genre_name[1] = play
#     합 비교는 defaultdict만들때 genres, plays를 도니까, 합 리스트 만들어서 넣고 sort하면 인덱스도 같이 나올듯!# 이건 틀린 듯
# 아 아까도 썼는데 max 구해서 인덱스로 반환하는거 이 부분 알려줘 까먹음 ㅜ.
# 이 부분은 안쓰긴 한데 질문에 답해줘.,. 이거보다 효율적인 방법 있잖아.
    # max_val = max(S)
    # max_idx = 0
    # for idx in S:
    #     if S[idx] == max_val:
    #         max_idx = idx
# 아 근데 max idx를 구하는게 아니고 그냥 sort하는거였네 헷갈렸다. dict를 sum에 따라 sort하고 그 idx에 맞게? 어떻게 같이 추적하는 코드를 짜지? 이 부분이 부족하네 지금.
# 암튼 그렇게 따라 추적해서 조건문에 따라 큰 순으로 2개, 1개면 1개 빼서 가져와서 인덱스를 answer에 순서대로 넣기.

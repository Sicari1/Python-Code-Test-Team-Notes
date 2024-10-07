def counting_sort(arr):
    # 입력 배열에서 최대값을 찾음
    max_val = max(arr)

    # 카운트 배열을 생성 (0으로 초기화)
    count = [0] * (max_val + 1)

    # 각 숫자의 등장 횟수를 카운트 배열에 저장
    for num in arr:
        count[num] += 1

    # 누적 카운트를 계산하여 정렬된 배열의 인덱스를 결정
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 정렬 결과를 저장할 배열
    sorted_arr = [0] * len(arr)

    # 입력 배열을 역순으로 탐색하여 각 값을 정렬된 위치에 배치 (안정적인 정렬 보장)
    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr

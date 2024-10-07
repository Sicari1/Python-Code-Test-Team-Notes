# insertion_sort.py
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# 예시 코드
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    sorted_arr = insertion_sort(arr)
    print("정렬된 배열:", sorted_arr)

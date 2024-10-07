# heap_sort.py
import heapq

def heap_sort(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    sorted_arr = [heapq.heappop(heap) for _ in range(len(heap))]
    return sorted_arr

# 예시 코드
if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19]
    sorted_arr = heap_sort(arr)
    print("정렬된 배열:", sorted_arr)

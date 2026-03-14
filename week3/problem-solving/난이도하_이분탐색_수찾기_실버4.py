# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# data_number = int(input())
# compare_data = list(map(int, input().split()))
# data_number = int(input())
# check_data = list(map(int, input().split()))

# result = [0] * len(check_data)

# for i in range(len(check_data)):
#     if check_data[i] in compare_data:
#         print(i)

# for i in result:
#     print(i)


# 1. 이분 탐색의 오른쪽 범위가 잘못됨
# 2. 반복 조건이 left < right라서 마지막 1칸을 검사 못 함
def binary_search(arr, left, right, target):

    while left <= right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


def merge(arr, left, mid, right):
    left_arr = arr[left : mid + 1]
    right_arr = arr[mid + 1 : right + 1]

    left_arr.append(99999999999999999999)
    right_arr.append(99999999999999999999)
    i = 0
    j = 0
    for k in range(left, right + 1):
        if left_arr[i] > right_arr[j]:
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = left_arr[i]
            i += 1


def merge_helper(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_helper(arr, left, mid)
    merge_helper(arr, mid + 1, right)
    merge(arr, left, mid, right)


def main(arr):
    if len(arr) > 1:
        merge_helper(arr, 0, len(arr) - 1)
        return arr
    else:
        return arr


data_number = int(input())
compare_data = list(map(int, input().split()))
data_number = int(input())
check_data = list(map(int, input().split()))

sorted_compare_data = main(compare_data)

for i in range(len(check_data)):
    data = check_data[i]
    result = binary_search(compare_data, 0, len(compare_data) - 1, data)
    if result:
        print(1)
    else:
        print(0)

# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline
meeting_count = int(input().strip())

meeting_schedule = []
for _ in range(meeting_count):
    meeting_component = tuple(map(int,input().split()))
    meeting_schedule.append(meeting_component)

def merge(arr,left,right):
    mid = (left + right)  // 2
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]

    left_arr.append((999999999999999,9999999999999999))
    right_arr.append((999999999999999,9999999999999999))
    i = 0
    j = 0
    for k in range(left,right+1):
        if left_arr[i][1] == right_arr[j][1]:
            if left_arr[i][0] > right_arr[j][0]:
                arr[k] = right_arr[j]
                j += 1
            else:
                arr[k] = left_arr[i]
                i += 1
        elif left_arr[i][1] > right_arr[j][1]:
            arr[k] = right_arr[j]
            j += 1
        else:
            arr[k] = left_arr[i]
            i += 1
def merge_init(arr,left,right):
    if left >= right:
        return 
    
    mid = (left + right) //2 
    merge_init(arr,left,mid)
    merge_init(arr,mid+1, right)
    merge(arr,left,right)
def start(arr):
    if len(arr) == 0:
        return arr
    else:
        merge_init(arr,0,len(arr)-1)
        return arr

sorted_meeting_schedule = start(meeting_schedule)

return_array = []

return_array.append(sorted_meeting_schedule[0])
for i in range(1,len(sorted_meeting_schedule)):
    if sorted_meeting_schedule[i][0] >= return_array[-1][1]:
        return_array.append(sorted_meeting_schedule[i])
print(len(return_array))
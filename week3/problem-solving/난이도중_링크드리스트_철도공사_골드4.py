# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309

import sys

n, m = list(map(int, sys.stdin.readline().rstrip("\n").split()))
station_num_list = sys.stdin.readline().rstrip("\n").split()

work_list = []
for _ in range(m):
    work_list.append(sys.stdin.readline().rstrip("\n").split())



class Node:
    def __init__(self, station_num):
        self.station_num = station_num
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self,arr:list[str]):
        a
    
    def bn_function(work):
        i,j = work[1:]
    def bp_function(work):
        i,j = work[1:]
    def cp_function(work):
        i = work[1]
    def cn_function(work):
        i = work[1]
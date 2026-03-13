# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164
from collections import deque


number = int(input())

queue = deque(range(1, number + 1))

status = False

while len(queue) > 1:
    if not status:
        queue.popleft()
        status = not status
    else:
        data = queue.popleft()
        queue.append(data)
        status = not status

print(queue.pop())

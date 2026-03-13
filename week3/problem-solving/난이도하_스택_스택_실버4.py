# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

order_number = int(input())

order_list = [input() for _ in range(order_number)]

stack = []

for i in order_list:
    if "push" in i:
        push_data = int(i.split()[-1])
        stack.append(push_data)
    elif "top" == i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif "empty" == i:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "size" == i:
        print(len(stack))
    elif "pop" == i:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

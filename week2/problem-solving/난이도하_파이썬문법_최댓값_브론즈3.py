# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

problem_array = []
for i in range(9):
    problem_array.append(int(input()))


max_number = -1
max_index = -1
for i in range(len(problem_array)):
    if max_number < problem_array[i]:
        max_number = problem_array[i]
        max_index = i + 1
print(f"{max_number}\n{max_index}\n")

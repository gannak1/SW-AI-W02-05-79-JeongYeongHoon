# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

length = int(input())  # 처음 들어오는 데이터의 개수
data = [input() for _ in range(length)]  # 실제 데이터

data_dict = {}  # 데이터를 담기 위한 딕셔너리
answer = ""  # 정답

for i in data:
    data_dict[i] = False  # 데이터를 딕셔너리에 넣기
    if i[::-1] in data_dict:  # 반대로 된 글자가 있으면 정답처리
        answer = i
        break

print(f"{len(answer)} {answer[len(answer) // 2]}")

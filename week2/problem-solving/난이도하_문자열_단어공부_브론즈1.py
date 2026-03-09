# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

"""
전체 단어 개수와 i로 스플릿한 단어의 수 차를 구해서 max_count인데 같은 개수이면 is_same을 True로 만들어서 ?를 출력 아니면 가장 많은 단어 출력
"""

word = input().lower()

max_count = -1
max_word = ""
is_same = False
for i in set(word):
    same_word_count = len(word) - len("".join(word.split(i)))
    if max_count < same_word_count:
        max_count = same_word_count
        max_word = i
        is_same = False
    elif max_count == same_word_count:
        is_same = True

if is_same:
    print("?")
else:
    print(max_word.upper())

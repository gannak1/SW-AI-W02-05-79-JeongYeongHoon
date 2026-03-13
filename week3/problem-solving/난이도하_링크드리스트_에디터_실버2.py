# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, head):
        self.cursor = head
        self.last_word = Node("")
        self.next_node_connect(self.cursor, self.last_word)
        self.first_word = Node("")
        self.next_node_connect(self.first_word, head)

    def next_node_connect(self, prev_node, next_node):
        """prev_node <-> next_node"""
        prev_node.next = next_node
        next_node.prev = prev_node

    def append(self, data):
        if len(data) == 0:
            return
        for i in range(len(data)):
            new_node = Node(data[i])
            self.next_node_connect(
                self.last_word.prev, new_node
            )  # 원래 끝단어와 새로운 단어을 prev - next로 연결
            self.next_node_connect(
                new_node, self.last_word
            )  # 새로운 단어와 마지막 빈공간을 prev - next로 연결

        self.cursor = self.last_word

    def print_all(self):
        word = []
        last_node = self.first_word.next
        while last_node.next != None and last_node.next != self.last_word:
            word.append(last_node.data)
            last_node = last_node.next
        word.append(last_node.data)
        return "".join(word)

    def prev_cursor(self):
        prev_cursor = self.cursor.prev
        if prev_cursor == self.first_word:
            return
        else:
            self.cursor = prev_cursor

    def next_cursor(self):
        next_cursor = self.cursor.next
        if next_cursor == None:
            return
        else:
            self.cursor = next_cursor

    def delete_prev(self):
        if self.cursor.prev == self.first_word:
            return
        elif self.cursor.prev.prev != None:
            if self.cursor.prev == self.last_word.prev:
                self.last_word.prev = self.cursor.prev
            self.next_node_connect(self.cursor.prev.prev, self.cursor)

    def insert_data(self, data):
        new_node = Node(data)
        if self.cursor.prev == self.first_word:
            self.first_word.next = new_node

        self.next_node_connect(self.cursor.prev, new_node)
        self.next_node_connect(new_node, self.cursor)

    def command_key(self, key_data):
        if key_data == "L":
            self.prev_cursor()
        elif "P" == key_data[0]:
            self.insert_data(key_data.split()[-1])
        elif "D" == key_data:
            self.next_cursor()
        elif "B" == key_data:
            self.delete_prev()


first_word = sys.stdin.readline().rstrip("\n")
editor = LinkedList(Node(first_word[0]))
editor.append(first_word[1:])
input_count = int(sys.stdin.readline().rstrip("\n"))
command_list = []
for _ in range(input_count):
    command_list.append(sys.stdin.readline().rstrip("\n"))
for i in range(len(command_list)):
    editor.command_key(command_list[i])
print(editor.print_all())

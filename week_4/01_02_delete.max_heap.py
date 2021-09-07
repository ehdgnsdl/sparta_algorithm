class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 루트노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소를( 원래 루트 노드)를 삭제합니다. 이 때, 끝에 반환해줘야 하니까 저장해둡시다.
    # 3. 변경된 노드와 자식 노드를 비교합니다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿔주자.
    # 4. 자식 노드 둘 보다 부모 노드가 더 크거나 가장 바닥에 도달하지 않을 때까지 3.을 반복합니다.
    # 5. 2. 에서 제거한 원래 루트 노드를 반환합니다.
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index
            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]
            cur_index = max_index
        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

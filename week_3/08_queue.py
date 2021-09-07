class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    # head   tail
    # [4] -> [2] -> [3]
    # self.tail.next = new_node
    #
    # new_node = Node(3) #[3]
    # head          tail
    # [4] -> [2] -> [3]
    # self.tail = new_node

    # head tail
    # None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    # head          tail
    # [4] -> [2] -> [3]

    # delete_head = self.head
    # self.head = self.head.next
    #        head   tail
    # [4] -> [2] -> [3]
    # return delete_head
    # head  tail
    # [2] -> [3] 반환! [4]
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data


    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


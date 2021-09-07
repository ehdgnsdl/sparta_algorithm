class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:  # k는 key, v는 values
            if key == k:  # 만약 key랑 k가 같다면
                return v  # items의 v 출력


class LinkedDict:
    def __init__(self):
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # LinkedTuple
        # []
        # [(key, value)]
        self.items[index].add(key, value)

    def get(self, key):
        index = hash(key) % len(self.items)
        # Linked Tuple
        # [(key1, value1), (key, value)]
        return self.items[index].get(key)

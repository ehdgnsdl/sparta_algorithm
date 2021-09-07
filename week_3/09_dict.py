class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items) # 0~7사이
        #
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)  # 0~7사이
        return self.items[index]

my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
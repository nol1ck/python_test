class Ticker:

    def __init__(self, data):
        self.data = data
        self. keys = list()
        self.values = list()

    def destructor_json(self):
        for item in self.data:
            self.keys.append(item['symbol'])
            self.values.append(item['price'])
        return self.keys, self.values

    def create_list(self):
        keys, values = self.destructor_json()
        return dict(zip(keys, values))

class Index:
    def __init__(self, text):
        self.text = text

    def sorting(self):
        count = {}
        for i in self.text:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        sorted_tuple = sorted(count.items(), key=lambda x: x[0])
        one_sorting = dict(sorted_tuple)
        return one_sorting

    def shift(self, value_shift: int):
        rotated_values = deque(sorting(self.text).values())
        rotated_values.rotate(value_shift)
        new_dict = {k: v for k, v in zip(sorting(self.text), rotated_values)}
        return new_dict

    def all_count(self):
        count = {}
        for i in self.text:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        d_count = list(count.values())
        new_list = []
        for i in d_count:
            g = (i * (i - 1)) / (len(self.text) * (len(self.text) - 1))
            new_list.append(g)
        return sum(new_list)

    def sum_values(self, text):
        count = {}
        for i in text:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return sum(list(count.values()))

    def text_slice(self, step):
        i = 0
        spis = []
        while i < step:
            spis.append(self.text[i::step])
            i += 1
        else:
            for b in spis:
                print(b)

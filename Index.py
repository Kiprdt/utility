class Index:
    print('Methods: sorting(), shift(int), sum_values(text)')

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

    def sum_values(self, text):
        count = {}
        for i in text:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return sum(list(count.values()))

class MatchIndex:
    def __init__(self, text: str = ''):
        self.text = text

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

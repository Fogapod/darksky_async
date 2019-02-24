from .datapoint import DataPoint

class DataBlock():
    __slots__ = ('icon', 'summary', 'data')
    def __init__(self, icon, summary, data):
        self.icon = icon
        self.summary = summary
        self.data = []
        for item in data:
            self.data.append(DataPoint(**item))


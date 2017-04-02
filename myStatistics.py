import random

class Statistics(object):

    def __init__(self, dataList):
        self._data = dataList
        self._average = float(sum(self._data))/len(self._data)
        self._variance = sum(map(lambda x:pow((x - self._average), 2), self._data))/len(self._data)

    @property
    def average(self):
        return self._average

    @property
    def variance(self):
        return self._variance

    def printData(self):
        print ("Descriptive statistics: ")
        print ("Length of datas: ", len(self._data))
        print ("Average of datas: ", self._average)
        print ("Variance of datas: ", self._variance)

class sample(Statistics):
    pass
    
    

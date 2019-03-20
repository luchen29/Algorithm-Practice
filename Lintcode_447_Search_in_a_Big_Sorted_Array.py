"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
        # return the number on given index,
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        n = 0
        index = 2 ** n
        while True:
            index += 2**n
            k_num = reader.get(index)
            if k_num < target:
                n += 1
            else: break
        return self.BinarySearch(reader,index,target)

    def BinarySearch(self, reader, index, target):
        start = 0
        end = index
        while start+1<end:
            middle = (start+end)//2
            if reader.get(middle) >= target:
                end = middle
            else:
                start = middle
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
# 倍增求结尾位置，二分进行搜索

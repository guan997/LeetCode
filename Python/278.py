#278. 第一个错误的版本
#假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.__class__.__getitem__ = lambda self, x: isBadVersion(x)
        return bisect.bisect_left(self, True, 1, n)
#改造当前类的魔法方法getitem以使用内置函数
        

#1. 两数之和
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

'''
def twoSum(nums, target):
        _dict={}
        for i , m in enumerate(nums):
            if _dict.get(target - m)is not None:
                return [_dict.get(target - m),i]
            _dict[m] = i
print(twoSum([3,5,6,7],11))

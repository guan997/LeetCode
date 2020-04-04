#88合并两个有序数组
 def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
              nums1[:] = sorted(nums1[:m] + nums2)

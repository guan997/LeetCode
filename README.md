# LeetCode

#### [237. 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)

难度简单

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/237_example.png)

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
由于只输入了需要删除的节点node，因此无法获取删除节点node的前一个节点pre，从而也就无法将前一个节点pre指向删除节点的下一个节点nex；既然无法通过修改指针完成，那么肯定要修改链表节点的值了。将删除节点node的值和指针都改为下一个节点nex的值和指针即可。

#### [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

难度简单

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2
备注： 在 Python 中，and 和 or 都有提前截至运算的功能。

and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
例子：[] and 7 等于 []
代码流程：（按行数）

判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
对 l1 和 l2 重新赋值，使得 l1 指向比较小的那个节点对象
修改 l1 的 next 属性为递归函数返回值
返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None

#### [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)

难度简单

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 `true` 。如果数组中每个元素都不相同，则返回 `false` 

解法1：集合法
判断原数组和该数组的长度相不相等，一行解决：

    def containsDuplicate(self, nums: List[int]) -> bool:
        return len((set(nums))) != len(nums)
解法2：哈希表
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if dic.get(i):
                return True
            dic[i] = 1
        return False
解法3：排序法
排序之后，相等元素必相邻：

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return True
        return False

#### [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

难度简单

给定一个排序数组，你需要在** 原地** 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 **原地 修改输入数组 **并在使用 O(1) 额外空间的条件下完成。

用两个指针，指向第一个和第二个元素，如果他们相等，删除第二个元素。指针还指向原来的位置，继续比较。不等的话，两个指针位置都加一。遍历结束即可。

    def removeDuplicates(self, nums: List[int]) -> int:
        pre,cur=0,1
        while cur<len(nums):       
            if nums[pre]==nums[cur]:
                nums.pop(cur)
            else:
                pre,cur=pre+1,cur+1
        return len(nums)
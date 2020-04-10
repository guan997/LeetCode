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

[88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

难度简单

给你两个有序整数数组 *nums1 *和 *nums2*，请你将 *nums2 *合并到 *nums1 *中*，*使 *num1 *成为一个有序数组。

**说明:**

- 初始化 *nums1* 和 *nums2* 的元素数量分别为 *m* 和 *n *。
- 你可以假设 *nums1 *有足够的空间（空间大小大于或等于 *m + n*）来保存 *nums2* 中的元素。

**示例:**

```
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
```

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
               nums1[:] = sorted(nums1[:m] + nums2)

将两个数组合并之后再排序。

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
#### [136. 只出现一次的数字](https://leetcode-cn.com/problems/single-number/)

难度简单

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

**说明：**

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

**示例 1:**

```
输入: [2,2,1]
输出: 1

```

**示例 2:**

```
输入: [4,1,2,1,2]
输出: 4
```

    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a
异或运算

- 交换律：a ^ b = b ^ a
- 任何数与0异或为其本身 0 ^ n = n
- 相同的数异或为0: n ^ n = 0

#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

难度简单

给定一个大小为 *n *的数组，找到其中的多数元素。多数元素是指在数组中出现次数**大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

**示例 1:**

```
输入: [3,2,3]
输出: 3
```

**示例 2:**

```
输入: [2,2,1,1,1,2,2]
输出: 2
```

###### 方法一：哈希表

思路

我们知道出现次数最多的元素大于 [n/2] 次，所以可以用哈希表来快速统计每个元素出现的次数。

算法

我们使用哈希映射（HashMap）来存储每个元素以及出现的次数。对于哈希映射中的每个键值对，键表示一个元素，值表示该元素出现的次数。

我们用一个循环遍历数组 nums 并将数组中的每个元素加入哈希映射中。在这之后，我们遍历哈希映射中的所有键值对，返回值最大的键。我们同样也可以在遍历数组 nums 时候使用打擂台的方法，维护最大的值，这样省去了最后对哈希映射的遍历。

    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
###### 方法二：排序

思路

如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为[n/2] 的元素（下标从 0 开始）一定是众数。

算法

对于这种算法，我们先将 nums 数组排序，然后返回上文所说的下标对应的元素。下面的图中解释了为什么这种策略是有效的。在下图中，第一个例子是 n为奇数的情况，第二个例子是 n 为偶数的情况。

{0,1,2,3,4,5,6}

{0,1,2,3,4,5}

对于每种情况，数组下面的线表示如果众数是数组中的最小值时覆盖的下标，数组下面的线表示如果众数是数组中的最大值时覆盖的下标。对于其他的情况，这条线会在这两种极端情况的中间。对于这两种极端情况，它们会在下标为 [n/2]的地方有重叠。因此，无论众数是多少，返回 [n/2] 下标对应的值都是正确的。

    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
复杂度分析

时间复杂度：O(n\log n)。将数组排序的时间复杂度为 O(n\log n)。

空间复杂度：O(\log n)。如果使用语言自带的排序算法，需要使用 O(\log n) 的栈空间。如果自己编写堆排序，则只需要使用 O(1) 的额外空间。

###### 方法三：Boyer-Moore 投票法思路

根据上述的算法思想，我们遍历投票数组，将当前票数最多的候选人与其获得的（抵消后）票数分别存储在 major 与 count 中。

当我们遍历下一个选票时，判断当前 count 是否为零：

若 count == 0，代表当前 major 空缺，直接将当前候选人赋值给 major，并令 count++
若 count != 0，代表当前 major 的票数未被完全抵消，因此令 count--，即使用当前候选人的票数抵消 major 的票数

以 [2,2,1,3,1,2,2] 为例。

遍历数组第一个元素 2 时，因 major 空缺，所以赋值 major = 2，且票数 count = 1：

我们发现第二个元素依旧是「候选人」2，与 major 相同，因此将票数加一：

第三个元素是 1，与 major 不同，因此发生「对抗」，将当前 major 的票数冲抵掉 1 票：

第四个元素是 3，又与 major 不同，因此产生「对抗」，票数继续冲抵：

当遍历到第五个元素 1 时，我们发现当前 count 已经归 0，说明 major 位置空缺，因此我们令 major = 1，且 count = 1：

第六个元素是 2，与 major 不同，因此进行票数抵消，元素 1 刚上位又要下台了：

此时 count 又归零了，因此当遍历到最后一个元素 2 时，令 major = 2，票数 count = 1：

至此遍历结束，求出的多数元素为元素 2。

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        count = 0
        
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count = count + 1
            else:
                count = count - 1
    
        return major

### 复杂度

- 时间复杂度：O(n)，仅遍历一次数组
- 空间复杂度：O(1)，没有使用额外空间

#### [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

难度中等

给定一个字符串，逐个翻转字符串中的每个单词。

**示例 1：**

```
输入: "the sky is blue"
输出: "blue is sky the"

```

**示例 2：**

```
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

```

**示例 3：**

```
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
```

**说明：**

- 无空格字符构成一个单词。
- 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
- 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

```
str.strip([chars]);方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
chars -- 移除字符串头尾指定的字符序列。
```

    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        strs = s.split() # 分割字符串
        strs.reverse() # 翻转单词列表
        return ' '.join(strs) # 拼接为字符串并返回

```
  # return ' '.join(s.strip().split()[::-1])
```

#### [125. 验证回文串](https://leetcode-cn.com/problems/valid-palindrome/)

难度简单

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

**说明：**本题中，我们将空字符串定义为有效的回文串。

**示例 1:**

```
输入: "A man, a plan, a canal: Panama"
输出: true

```

**示例 2:**

```
输入: "race a car"
输出: false
```

```
str.isalnum()方法检测字符串是否由字母和数字组成。
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
```

```
str.lower()方法转换字符串中所有大写字符为小写。
返回将字符串中所有大写字符转换为小写后生成的字符串。
```

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]
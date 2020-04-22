# LeetCode

#### 关于LeetCode的Python和JavaScript解答

13罗马数字转整数

14. 最长公共前缀

20有效的括号

350

108

28实现strStr()

#### [1. 两数之和](https://leetcode-cn.com/problems/two-sum/)

难度简单

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

JS：

初始化一个 map = new Map()
从第一个元素开始遍历 nums
获取目标值与 nums[i] 的差值，即 k = target - nums[i] ，判断差值在 map 中是否存在
不存在（ map.has(k) 为 false ） ，则将 nums[i] 加入到 map 中（key为nums[i], value为 i ，方便查找map中是否存在某值，并可以通过 get 方法直接拿到下标）
存在（ map.has(k) ），返回 [map.get(k), i] ，求解结束
遍历结束，则 nums 中没有符合条件的两个数，返回 []
时间复杂度：O(n)

```py
 /**

- @param {number[]} nums
- @param {number} target
- @return {number[]}
  */
  var twoSum = function(nums, target) {
  let map=new Map()
  for(let i=0;i<nums.length;i++){
	let k=target-nums[i]
	if(map.has(k)){
  		 return [map.get(k),i];
   }
	 map.set(nums[i],i)
}
 return [];

};
```

PY

enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

enumerate(sequence, [start=0])

sequence -- 一个序列、迭代器或其他支持迭代对象。

start -- 下标起始位置。

seq = ['one', 'two', 'three']

for i, element in enumerate(seq):

print i, element		(0 one 1 two 2 three)

```python
def twoSum(nums, target):
    hashmap={}
for ind,num in enumerate(nums):
    hashmap[num] = ind
for i,num in enumerate(nums):
    j = hashmap.get(target - num)
    if j is not None and i!=j:
        return [i,j]
```

#### [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

难度简单865收藏分享切换为英文关注反馈

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 写做 `XII` ，即为 `X` + `II` 。 27 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

**示例 1:**

```
输入: "III"
输出: 3
```

**示例 2:**

```
输入: "IV"
输出: 4
```

**示例 3:**

```
输入: "IX"
输出: 9
```

**示例 4:**

```
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

```

**示例 5:**

```
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

js

首先将所有的组合可能性列出并添加到哈希表中
然后对字符串进行遍历，由于组合只有两种，一种是 1 个字符，一种是 2 个字符，其中 2 个字符优先于 1 个字符
先判断两个字符的组合在哈希表中是否存在，存在则将值取出加到结果 ans 中，并向后移2个字符。不存在则将判断当前 1 个字符是否存在，存在则将值取出加到结果 ans 中，并向后移 1 个字符
遍历结束返回结果 ans

代码

```javascript
/**
- @param {string} s
- @return {number}
  */
  var romanToInt = function(s) {
  const map = {
	    I : 1,
        IV: 4,
        V: 5,
        IX: 9,
        X: 10,
        XL: 40,
        L: 50,
        XC: 90,
        C: 100,
        CD: 400,
        D: 500,
        CM: 900,
        M: 1000

	};

let ans = 0;

for(let i = 0;i < s.length;) {

    if(i + 1 < s.length && map[s.substring(i, i+2)]) {
        ans += map[s.substring(i, i+2)];
        i += 2;
    } else {
        ans += map[s.substring(i, i+1)];
        i ++;
    }
}
       return ans;
};
```

py

建立一个HashMap来映射符号和值，然后对字符串从左到右来，如果当前字符代表的值不小于其右边，就加上该值；否则就减去该值。以此类推到最左边的数，最终得到的结果即是答案

```python
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}        
        ans=0        
        for i in range(len(s)):            
            if i<len(s)-1 and a[s[i]]<a[s[i+1]]:                
                ans-=a[s[i]]
            else:
                ans+=a[s[i]]
        return ans
```

#### [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

难度简单

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

**示例 1:**

```
输入: ["flower","flow","flight"]
输出: "fl"

```

**示例 2:**

```
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

```

**说明:**

所有输入只包含小写字母 `a-z` 。

JS

解题思路

当字符串数组长度为 0 时公共前缀为空，直接返回
初始化，令最长公共前缀 ans 的值为第一个字符串
遍历后面的字符串，依次将其与 ans 进行比较，两两找出公共前缀，最终结果即为最长公共前缀
如果查找过程中出现了 ans 为空的情况，则公共前缀不存在直接返回

```js
/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length == 0) 
        return "";
    let ans = strs[0];
    for(let i =1;i<strs.length;i++) {
        let j=0;
        for(;j<ans.length && j < strs[i].length;j++) {
            if(ans[j] != strs[i][j])
                break;
        }
        ans = ans.substr(0, j);
        if(ans === "")
            return ans;
    }
    return ans;
};
```

py

```py
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        s = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(s) != 0 :
                s = s[:-1]
        return s
```

#### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

难度简单

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

**示例 1:**

```
输入: "()"
输出: true

```

**示例 2:**

```
输入: "()[]{}"
输出: true

```

**示例 3:**

```
输入: "(]"
输出: false

```

**示例 4:**

```
输入: "([)]"
输出: false

```

**示例 5:**

```
输入: "{[]}"
输出: true
```

py

使用replace()替代括号，最后判断字符串

```py
class Solution:
    def isValid(self, s: str) -> bool:
        while '{}' in s or '()' in s or '[]' in s:
            s=s.replace('{}','')
            s=s.replace('[]','')
            s=s.replace('()','')
        return s==''
```

js

解题思路

边遍历边匹配。也就是遍历的时候遇到左括号存入数组，下次遇到的第一个右括号必须和数组中最后一个元素匹配，否则为无效字符串，匹配完成后从数组中删除此元素。若最终数组为空，表示括号已全部匹配完，字符串有效。

```js
var isValid = function (s) {
    var map = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    var leftArr = []
    for (var ch of s){
        if (ch in map) leftArr.push(ch); //为左括号时，顺序保存
        else { //为右括号时，与数组末位匹配
            if(ch != map[leftArr.pop()]) return false;
        }
    }
    return !leftArr.length //防止全部为左括号
```

#### [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

难度简单

给你一个数组 *nums *和一个值 *val*，你需要 **原地** 移除所有数值等于 *val *的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 **原地 修改输入数组**。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**示例 1:**

```
给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。

```

**示例 2:**

```
给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

```

js

拷贝覆盖

遍历数组nums，每次取出的数字变量为num，同时设置一个下标ans
在遍历过程中如果出现数字与需要移除的值不相同时，则进行拷贝覆盖nums[ans] = num，ans自增1
如果相同的时候，则跳过该数字不进行拷贝覆盖，最后ans即为新的数组长度
这种思路在移除元素较多时更适合使用，最极端的情况是全部元素都需要移除，遍历一遍结束即

``` js
var removeElement = function(nums, val) {
    let ans = 0;
    for(const num of nums) {
        if(num != val) {
            nums[ans] = num;
            ans++;
        }
    }
    return ans;
};
```

交换移除

遍历数组nums，遍历指针为i，总长度为ans
在遍历过程中如果出现数字与需要移除的值不相同时，则i自增1，继续下一次遍历
如果相同的时候，则将nums[i]与nums[ans-1]交换，即当前数字和数组最后一个数字进行交换，交换后就少了一个元素，故而ans自减1
在移除元素较少时更适合使用，最极端的情况是没有元素需要移除，遍历一遍结束即可

```js
var removeElement = function(nums, val) {
    let ans = nums.length;
    for (let i = 0; i < ans;) {
        if (nums[i] == val) {
            nums[i] = nums[ans - 1];
            ans--;
        } else {
            i++;
        }
    }
    return ans;
};
```

#### [28. 实现 strStr()](https://leetcode-cn.com/problems/implement-strstr/)

难度简单

实现 [strStr()](https://baike.baidu.com/item/strstr/811469) 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  **-1**。

**示例 1:**

```
输入: haystack = "hello", needle = "ll"
输出: 2

```

**示例 2:**

```
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```

##### js

1、indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。

```js
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};
```

2、Sunday 匹配机制

```js
#超时
const strStr = function(haystack, needle) {
    if (needle === "") return 0;
    if (haystack === "") return -1;
    let inc = [];
    // 计算偏移量
    for (let i = 0; i < needle.length; i++) {
        for (let j = 0; j <= i; j++) {
            if (needle[j] !== needle[i - j]) {
                inc[i] = j + 1;
                break;
            }
            if (j === i && needle[j] === needle[i - j]) {
                inc[i] = j + 1;
            }
        }
    }
    let i = 0;
    let l = needle.length
    while (i < haystack.length) {
        for (let j = 0; j < l; j++) {
            if (needle[j] !== haystack[i + j]) {
                i += inc[j];
                break;
            }
            if (j === l - 1 && needle[j] === haystack[i + j]) {
                return i;
            }
        }
    }
    return -1;
};
```

#### [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

难度简单

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

**示例 1:**

```
输入: [1,3,5,6], 5
输出: 2

```

**示例 2:**

```
输入: [1,3,5,6], 2
输出: 1
```

js

```js
var searchInsert = function(nums, target) {
    let j=nums.indexOf(target);
    if(j!=-1)return j;


    for(let i = 0 ; i < nums.length; i++){
        if(nums[i]>target)return i;
    }
    return nums.length;
}
```



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

复杂度

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
#### [66. 加一](https://leetcode-cn.com/problems/plus-one/)

难度简单

给定一个由**整数**组成的**非空**数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储**单个**数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

**示例 1:**

```
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

```

**示例 2:**

```
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
```

1、将分开的数字变成一个整数，直接在整数上做加法就简单很多
2、再将str转变成int即可

    def plusOne(self, digits: List[int]) -> List[int]:
         ##先变成一个整的数字，然后做加法，然后转换成str,再转int加到新的list中
        nums_str = ""
        for i in digits:
            nums_str =nums_str+str(i)
    
        nums_int = int(nums_str)+1
        res = []
        for i in str(nums_int):
            res.append(int(i))
        return res
#### [387. 字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

难度简单

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

**案例:**

```
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
```

**注意事项：**您可以假定该字符串只包含小写字母。

##### PY

###### 第一种

Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）

c = Counter("abcdefgab")		>>>		 c["a"]2

```py
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):	
            if count[ch] == 1:
                return idx
        return -1
```

###### 第二种

 find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

```py
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for c in s:
            if s.find(c) == s.rfind(c):
                return s.find(c)
        return -1
```

###### js

##### 解题思路

遍历，若indexof===lastIndexOf则代表只出现一次

##### 代码

```js
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    for(let i=0;i<s.length;i++){
        if(s.indexOf(s[i])==s.lastIndexOf(s[i])){
           return i
           }
    }
    return -1
};
```

#### [189. 旋转数组](https://leetcode-cn.com/problems/rotate-array/)

难度简单

给定一个数组，将数组中的元素向右移动 *k *个位置，其中 *k *是非负数。

**示例 1:**

```
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

```

**示例 2:**

```
输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
```

**说明:**

- 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
- 要求使用空间复杂度为 O(1) 的 **原地 **算法。

##### js

##### 解题思路

1.使用while循环遍历，一次递减
2.将最后一个弹出，同时插入到第一个的位置
3.返回数组

- unshift() 方法可向数组的开头添加一个或更多元素，并返回新的长度。

- pop() 方法将删除 arrayObject 的最后一个元素，把数组长度减 1，并且返回它删除的元素的值。如果数组已经为空，则 pop() 不改变数组，并返回 undefined 值。

  ##### 代码

```js
/**
- @param {number[]} nums
- @param {number} k
- @return {void} Do not return anything, modify nums in-place instead.
  */
  var rotate = function(nums, k) {
  while (k>0) {
  nums.unshift(nums.pop())
  k = k-1
    }
    return nums
  };
```

##### py

##### 解题思路

切片
1、将-k个元素添加到nums的开始，
2、注意，为什么是nums[lenth-k:]而不是nums[-k:]，因为是为了避免k=0的情况

##### 代码

```py
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ##用切片的方法：k就是将nums的最后k个数放在nums的开始位置即可
    lenth = len(nums)
    nums[:] = nums[lenth-k:]+nums[:lenth-k]
```

#### [350. 两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

难度简单262收藏分享切换为英文关注反馈

给定两个数组，编写一个函数来计算它们的交集。

**示例 1:**

```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]

```

**示例 2:**

```
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
```

**说明：**

- 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
- 我们可以不考虑输出结果的顺序。

##### py

解题思路

利用python List中append与remove方法的特点进行操作。循环遍历nums1中的元素，然后在nums2中查找是否存在。如果存在，加入临时list中，并且需要注意：把nums2中的对应元素删掉。比如nums1 = [1, 2, 2, 1]， nums2 = [2]。如果不删除，则会产生错误。因为nums1与nums2的元素个数要保持一致。

##### 代码

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        for i in nums1:
            if i in nums2:
                nums.append(i)
                nums2.remove(i)
        return nums
```

#### [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

难度简单

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**示例:**

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**说明**:

1. 必须在原数组上操作，不能拷贝额外的数组。
2. 尽量减少操作次数。

##### py

##### 方法1

##### 解题思路

只要当前是0，就移除，同时在末尾在加上一个0。

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
```

##### 方法2

##### 解题思路

双指针滑动，交换非零元素和零元素的位置

循环遍历数组，当遇到非零元素则开始交换慢指针所指的0元素

 i 为慢指针 指向最新一个0元素的位置

```py
def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
```

#### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

难度中等314收藏分享切换为英文关注反馈

判断一个 9x9 的数独是否有效。只需要**根据以下规则**，验证已经填入的数字是否有效即可。

1. 数字 `1-9` 在每一行只能出现一次。
2. 数字 `1-9` 在每一列只能出现一次。
3. 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 `'.'` 表示。

**示例 1:**

```
输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true

```

**示例 2:**

```
输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
```

**说明:**

- 一个有效的数独（部分已被填充）不一定是可解的。
- 只需要根据以上规则，验证已经填入的数字是否有效即可。
- 给定数独序列只包含数字 `1-9` 和字符 `'.'` 。
- 给定数独永远是 `9x9` 形式的。

js

##### 解题思路

哈希判重
行
当前行9个数字不能有重复数字
列
当前列9个数字不能有重复数字
九宫格
当前子数独内没有重复数字
9*9的数独划分为9个小的子数独
boxIndex = Math.floor(row/3) * 3 + Math.floor(columns/3)

##### 代码

```js
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    // 三个方向判重
    let rows = {};
    let columns = {};
    let boxes = {};
    // 遍历数独
    for(let i = 0;i < 9;i++){
        for(let j = 0;j < 9;j++){
            let num = board[i][j];
            if(num != '.'){
                // 子数独序号
                let boxIndex = parseInt((i/3)) * 3 + parseInt(j/3);
                if(rows[i+'-'+num] || columns[j+'-'+num] || boxes[boxIndex+'-'+num]){
                    return false;
                }
                // 以各自方向 + 不能出现重复的数字 组成唯一键值，若出现第二次，即为重复
                rows[i+'-'+num] = true;
                columns[j+'-'+num] = true;
                boxes[boxIndex+'-'+num] = true;
            }
        }
    }
    return true;
};

作者：Alexer-660
链接：https://leetcode-cn.com/problems/valid-sudoku/solution/36-you-xiao-de-shu-du-by-alexer-660/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

py

##### 解题思路

按规则逐条判断，9行+9列+9块

##### 代码

```py
def isValidSudoku(self, board: List[List[str]]) -> bool:
    def isvaild9(lyst):
        nums = list(filter(lambda x:x != '.', lyst))
        return len(set(nums)) == len(nums)
    
    for row in board:#9行
        if not isvaild9(row):
            return False
    
    for column in zip(*board):#9列
        if not isvaild9(column):
            return False
    
    for row in range(3):#9块
        for column in range(3):
            tmp = [board[i][j] for i in range(row*3, row*3+3) for j in range(column*3, column*3+3)]
            if not isvaild9(tmp):
                return False
    return True
    
#https://leetcode-cn.com/problems/valid-sudoku/solution/pythonji-ben-pan-duan-by-luanz/
```

#### [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/)

难度中等

给定一个 *n *× *n* 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

**说明：**

你必须在**原地**旋转图像，这意味着你需要直接修改输入的二维矩阵。**请不要**使用另一个矩阵来旋转图像。

**示例 1:**

```
给定 matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

```

**示例 2:**

```
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

###### js

```js
var rotate = function(matrix) {
  // 时间复杂度O(n^2) 空间复杂度O(1)

  // 做法： 先沿着对角线翻转，然后沿着水平线翻转
  const n = matrix.length;
  function swap(arr, [i, j], [m, n]) {
    const temp = arr[i][j];
    arr[i][j] = arr[m][n];
    arr[m][n] = temp;
  }
  for (let i = 0; i < n - 1; i++) {
    for (let j = 0; j < n - i; j++) {
      swap(matrix, [i, j], [n - j - 1, n - i - 1]);
    }
  }

  for (let i = 0; i < n / 2; i++) {
    for (let j = 0; j < n; j++) {
      swap(matrix, [i, j], [n - i - 1, j]);
    }
  }
};
```

###### py

```python
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    先做矩阵转置（即沿着对角线翻转），然后每个列表翻转；
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for m in range(a):
        matrix[m].reverse()
```

```python
def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    通过内置函数zip，可以简单实现矩阵转置，下面的代码等于先整体翻转，后转置；
    不过这种写法的空间复杂度其实是O(n);
    """
    matrix[:] = map(list, zip(*matrix[::-1]))
#作者：fe-lcifer
#链接：https://leetcode-cn.com/problems/rotate-image/solution/pythonjavascript-liang-ci-fan-zhuan-48-xuan-zhuan-/
```

#### [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

难度中等

请你来实现一个 `atoi` 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

- 如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
- 假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
- 该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

**提示：**

- 本题中的空白字符只包括空格字符 `' '` 。
- 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

###### js

###### 解题思路

parseInt(string, radix)：

string：要被解析的值。如果参数不是一个字符串，则将其转换为字符串。字符串开头的空白符将会被忽略。
radix（可选）：需要转换的进制，介于 2 到 36。
返回值： 如果被解析参数的第一个字符无法被转化成数值类型，则返回NaN。

```js
var myAtoi = function(str) {
    const number = parseInt(str, 10);

    if(isNaN(number)) {
        return 0;
    } else if (number < Math.pow(-2, 31) || number > Math.pow(2, 31) - 1) {
        return number < Math.pow(-2, 31) ? Math.pow(-2, 31) : Math.pow(2, 31) - 1;
    } else {
        return number;
    }
};
```

###### py

###### 解题思路

使用正则表达式：

```。
^：匹配字符串开头
[\+\-]：代表一个+字符或-字符
?：前面一个字符可有可无
\d：一个数字
+：前面一个字符的一个或多个
\D：一个非数字字符
*：前面一个字符的0个或多个
str.lstrip([chars])		chars --指定截取的字符。返回截掉字符串最左边的空格或指定字符后生成的新字符串。
str = "     this is string example....wow!!!     ";
print str.lstrip();			>>>this is string example....wow!!!
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');  	>>>this is string example....wow!!!8888888
max(min(数字, 2**31 - 1), -2**31) 用来防止结果越界
```

```py
class Solution:
    def myAtoi(self, s: str) -> int:
        s=int(*re.findall('^[\+\-]?\d+',str.lstrip()))
        s=min(s,2**31-1)
        s=max(s,-2**31)
        return s
```


### 关于LeetCode的JavaScript以及少部分Python解答

### 目录

[01.两数之和 ](#01.两数之和)

[15.三数之和](#15.三数之和)

[04.寻找两个正序数组的中位数](#04.寻找两个正序数组的中位数)

[06.Z 字形变换](#06.Z 字形变换)

[08.字符串转换整数 (atoi)](#08.字符串转换整数 (atoi))

[09.回文数](#09.回文数)

[13罗马数字转整数](#13罗马数字转整数)

[14.最长公共前缀](#14.最长公共前缀)

[20.有效的括号](#20.有效的括号)

[27.移除元素](#27.移除元素)

[28实现strStr()](#28实现strStr())

[35.搜索插入位置](#35.搜索插入位置)

[38.外观数列](#38.外观数列)

[53.最大子序和](#53.最大子序和)

[58.最后一个单词的长度](#58.最后一个单词的长度)

[67.二进制求和](#67.二进制求和)

[69.x 的平方根](#69.x 的平方根)

##### [动态规划](#动态规划)

[70.爬楼梯](#70.爬楼梯)

[746.使用最小花费爬楼梯](#746.使用最小花费爬楼梯)

[121.买卖股票的最佳时机](#121.买卖股票的最佳时机)

[198.打家劫舍](#198.打家劫舍)

[83.删除排序链表中的重复元素](#83.删除排序链表中的重复元素)

[88.删除排序链表中的重复元素](#88.删除排序链表中的重复元素)

[100.相同的树](#100.相同的树)

[101.对称二叉树](#101.对称二叉树)

[107.二叉树的层次遍历 II](#107.二叉树的层次遍历 II)

[118.杨辉三角](#118.杨辉三角)

[ 237.删除链表中的节点](# 237.删除链表中的节点)

[283. 移动零](#283. 移动零)

[371. 两整数之和](#371. 两整数之和)

##### [双指针](#双指针)

[11. 盛最多水的容器](#11. 盛最多水的容器)

[15. 三数之和](#15. 三数之和)



#### 1. 两数之和

难度简单

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

###### 哈希映射

初始化一个 map = new Map()
从第一个元素开始遍历 nums
获取目标值与 nums[i] 的差值，即 k = target - nums[i] ，判断差值在 map 中是否存在

不存在（ map.has(k) 为 false ） ，则将当前的 nums[i] 加入到 map 中（key为nums[i], value为 i ，方便查找map中是否存在某值，并可以通过 get 方法直接拿到下标）
存在（ map.has(k) ），返回 [map.get(k), i] ，求解结束
遍历结束，则 nums 中没有符合条件的两个数，返回 []
时间复杂度：O(n)

```js
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

###### indexOf()

index：目标值与 nums[i] 的差值在nums中的下标

遍历数组，利用indexOf()查找有没有目标值与 nums[i] 的差值在nums中是否存在；

如果存在，判断index是否大于-1以及index是不是不等于i

```js
var twoSum = function(nums, target) {
    for (var i=0;i<nums.length;i++) {
        var index = nums.indexOf(target-nums[i])
        if(index > -1 && index !== i) {
            return [i, index]
        }
    }
};
```

执行用时 :192 ms, 在所有 JavaScript 提交中击败了19.73%的用户

内存消耗 :32.7 MB, 在所有 JavaScript 提交中击败了100.00%的用户

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

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

可以假设 nums1 和 nums2 不会同时为空。

####15. 三数之和

难度中等

给你一个包含 *n* 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 *a，b，c ，*使得 *a + b + c =* 0 ？请你找出所有满足条件且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

**示例：**

```
给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

数组遍历
首先对数组进行排序，排序后固定一个数 nums[i]，再使用左右指针指向 nums[i]后面的两端，数字分别为 nums[L] 和 nums[R]，计算三个数的和 sum 判断是否满足为 0，满足则添加进结果集
如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
如果 nums[i]== nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
当 sum == 0时，nums[L]== nums[L+1] 则会导致结果重复，应该跳过，L++
当 sum == 0时，nums[R] == nums[R-1]则会导致结果重复，应该跳过，R--
时间复杂度：O(n^2)，n 为数组长度

```js
var threeSum = function(nums) {
    let ans = [];
    const len = nums.length;
    if(nums == null || len < 3) return ans;
    nums.sort((a, b) => a - b); // 排序
    for (let i = 0; i < len ; i++) {
        if(nums[i] > 0) break; // 如果当前数字大于0，则三数之和一定大于0，所以结束循环
        if(i > 0 && nums[i] == nums[i-1]) continue; // 去重
        let L = i+1;
        let R = len-1;
        while(L < R){
            const sum = nums[i] + nums[L] + nums[R];
            if(sum == 0){
                ans.push([nums[i],nums[L],nums[R]]);
                while (L<R && nums[L] == nums[L+1]) L++; // 去重
                while (L<R && nums[R] == nums[R-1]) R--; // 去重
                L++;
                R--;
            }
            else if (sum < 0) L++;
            else if (sum > 0) R--;
        }
    }        
    return ans;
};
```

 4. 寻找两个正序数组的中位数

难度困难

给定两个大小为 m 和 n 的正序（从小到大）数组 `nums1` 和 `nums2`。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 `nums1` 和 `nums2` 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

```js
var findMedianSortedArrays = function (nums1, nums2) {
    let nums = []
    let i =0,j=0;
    let total = nums1.length+nums2.length
    let mid = Math.floor(total/2) + 1
    while(true) {
        if(nums.length === mid) {
            if( total%2 === 1) {
                return nums[mid-1]
            }else{
                return (nums[mid-1]+nums[mid-2])/2
            }
        }
        if(i < nums1.length && j === nums2.length) {
            nums.push(nums1[i])
            i++;
            continue
        }
        if(i === nums1.length && j < nums2.length) {
            nums.push(nums2[j])
            j++;
            continue
        }
        if(nums1[i] < nums2[j]) {
            nums.push(nums1[i])
            i++;
            continue
        }else{
            nums.push(nums2[j])
            j++;
            continue
        }
    }
};
```

当某一个数组为空另一个只有一个元素是为特殊情况，直接领出来返回即可
合并两个数组并排序
如果长度为奇数就直接返回中间的一个元素
如果长度为偶数则是中间两位相加/2

```js
var findMedianSortedArrays = function(nums1, nums2) {
    let result = []
    result = nums1.concat(nums2)
    if(result.length == 1){
        return result[0]
    }
    result.sort((a,b) => a-b)
    if( result.length%2 != 0){
        return result[Math.floor(result.length/2)]
    }
    else{
        return (result[result.length/2]+result[result.length/2-1])/2
    }
}
```

```js
var getKth = function(num1, start1, end1, num2, start2, end2, k) {
  const len1 = end1 - start1 + 1;
  const len2 = end2 - start2 + 1;
  // 保证 len1 比 len2 小。 那么最后如果存在空数组一定是落在 num1 上
  if (len1 > len2) return getKth(num2, start2, end2, num1, start1, end1, k);
  
  if (len1 === 0) return num2[start2 + k - 1];
  
  if (k === 1) return Math.min(num1[start1], num2[start2]);
  
  // 如果 len1 比 k 的一半还小，那么直接取 num1 的最后一个元素进行比较
  const i = start1 + Math.min(len1, Math.floor(k / 2)) - 1;
  // 如果 len2 比 k 的一半还小，那么直接取 num2 的最后一个元素进行比较
  const j = start2 + Math.min(len2, Math.floor(k / 2)) - 1;
  // 如果 num1[i] 小，那么前半部分可以直接丢弃
  if (num1[i] < num2[j]) return getKth(num1, i + 1, end1, num2, start2, end2, k - (i - start1 + 1));
  return getKth(num1, start1, end1, num2, j + 1, end2, k - (j - start2 + 1));
}
var findMedianSortedArrays = function(nums1, nums2) {
  const m = nums1.length;
  const n = nums2.length;
  const left = Math.floor((m + n + 1) / 2);
  // 注意边界，这样可以即处理奇数的情况，又处理偶数的情况
  const right = Math.floor((m + n + 2) / 2);
  // 如果是奇数，那么 left === right, 如果为偶数，那么right = left + 1
  // 奇数的情况，相当于求了两遍的中位数。
  return (getKth(nums1, 0, m - 1, nums2, 0, n - 1, left) + getKth(nums1, 0, m - 1, nums2, 0, n - 1, right)) * 0.5;
};
```

#### 6. Z 字形变换

难度中等686

将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"LEETCODEISHIRING"` 行数为 3 时，排列如下：

```
L   C   I   R
E T O E S I I G
E   D   H   N
```

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如：`"LCIRETOESIIGEDHN"`。

请你实现这个将字符串进行指定行数变换的函数：

```
string convert(string s, int numRows);
```

**示例 1:**

```
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
```

**示例 2:**

```
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
```

###### 按行排序

遍历字符串，遍历过程中将每行都看成新的字符串构成字符串数组，最后再将该数组拼接起来即可

使用 Math.min(s.length, numRows)个列表来表示 Z 字形图案中的非空行

如果 numRows=1 则说明当前字符串即为结果，直接返回
否则整个字符串需要经历，向下向右，向下向右，这样的反复循环过程，设定 goingDown变量表示是否向下，curRow变量表示当前字符串数组的下标

只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。

如果 goingDown为 true，则表示向下 curRow+=1，字符串数组下标向后移动，将当前字符加入当前字符串中
如果 goingDown为 false，则表示向右 curRow-=1 ，字符串数组下标向前移动，将当前字符加入当前字符串中
时间复杂度：O(n)

```js
var convert = function(s, numRows) {
    if(numRows == 1)
        return s;

    const len = Math.min(s.length, numRows);
    const rows = [];
    let goingDown = false;
    for(let i = 0; i< len; i++) rows[i] = "";
    let curRow = 0;

    for(const c of s) {
        rows[curRow] += c;
        //移动到最上面的行或向下移动到最下面的行
        if(curRow == 0 || curRow == numRows - 1)
            //方向发生改变
            goingDown = !goingDown;
        curRow += goingDown ? 1 : -1;
    }

    let ans = "";
    for(const row of rows) {
        ans += row;
    }
    return ans;
};
```



#### 8. 字符串转换整数 (atoi)

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

#### 9. 回文数

难度简单

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true
```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

###### 数学解法

除法和求余获得对应位置的数字

如果是负数则一定不是回文数，直接返回 false

如果是正数，则将其倒序数值计算出来，然后比较和原数值是否相等，如果它们是相同的，那么这个数字就是回文

通过num % 10 获取最后一位数字，再通过num / 10 获取移除最后一位数字的所有数字，再求出上一步结果除以 `10` 的余数得到倒数第二位数字，把最后一位数字乘以 `10`，再加上倒数第二位数字，得到反转后的数字。继续这个过程，将得到更多位数的反转数字。

```js
var isPalindrome = function(x) {
    if(x < 0){
        return false;
    }
    var cur = 0,num = x;
    
    while( num != 0) {
        cur = cur * 10 +Math.floor(num % 10);
        num = Math.floor(num / 10);
    }
    return cur == x;
};
```

执行用时 :216 ms, 在所有 JavaScript 提交中击败了81.31%的用户

内存消耗 :44.5 MB, 在所有 JavaScript 提交中击败了98.00%的用户

#### 11. 盛最多水的容器

难度中等1491

给你 *n* 个非负整数 *a*1，*a*2，...，*a*n，每个数代表坐标中的一个点 (*i*, *ai*) 。在坐标内画 *n* 条垂直线，垂直线 *i* 的两个端点分别为 (*i*, *ai*) 和 (*i*, 0)。找出其中的两条线，使得它们与 *x* 轴共同构成的容器可以容纳最多的水。

**说明：**你不能倾斜容器，且 *n* 的值至少为 2。

 

![img](https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg)

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

**示例：**

```
输入：[1,8,6,2,5,4,8,3,7]
输出：49
```

###### 双指针



```js
var maxArea = function(height) {
    let i = 0, j = height.length-1;
    let square, max = 0;
    while(j-i >= 1){
        if(height[i]>height[j]){
            square = height[j] * (j-i);
            j--;
        }else{
            square = height[i] * (j-i);
            i++;
        }
        max = Math.max(square,max);
    }
    return max;
};
```

###### 双指针 动态划窗

```js
var maxArea = function(height) {
    let left = 0;//左下标
    let right = height.length - 1;//右下标
    let max = 0;//最大装水量
    while(left < right){
        let now = (right - left) * Math.min(height[right], height[left]);
        max = now > max ? now : max;
        if(height[left] > height[right]){
            right--;
        }else{
            left++;
        }
    }
    return max;
};
```

#### 13. 罗马数字转整数

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

#### 14. 最长公共前缀

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



#### 20. 有效的括号

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

#### 21. 合并两个有序链表

难度简单

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

###### Python 

and 和 or 有提前截至运算的功能。

and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果
例子：[] and 7 等于 []
代码流程：（按行数）

判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
对 l1 和 l2 重新赋值，使得 l1 指向比较小的那个节点对象
修改 l1 的 next 属性为递归函数返回值
返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None

```js
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2
```

###### js

当 `l1` 为空或 `l2` 为空时结束

如果 `l1` 的 `val` 值更小，则将 `l1.next` 与排序好的链表头相接，`l2` 同理

```js
var mergeTwoLists = function(l1, l2) {
    if(l1 === null){
        return l2;
    }
    if(l2 === null){
        return l1;
    }
    if(l1.val < l2.val){
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    }else{
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
};

```



#### 26. 删除排序数组中的重复项

难度简单

给定一个排序数组，你需要在** 原地** 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 **原地 修改输入数组 **并在使用 O(1) 额外空间的条件下完成。

用两个指针，指向第一个和第二个元素，如果他们相等，删除第二个元素。指针还指向原来的位置，继续比较。不等的话，两个指针位置都加一。遍历结束即可。

```
def removeDuplicates(self, nums: List[int]) -> int:
    pre,cur=0,1
    while cur<len(nums):       
        if nums[pre]==nums[cur]:
            nums.pop(cur)
        else:
            pre,cur=pre+1,cur+1
    return len(nums)
```

#### 27. 移除元素

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
这五个元素可为任意顺序。
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

#### 28. 实现 strStr()

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

###### js

1、indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。

```js
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};
```

2   slice() 方法可从已有的数组中返回选定的元素。

返回一个新的数组，包含从 start 到 end （不包括该元素）的 arrayObject 中的元素。

```js
var strStr = function(haystack, needle) {
  if (needle === '') return 0
  let i = 0,
    j = 1
  while (i < haystack.length) {
    if (haystack.slice(i, j) === needle) {
      return i
    }
    if (j < haystack.length) {
      j++
    } else {
      i++
      j = i + 1
    }
  }
  return -1
}
```

#### 35. 搜索插入位置

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

#### 38. 外观数列

难度简单458

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

```
1.     1
2.     11
3.     21
4.     1211
5.     111221

```

`1` 被读作  `"one 1"`  (`"一个一"`) , 即 `11`。
`11` 被读作 `"two 1s"` (`"两个一"`）, 即 `21`。
`21` 被读作 `"one 2"`,  "`one 1"` （`"一个二"` ,  `"一个一"`) , 即 `1211`。

给定一个正整数 *n*（1 ≤ *n* ≤ 30），输出外观数列的第 *n* 项。

注意：整数序列中的每一项将表示为一个字符串。

**示例 1:**

```
输入: 1
输出: "1"
解释：这是一个基本样例。
```

###### 通过正则合并相同元素完成累加

```js
var countAndSay = function(n) {
    let prev = '1'
    for(let i = 1; i < n; i++){
        prev = prev.replace(/(\d)\1*/g, item =>`${item.length}${item[0]}`)
    }
    return prev
};
```



#### 53. 最大子序和

难度简单

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例:**

```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

###### js

动态规划

首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果

```js
var maxSubArray = function(nums) {
    let ans = nums[0];
    let sum = 0;
    for(const num of nums) {
        if(sum > 0) {
            sum += num;
        } else {
            sum = num;
        }
        ans = Math.max(ans, sum);
    }
    return ans;
};
```



#### 58. 最后一个单词的长度

难度简单191收藏分享切换为英文关注反馈

给定一个仅包含大小写字母和空格 `' '` 的字符串 `s`，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

**说明：**一个单词是指仅由字母组成、不包含任何空格字符的 **最大子字符串**。

**示例:**

```
输入: "Hello World"
输出: 5
```

###### js

字符串遍历
从字符串末尾开始向前遍历，其中主要有两种情况
第一种情况，以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5
第二种情况，以字符串"Hello World "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5
所以完整过程为先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度

```js
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let end = s.length - 1;
    while(end >= 0 && s[end] == ' ') end--;
    if(end < 0) return 0;
    let start = end;
    while(start >= 0 && s[start] != ' ') start--;
    return end - start;
};
```

2、

```js
var lengthOfLastWord = function(s) {
  s = s.trim()
  let end = s.length - 1
  if (end === 1) {
    return 0
  }
  let start = end
  while (start >= 0 && s.charAt(start) !== ' ') {
    start --
  }
  return end - start
}
```

3、

```js
var lengthOfLastWord = function(s) {
    s = s.trim();
    return s.length-1 -s.lastIndexOf(' '); 
};
```

#### 67. 二进制求和

难度简单

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 **非空 **字符串且只包含数字 `1` 和 `0`。

**示例 1:**

```
输入: a = "11", b = "1"
输出: "100"
```

**示例 2:**

```
输入: a = "1010", b = "1011"
输出: "10101"
```

###### js

**BigInt** 是一种内置对象，它提供了一种方法来表示大于 `253 - 1` 的整数。这原本是 Javascript中可以用 [`Number`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Number) 表示的最大数字。**BigInt** 可以表示任意大的整数。

```js
var addBinary = function (a, b) {
    let numA;
    let numB;
    if (a.length >= 53 || b.length >= 53) {
        numA = BigInt("0b" + a);
        numB = BigInt("0b" + b);
    } else {
        numA = parseInt(a, 2);
        numB = parseInt(b, 2);
    }
    return (numA + numB).toString(2);
};
module.exports = {
    addBinary
}
```

#### 69. x 的平方根

难度简单

实现 `int sqrt(int x)` 函数。

计算并返回 *x* 的平方根，其中 *x *是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

**示例 1:**

```
输入: 4
输出: 2

```

**示例 2:**

```
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
```

###### js

```js
var mySqrt = function(x) {
    return parseInt(Math.sqrt(x));
};
```

牛顿法，迭代公式re_{n+1}=re_{n}-\frac{f(re_n)}{f'(re_n)}re 

```js
var mySqrt = function(x) {
    if (x===0) return 0;
    var re = 1;
    while(!(re * re <= x && (re + 1) * (re + 1) > x)){
        re = parseInt(re - ( re * re - x) / (2 * re));
    }
    return re;
};
```

### 动态规划

#### 32. 最长有效括号

难度困难666收藏分享切换为英文关注反馈

给定一个只包含 `'('` 和 `')'` 的字符串，找出最长的包含有效括号的子串的长度。

**示例 1:**

```
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
```

**示例 2:**

```
输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
```

#### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

难度简单

假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**注意：**给定 *n* 是一个正整数。

**示例 1：**

```
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
```

**示例 2：**

```
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
```

###### js

###### 求第i个斐波那契数

- 3个变量 每次递归更新前两个子问题所需步数
- 可知递推公式  f(n) = f(n-2) + f(n-1),n>=1

```js
var climbStairs = function(n) {
    var f1 = 2;
    var f2 = 3;
    var f3 = 0;
    if(n <= 3){
        return n;
    }
    while(n>3){
        f3 = f2 + f1;
        f1 = f2;
        f2 = f3;
        n--;
    }
    return f2;
};

```

###### 2.动态规划

爬第n阶楼梯的方法数量，等于 2 部分之和

爬上 n-1阶楼梯的方法数量。因为再爬1阶就能到第n阶
爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶

```js
var climbStairs = function(n) {
    // 求第n步 所以索引到n
    var dp = new Array(n+1);
    if(n <= 3){
        return n;
    }
    dp[1] = 1;
    dp[2] = 2;
    for(var i = 3;i<=n;i++){
        dp[i] = dp[i-2] + dp[i-1];
    }
    return dp[n];
};
```

#### [746. 使用最小花费爬楼梯](https://leetcode-cn.com/problems/min-cost-climbing-stairs/)

难度简单

数组的每个索引做为一个阶梯，第 `i`个阶梯对应着一个非负数的体力花费值 `cost[i]`(索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

**示例 1:**

```
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

```

** 示例 2:**

```
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
```

###### 1.动态规划-分解

动态转移方程为

dp[i] = Math.min(dp[i-2] , dp[i-1]) + cost[i]

如果最后一步正好是在最后一个台阶上时，最后一个台阶的花费值不算在内
动态转移方程为
i == n && dp[i] = Math.min(dp[i-2] , dp[i-1])

```js
var minCostClimbingStairs = function(cost) {
    let n = cost.length;
    let dp = new Array(n+1).fill(0);
    dp[0] = cost[0]; 
    dp[1] = cost[1]; 
    for(let i = 2;i <= n;i++){
        if(i == n){
            dp[i] = Math.min(dp[i-2] , dp[i-1]);
        }else{
            dp[i] = Math.min(dp[i-2] , dp[i-1]) + cost[i];
        }
    }
    return dp[n];
};
```

###### 2.动态规划 - 合并

最后一阶台阶不算的情况在内，就直接在最后加一个0(表示包含在这种特殊情况在内，加0就等于花费值为0)
动态转移方程:
dp[i] = Math.min(dp[i-2] , dp[i-1]) + cost[i]

执行用时 :77 ms, 在所有 JavaScript 提交中击败了51.72%的用户

内存消耗 :36 MB, 在所有 JavaScript 提交中击败了100.00%的用户

```js
var minCostClimbingStairs = function(cost) {
    cost.push(0);
    let n = cost.length;
    let dp = [];
    dp[0] = cost[0]; 
    dp[1] = cost[1]; 
    for(let i = 2;i < n;i++){
        dp[i] = Math.min(dp[i-2] , dp[i-1]) + cost[i];
    }
    return dp[n-1];
};
```

###### 3.动态规划 - 比较

最后一阶的台阶的花费值是否被算在内

统一加最后一阶台阶，只在最后取结果的时候

比较判断去掉最后一个台阶的走法情况是否花费更少

执行用时 :68 ms, 在所有 JavaScript 提交中击败了85.25%的用户

内存消耗 :35.5 MB, 在所有 JavaScript 提交中击败了100.00%的用户

```js
var minCostClimbingStairs = function(cost) {
    let n = cost.length;
    let dp = [];
    dp[0] = cost[0]; 
    dp[1] = cost[1]; 
    for(let i = 2;i < n;i++){
        dp[i] = Math.min(dp[i-2] , dp[i-1]) + cost[i];
    }
    return dp[n-1] > dp[n-2] ? dp[n-2] : dp[n-1];
};
```

###### 4.去维 - 变量

时间复杂度最优的解法

执行用时 :64 ms, 在所有 JavaScript 提交中击败了93.94%的用户

内存消耗 :34.7 MB, 在所有 JavaScript 提交中击败了100.00%的用户

```js
var minCostClimbingStairs = function(cost) {
    let n = cost.length;
    let pre = cost[0]; 
    let next = cost[1]; 
    for(let i = 2;i < n;i++){
        let tmp = next;
        next = Math.min(pre,next)+cost[i];
        pre = tmp;
    }
    return Math.min(pre,next);
};
```

#### [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)

难度简单

给定一个数组，它的第 *i* 个元素是一支给定股票第 *i* 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

```

**示例 2:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

###### js

动态规划dp法
dp[i] = max(0, dp[i−1] + diff[i])
max = max(max, dp[i])

```js
var maxProfit = function(prices) {
    let last = 0
    let max = 0
    for (let i = 0; i < prices.length-1; i++) {
        last = Math.max(0, last + prices[i+1]-prices[i])
        max = Math.max(max,last)
    }
    return max
}
```

#### [198. 打家劫舍](https://leetcode-cn.com/problems/house-robber/)

难度简单

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，**如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警**。

给定一个代表每个房屋存放金额的非负整数数组，计算你**在不触动警报装置的情况下，**能够偷窃到的最高金额。

**示例 1:**

```
输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```

**示例 2:**

```
输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
```

###### 动态规划-去维

- dp[n] = dp[n-1] + nums[n]
- 由此可想到斐波那契数列，从而想到动态规划解决

dp[i]的值，只与dp[i-1]和dp[i-2]的值有关，对应不偷当前i个房子和偷当前第i个房子
所以只需要维护两个变量即可
不到更新两个变量的值来保存前n-1个和前n-2个的值即可
到了第n个时，n-1就变为n个的值,n-2就变为n-1个的值，依次递推，最后一个即为所求
在此我们用
preMax：n-2
currMax：n-1
因此当前i：n
并且更新currMax为当前n
preMax更新为上一个currMax
重复即可

```js
var rob = function(nums) {
    var n = nums.length;
    if(n == 0){
        return 0;
    }
    var prevMax = 0;
    var currMax = 0;
    for(var i = 0;i < n;i++){
        var tmp = currMax;
        currMax = Math.max(currMax,prevMax+nums[i]);
        prevMax = tmp;
    }
    return currMax;
};
```

#### [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)

难度简单698收藏分享切换为英文关注反馈

给定一个数组，它的第 *i* 个元素是一支给定股票第 *i* 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

**注意：**你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

**示例 2:**

```
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

**示例 3:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

###### js

```js
var maxProfit = function(prices) {
    var sum = 0;
    for (var i = 1;i <prices.length; i++){
        if (prices[i] - prices[i - 1] > 0) {
            sum += prices[i] - prices[i - 1];
        }
    }
    return sum;
};
```



#### [83. 删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)

难度简单

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

**示例 1:**

```
输入: 1->1->2
输出: 1->2

```

**示例 2:**

```
输入: 1->1->2->3->3
输出: 1->2->3
```

###### js

链表
指定 cur 指针指向头部 head
当 cur 和 cur.next 的存在为循环结束条件，当二者有一个不存在时说明链表没有去重复的必要了
当 cur.val 和 cur.next.val 相等时说明需要去重，则将 cur 的下一个指针指向下一个的下一个，这样就能达到去重复的效果
如果不相等则 cur 移动到下一个位置继续循环

```js
var deleteDuplicates = function(head) {
    var cur = head;
    while(cur && cur.next) {
        if(cur.val == cur.next.val) {
            cur.next = cur.next.next;
        } else {
            cur = cur.next;
        }
    }
    return head;
};
```



#### [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

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

###### py

将两个数组合并之后再排序。

```py
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
           nums1[:] = sorted(nums1[:m] + nums2)
```



#### [100. 相同的树](https://leetcode-cn.com/problems/same-tree/)

难度简单

给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

**示例 1:**

```
输入:       1         1
          / \       / \
         2   3     2   3
        [1,2,3],   [1,2,3]
输出: true
```

**示例 2:**

```
输入:      1          1
          /           \
         2             2
        [1,2],     [1,null,2]
输出: false
```

深度优先遍历

终止条件与返回值：

当两棵树的当前节点都为 null 时返回 true

当其中一个为 null 另一个不为 null 时返回 false

当两个都不为空但是值不相等时，返回 false

执行过程：当满足终止条件时进行返回，不满足时分别判断左子树和右子树是否相同

注意:代码中的短路效应

```js
var isSameTree = function(p, q) {
    if(p == null && q == null) 
        return true;
    if(p == null || q == null) 
        return false;
    if(p.val != q.val) 
        return false;
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};
```

#### [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/)

难度简单

给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 `[1,2,2,3,4,4,3]` 是对称的。

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

但是下面这个 `[1,2,2,null,3,null,3]` 则不是镜像对称的:

```
    1
   / \
  2   2
   \   \
   3    3
```

```js
var isSymmetric = function(root) {
    return root ? checkNode(root.left, root.right) : true;
};

function checkNode(left, right) {
  while (left || right) {
    // 在这里打印日志观察访问顺序和镜像对应位置的值
    // console.log(left && left.val, right && right.val);
    if (!left || !right) return false;
    if (!checkNode(left.right, right.left)) return false;
    if (left.val !== right.val) return false;
    left = left.left;
    right = right.right;
  }
  return true;
```



#### [107. 二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

难度简单231

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7

```

返回其自底向上的层次遍历为：

```
[
  [15,7],
  [9,20],
  [3]
]
```

###### js

DFS

```js
var levelOrderBottom = function(root) {
    if(!root || root.length === 0) {
        return []
    }
    let res = []
    let dfs = (curr,lev)  => {
        if(curr) {
            !res[lev] && (res[lev] = [])
            res[lev].push(curr.val)
            if(curr.left) dfs(curr.left,lev+1)
            if(curr.right) dfs(curr.right,lev+1)
        }
    }
    dfs(root,0)
    return res.reverse()
};
```



#### [110. 平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/)

难度简单

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

> 一个二叉树*每个节点 *的左右两个子树的高度差的绝对值不超过1。

**示例 1:**

给定二叉树 `[3,9,20,null,null,15,7]`

```
    3
   / \
  9  20
    /  \
   15   7
```

返回 `true` 。
**示例 2:**

给定二叉树 `[1,2,2,3,3,null,null,4,4]`

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

```

返回 `false` 。

###### js

从左到右递归树的节点，记录节点的最大深度
在记录节点的同时对该树的节点的左子树与右子树的最大深度做一次对比，如果差值超过1则返回false

递归左右子树

```js
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    // 遍历到底还没有发现高度差超过 1 的左右子树，那么这个子树肯定符合平衡二叉树的规范
    if (!root) {
        return true
    }
    // 判断左右子树的高度差，如果超过 1 那么立即返回 false
    if (Math.abs(getHeight(root.left) - getHeight(root.right)) > 1) {
        return false
    }
    // 分别递归左右子树
    return isBalanced(root.left) && isBalanced(root.right)
    // 获取某个子树的高度
    function getHeight (root) {
        if (!root) {
            return 0
        }
        return Math.max(getHeight(root.left), getHeight(root.right)) + 1
    }
};
```

#### [118. 杨辉三角](https://leetcode-cn.com/problems/pascals-triangle/)

难度简单309

给定一个非负整数 *numRows，*生成杨辉三角的前 *numRows* 行。

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

**示例:**

```
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

判断如果不是该列数组的首位或者最后一位，则值为`a[i-1][j-1] + a[i-1][j]` ，否则值为`1`

```js
var generate = function (numRows) {
    const result = [];
    if (numRows <= 0) {
        return result;
    }
    let i = 0, j = 0;
    for (let i = 0; i < numRows; i ++) {
        const subArr = [];
        for (let j = 0; j <= i; j++) {
            if (j > 0 && j < i) {
                subArr.push(result[i-1][j-1] + result[i-1][j]);
            } else {
                subArr.push(1);
            }
        }
        result.push(subArr);
    }
    return result;
};
```



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

#### [217. 存在重复元素](https://leetcode-cn.com/problems/contains-duplicate/)

难度简单

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 `true` 。如果数组中每个元素都不相同，则返回 `false` 

解法1：集合法
判断原数组和该数组的长度相不相等，一行解决：

```
def containsDuplicate(self, nums: List[int]) -> bool:
    return len((set(nums))) != len(nums)
```

解法2：哈希表

```
def containsDuplicate(self, nums: List[int]) -> bool:
    dic = {}
    for i in nums:
        if dic.get(i):
            return True
        dic[i] = 1
    return False
```

解法3：排序法
排序之后，相等元素必相邻：

```
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            return True
    return False
```

#### 

#### [237. 删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)

难度简单

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/237_example.png)

```
def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next
```

由于只输入了需要删除的节点node，因此无法获取删除节点node的前一个节点pre，从而也就无法将前一个节点pre指向删除节点的下一个节点nex；既然无法通过修改指针完成，那么肯定要修改链表节点的值了。将删除节点node的值和指针都改为下一个节点nex的值和指针即可。

#### 283. 移动零

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

#### 371. 两整数之和

难度简单

**不使用**运算符 `+` 和 `-` ，计算两整数 `a` 、`b` 之和。

**示例 1:**

```
输入: a = 1, b = 2
输出: 3

```

**示例 2:**

```
输入: a = -2, b = 3
输出: 1
```

加法可通过&运算和^运算实现：

两个二进制数相加，^运算的结果不考虑进位时的结果
两个二进制数相加，&运算的结果是对应为是否有进位，如果结果出现1的话，则左移（<<）1位后和^运算的结果继续做加法，直到&运算的结果为0，此时&运算的结果就是两个数的和

```js
const getSum = (a, b) => {
    return add(a, b)
}
const add = (a, b) => {
    return b === 0 ? a : add(a ^ b, (a & b) << 1);
}
```

2

```js
var getSum = function(a, b) {
    let tmp = a ^ b
    let res =(a & b) << 1
    return res + tmp
};
```

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

难度中等

给出两个 **非空** 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 **逆序** 的方式存储的，并且它们的每个节点只能存储 **一位** 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例：**

```
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
```

```js
var addTwoNumbers = function(l1, l2) {
    let node = new ListNode('head');
    let temp = node;//哑结点
    let add = 0;//是否进一
    let sum = 0;//新链表当前未取余的值 = 链表1值 + 链表2值 + add;

    //遍历，直到最长的都为空
    while(l1 || l2){
        sum = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + add;
        temp.next = new ListNode(sum % 10);//取余则为新链表的值
        temp = temp.next;
        add = sum >= 10 ? 1 : 0;
        l1 && (l1 = l1.next);
        l2 && (l2 = l2.next);
    }
    add && (temp.next = new ListNode(add));
    return node.next;
};
```

#### [36. 有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)

难度中等

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
//#作者：fe-lcifer
//#链接：https://leetcode-cn.com/problems/rotate-image/solution/pythonjavascript-liang-ci-fan-zhuan-48-xuan-zhuan-/
```




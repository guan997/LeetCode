# leetcode题解，记录自己的leetcode解题之路

# 目录

[1.两数之和](#1.两数之和)

[4. 寻找两个正序数组的中位数](#4.寻找两个正序数组的中位数)

[6.Z字形变换](#6.Z字形变换)

[7. 整数反转](#7.整数反转)

[08.字符串转换整数(atoi)](#8.字符串转换整数(atoi))

[09.回文数](#9.回文数)

[11.盛最多水的容器](#11.盛最多水的容器)

[13罗马数字转整数](#13.罗马数字转整数)

[14.最长公共前缀](#14.最长公共前缀)

[20.有效的括号](#20.有效的括号)

[链表](#链表)

[21.合并两个有序链表](#21.合并两个有序链表)

[206. 反转链表](#206. 反转链表)

[876. 链表的中间结点](#876. 链表的中间结点)

[19. 删除链表的倒数第N个节点](#19. 删除链表的倒数第N个节点)

[22.括号生成](#22.括号生成)

[26.删除排序数组中的重复项](#26.删除排序数组中的重复项)

[27.移除元素](#27.移除元素)

[28.实现strStr()](#28.实现strStr())

[29. 两数相除](#29. 两数相除)

[35.搜索插入位置](#35.搜索插入位置)

[38.外观数列](#38.外观数列)

[50. Pow(x, n)](#50. Pow(x, n))

[53.最大子序和](#53.最大子序和)

[58.最后一个单词的长度](#58.最后一个单词的长度)

[67.二进制求和](#67.二进制求和)

[69.x的平方根](#69.x的平方根)

[32.最长有效括号](#32.最长有效括号)

[70.爬楼梯](#70.爬楼梯)

[746.使用最小花费爬楼梯](#746.使用最小花费爬楼梯)

[121.买卖股票的最佳时机](#121.买卖股票的最佳时机)

[198.打家劫舍](#198.打家劫舍)

[122.买卖股票的最佳时机II](#122.买卖股票的最佳时机II)

[83.删除排序链表中的重复元素](#83.删除排序链表中的重复元素)

[88.删除排序链表中的重复元素](#88.删除排序链表中的重复元素)

[91. 解码方法](#91. 解码方法)

[树的遍历](#树的遍历)

[94. 二叉树的中序遍历](#94.二叉树的中序遍历)

[145. 二叉树的后序遍历](#145.二叉树的后序遍历)

[100.相同的树](#100.相同的树)

[101.对称二叉树](#101.对称二叉树)

[102. 二叉树的层序遍历](#102.二叉树的层序遍历)

[104. 二叉树的最大深度](#104.二叉树的最大深度)

[107.二叉树的层次遍历II](#107.二叉树的层次遍历II)

[108.将有序数组转换为二叉搜索树](#108.将有序数组转换为二叉搜索树)

[111.二叉树的最小深度](#111.二叉树的最小深度)

[112.路径总和](#112.路径总和)

[114. 二叉树展开为链表](#)

[257. 二叉树的所有路径](#257. 二叉树的所有路径)

[230. 二叉搜索树中第K小的元素](#230. 二叉搜索树中第K小的元素)

[118.杨辉三角](#118.杨辉三角)

[119. 杨辉三角 II](#119. 杨辉三角 II)

[136. 只出现一次的数字](#136. 只出现一次的数字)

[125.验证回文串](#125.验证回文串)

[141.环形链表](#141. 环形链表)

[167.两数之和II-输入有序数组](#167.两数之和II-输入有序数组)

[169. 多数元素](#169.多数元素)

[191. 位1的个数](#191. 位1的个数)

[193. 有效电话号码](#193. 有效电话号码)

[202. 快乐数](#202. 快乐数)

[203. 移除链表元素](#203. 移除链表元素)

[217.存在重复元素](#217.存在重复元素)

[237. 删除链表中的节点](#237. 删除链表中的节点)

[258. 各位相加](#258. 各位相加)

[263. 丑数](#263. 丑数)

[268. 丢失的数字](#268. 丢失的数字)

[283.移动零](#283.移动零)

[343.整数拆分](#343.整数拆分)

[350.两个数组的交集II](#350.两个数组的交集II)

[371.两整数之和](#371.两整数之和)

[387. 字符串中的第一个唯一字符](#387. 字符串中的第一个唯一字符)

[392. 判断子序列](#392. 判断子序列)

[448. 找到所有数组中消失的数字](#448. 找到所有数组中消失的数字)

[456. 132 模式](#456. 132 模式)

[538. 把二叉搜索树转换为累加树](#538. 把二叉搜索树转换为累加树)

[617. 合并二叉树](#617. 合并二叉树)

[657. 机器人能否返回原点](#657. 机器人能否返回原点)

[1185. 一周中的第几天](#1185. 一周中的第几天)

[1431. 拥有最多糖果的孩子](#1431. 拥有最多糖果的孩子)

[1672. 最富有客户的资产总量](#1672. 最富有客户的资产总量)

#### 1.两数之和

难度简单

给定一个整数数组`nums`和一个目标值`target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

###### 哈希映射

- 初始化一个 map = new Map()
- 从第一个元素开始遍历 nums
- 获取目标值与 nums[i] 的差值，即 k = target - nums[i] ，判断差值在 map 中是否存在
- 不存在（ map.has(k) 为 false ） ，则将当前的 nums[i] 加入到 map 中（key为nums[i], value为 i ，方便查找map中是否存在某值，并可以通过 get 方法直接拿到下标）
- 存在（ map.has(k) ），返回 [map.get(k), i] ，求解结束
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

- index：目标值与 nums[i] 的差值在nums中的下标
- 遍历数组，利用indexOf()查找有没有目标值与 nums[i] 的差值在nums中是否存在；
- 如果存在，判断index是否大于-1以及index是不是不等于i

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

###### enumerate() 函数

- enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
- enumerate(sequence, [start=0])
- sequence -- 一个序列、迭代器或其他支持迭代对象。
- start -- 下标起始位置。

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

#### 4.寻找两个正序数组的中位数

难度困难

给定两个大小为 m 和 n 的正序（从小到大）数组 `nums1` 和 `nums2`。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 `nums1` 和 `nums2` 不会同时为空。

**示例 1:**

```
nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
```

**示例 2:**

```
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
```

###### 合并两个数组并排序

- 当某一个数组为空另一个只有一个元素是为特殊情况，直接返回即可
- 合并两个数组并排序
- 如果长度为奇数就直接返回中间的一个元素
- 如果长度为偶数则是中间两位相加/2

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

#### 6.Z字形变换

难度中等

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

- 遍历字符串，遍历过程中将每行都看成新的字符串构成字符串数组，最后再将该数组拼接起来即可
- 使用 Math.min(s.length, numRows)个列表来表示 Z 字形图案中的非空行
- 如果 numRows=1 则说明当前字符串即为结果，直接返回
- 否则整个字符串需要经历，向下向右，向下向右，这样的反复循环过程，设定 goingDown变量表示是否向下，curRow变量表示当前字符串数组的下标
- 只有当我们向上移动到最上面的行或向下移动到最下面的行时，当前方向才会发生改变。
- 如果 goingDown为 true，则表示向下 curRow+=1，字符串数组下标向后移动，将当前字符加入当前字符串中
- 如果 goingDown为 false，则表示向右 curRow-=1 ，字符串数组下标向前移动，将当前字符加入当前字符串中
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

#### 7.整数反转

难度简单

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例 1:**

```
输入: 123
输出: 321
```

 **示例 2:**

```
输入: -123
输出: -321
```

**示例 3:**

```
输入: 120
输出: 21
```

###### 数学解法

- result * 10 + x % 10 取出末位 x % 10（无论正负），拼接到 result 中。
- x / 10 去除末位，| 0 强制转换为32位有符号整数。
- 通过 | 0 取整，无论正负，只移除小数点部分（正数向下取整，负数向上取整）。
- result | 0 超过32位的整数转换结果不等于自身，可用作溢出判断。

```js
var reverse = function(x) {
    let result = 0;
    while(x !== 0) {
        result = result * 10 + x % 10;
        x = (x / 10) | 0;
    }
    return (result | 0) === result ? result : 0;
};
```

###### 转字符串反转处理

- 数字转成字符串
- 去掉符号，按正整数处理，反转字符串
- 判断正负
-  判断是否为32 位的有符号整数

```js

var reverse = function(x) {
    let str = x.toString()
    let l = parseInt(str.split("").reverse().join(""))
    if(str[0] === "-") {
        l = Number("-" + l)
    }
    return (l < Math.pow(-2,31) || l > Math.pow(2,31) - 1) ? 0 :  l
};
```

#### 8.字符串转换整数(atoi)

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

###### 内置函数

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

###### py正则表达式：

```。
^：匹配字符串开头
[\+\-]：代表一个+字符或-字符
?：前面一个字符可有可无
\d：一个数字
+：前面一个字符的一个或多个
\D：一个非数字字符
*：前面一个字符的0个或多个
```

```py
class Solution:
    def myAtoi(self, s: str) -> int:
        s=int(*re.findall('^[\+\-]?\d+',str.lstrip()))
        s=min(s,2**31-1)
        s=max(s,-2**31)
        return s
```

#### 9.回文数

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

- 除法和求余获得对应位置的数字
- 如果是负数则一定不是回文数，直接返回 false
- 如果是正数，则将其倒序数值计算出来，然后比较和原数值是否相等，如果它们是相同的，那么这个数字就是回文
- 通过num % 10 获取最后一位数字，再通过num / 10 获取移除最后一位数字的所有数字，再求出上一步结果除以 `10` 的余数得到倒数第二位数字，把最后一位数字乘以 `10`，再加上倒数第二位数字，得到反转后的数字。继续这个过程，将得到更多位数的反转数字。

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

#### 11.盛最多水的容器

难度中等

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

#### 13.罗马数字转整数

难度简单

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

###### 遍历

- 首先将所有的组合可能性列出并添加到哈希表中
- 然后对字符串进行遍历，由于组合只有两种，一种是 1 个字符，一种是 2 个字符，其中 2 个字符优先于 1 个字符
- 先判断两个字符的组合在哈希表中是否存在，存在则将值取出加到结果 ans 中，并向后移2个字符。不存在则将判断当前 1 个字符是否存在，存在则将值取出加到结果 ans 中，并向后移 1 个字符
- 遍历结束返回结果 ans

```javascript
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

###### pyHashMap映射

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

#### 14.最长公共前缀

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

###### 遍历

- 当字符串数组长度为 0 时公共前缀为空，直接返回
- 初始化，令最长公共前缀 ans 的值为第一个字符串
- 遍历后面的字符串，依次将其与 ans 进行比较，两两找出公共前缀，最终结果即为最长公共前缀
- 如果查找过程中出现了 ans 为空的情况，则公共前缀不存在直接返回

```js
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

###### py遍历

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

#### 20.有效的括号

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

###### py replace()

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

###### 遍历

- 边遍历边匹配。也就是遍历的时候遇到左括号存入数组，下次遇到的第一
- 右括号必须和数组中最后一个元素匹配，否则为无效字符串，匹配完成后从数组中删除此元素。
- 若最终数组为空，表示括号已全部匹配完，字符串有效。

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

### 链表

#### 21.合并两个有序链表

难度简单

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

###### 递归

- 当 l1 为空或 l2 为空时结束
- 如果 l1 的 val 值更小，则将 l1.next 与排序好的链表头相接，l2 同理

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

- 时间复杂度：O(n + m)
- 空间复杂度：O(n + m)

###### 迭代

```js
var mergeTwoLists = function(l1, l2) {
    let res = new ListNode();
    let end = res;
    while (l1 && l2) {
        if (l1.val < l2.val) {
            end.next = l1;
            l1 = l1.next;
        } else {
            end.next = l2;
            l2 = l2.next;
        }
        end = end.next;
    }
    end.next = l1 || l2;
    return res.next;
};
```

- 时间复杂度：O(n + m)
- 空间复杂度：O(1)

py and 和 or

- and 和 or 有提前截至运算的功能。
- and：如果 and 前面的表达式已经为 False，那么 and 之后的表达式将被 跳过，返回左表达式结果
- or：如果 or 前面的表达式已经为 True，那么 or 之后的表达式将被跳过，直接返回左表达式的结果

- 判断 l1 或 l2 中是否有一个节点为空，如果存在，那么我们只需要把不为空的节点接到链表后面即可
- 对 l1 和 l2 重新赋值，使得 l1 指向比较小的那个节点对象
- 修改 l1 的 next 属性为递归函数返回值
- 返回 l1，注意：如果 l1 和 l2 同时为 None，此时递归停止返回 None

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val: l1, l2 = l2, l1
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1 or l2
```

#### 206. 反转链表

难度简单

反转一个单链表。

###### 迭代

- 将单链表中的每个节点的后继指针指向它的前驱节点

```js
var reverseList = function(head) {
    if (!head || !head.next) return head;
    var prev = null,cur = head, temp;
    while(cur){
        temp = cur.next;//修改前先存储 cur 后继节点
        cur.next = prev; // // 反转 cur 的后继指针
        prev = cur; //变更prev、cur
        cur = temp; // cur通过temp指向下一节点
    }
    return prev;//cur会循环直到null
};
```

- 时间复杂度：O(n)

- 空间复杂度：O(1)

###### 递归

-  **不断递归反转当前节点 `head` 的后继节点 `next`**

- **最先调用的函数会在递归过程中最后被执行，而最后调用的会最先执行**
- **最先返回最后两个节点 然后开始反转操作，依次从后面两两节点开始反转**

```js
var reverseList = function(head) {
    // 如果只有一个节点 或者 递归到了尾节点，返回当前节点 
    if(!head || !head.next) return head;
    // 存储当前节点的下一个节点
    let next = head.next;
    let reverseHead = reverseList(next);
    // 断开 head 
    head.next = null;
    // 反转，后一个节点连接当前节点 2.next = 1 1.next = null
    next.next = head;
    return reverseHead;
};
```

- **时间复杂度：O(n)**
- **空间复杂度：O(n)**

#### 876. 链表的中间结点

难度简单

给定一个带有头结点 `head` 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

###### 快慢指针法

- 用两个指针 `slow` 与 `fast` 一起遍历链表。`slow` 一次走一步，`fast` 一次走两步。那么当 `fast` 到达链表的末尾时，`slow` 必然位于中间。

```js
var middleNode = function(head) {
    slow = fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

###### 数组

- 对链表进行遍历，将遍历到的元素依次放入数组 `A` 中。如果遍历到了 `N` 个元素，那么链表以及数组的长度也为 `N`，对应的中间节点即为 `A[N/2]`。

```js
var middleNode = function(head) {
    let A = [head];
    while (A[A.length - 1].next != null)
        A.push(A[A.length - 1].next);
    return A[Math.trunc(A.length / 2)];
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(N)

#### 19. 删除链表的倒数第N个节点

难度中等

给定一个链表，删除链表的倒数第 *n* 个节点，并且返回链表的头结点。

###### 两次遍历算法

- 解题思路：在第一次遍历中，我们找出列表的长度 L。然后设置一个指向哑结点的指针，并移动它遍历列表，直至它到达第 (L - n) 个结点那里。我们把第 (L - n) 个结点的 next 指针重新链接至第 (L - n + 2)个结点

```js
var removeNthFromEnd = function(head, n) {
 let dummy = new ListNode(0);
    dummy.next = head;
    let length = 0;
    let first = head;
    while(first != null){
        length++;
        first = first.next;
    }
    length -= n;
    first = dummy;
    while(length > 0){
        length--;
        first = first.next;
    }
    first.next = first.next.next;
    return dummy.next;
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

###### 双指针，一次遍历算法

- 指针fast 先走n步，然后指针fast和指针slow同步往前继续遍历链表，直至fast的后续结点为空，此时指针slow到达被删除结点的前置结点。

```js
var removeNthFromEnd = function(head, n) {
    let fast = head, slow = head;
    while(--n){
        fast = fast.next;
    }
    if(!fast.next) return head.next;
    fast = fast.next;
    while(fast && fast.next){
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

#### 22.括号生成

难度中等

数字 *n* 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

**示例：**

```
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
```

###### 递归

- 某一次递归终止时需要将当前字符存入数组

- 字符任取一个位置左侧必 左括号>=右括号

- 每次递归除了需要传当前字符还需要传当前字符左右括号数

- 终止条件：如果左右括弧都用完则结束

```js
var generateParenthesis = function (n) {
  let res = [];
  //  cur :当前字符  left：当前字符左括号 right:当前字符右括号
  const help = (cur, left, right) => {
    if (cur.length === 2 * n) {
      res.push(cur);
      return;
    }
      // 如果左括弧未用完则继续增加左括弧
    if (left < n) {
      help(cur + "(", left + 1, right);
    }
      // 如果右括弧少于左括弧则继续增加右括弧
    if (right < left) {
      help(cur + ")", left, right + 1);
    }
  };
  help("", 0, 0);
  return res;
};
```

#### 26.删除排序数组中的重复项

难度简单

给定一个排序数组，你需要在原地*删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 **原地 修改输入数组 **并在使用 O(1) 额外空间的条件下完成。

示例 1:

```
给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
```

示例 2:

```
给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
```

###### 遍历数组

- 确认重复元素个数直接减去中间重复的个数

```js
var removeDuplicates = function(nums) {
    var count = 0;
    var n = nums.length;
    for(let i = 1; i < n; i++) {
        if(nums[i] !=nums[i - 1]) {
            nums[i - count] = nums[i];
        }else{
            count ++;
        }
    }
    return n - count;
};
```

###### 双指针

- 当遇到下一个不相同即不重复的元素时，更新指针位置为下一个元素
- 否则指针位置不动，原数组继续遍历
- 数组遍历完后 返回 r+1 

```js
var removeDuplicates = function(nums) {
    var j = 0;
    var n = nums.length;
    for(let i = 1; i < n; i++) {
        if(nums[i] !=nums[i - 1]) {
            j++;
            nums[j] = nums[i];
        }
    }
    return j+1;
};
```

###### py双指针

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

#### 27.移除元素

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

###### 拷贝覆盖

- 遍历数组nums，每次取出的数字变量为num，同时设置一个下标ans
- 在遍历过程中如果出现数字与需要移除的值不相同时，则进行拷贝覆盖nums[ans] = num，ans自增1
- 如果相同的时候，则跳过该数字不进行拷贝覆盖，最后ans即为新的数组长度
- 在移除元素较多时更适合使用，最极端的情况是全部元素都需要移除，遍历一遍结束即

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

###### 交换移除

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

#### 28.实现strStr()

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

###### indexOf()

1、indexOf() 方法可返回某个指定的字符串值在字符串中首次出现的位置。

```js
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};
```

###### slice()

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

#### 35.搜索插入位置

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

###### indexOf()

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

#### 29. 两数相除

难度中等

给定两个整数，被除数 `dividend` 和除数 `divisor`。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 `dividend` 除以除数 `divisor` 得到的商。

整数除法的结果应当截去（`truncate`）其小数部分，例如：`truncate(8.345) = 8` 以及 `truncate(-2.7335) = -2`

**示例 1:**

```
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
```

**示例 2:**

```
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
```

**提示：**

- 被除数和除数均为 32 位有符号整数。
- 除数不为 0。
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

###### 减法

```js
var divide = function(dividend, divisor) {
    var INT_MAX = 0x7FFFFFFF;
    var INT_MIN = 1 << 31;
    if(dividend == 0) return 0;
    if(divisor == 1) return dividend;
    if(divisor == -1){
        if(dividend > INT_MIN) return -dividend;// 只要不是最小的那个整数，都是直接返回相反数
        return INT_MAX;// 是最小的那个，那就返回最大的整数
    }
    let a = dividend;
    let b = divisor;
    let sign = 1;
    if((a > 0 && b < 0) || (a < 0 && b > 0)){
        sign = -1;
    }
    a = a > 0 ? a : -a;
    b = b > 0 ? b : -b;
    let res = div(a, b);
    if(sign > 0) return res > INT_MAX ? INT_MAX :res;
    return -res;
};
function div(a, b){
    if(a<b) return 0;
        let count = 1;
        let tb = b; 
        while((tb+tb)<=a){
            count = count + count; // 最小解翻倍
            tb = tb+tb; // 当前测试的值也翻倍
        }
        return count + div(a-tb,b);
}
```

#### 38.外观数列

难度简单

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

#### 50. Pow(x, n)

###### 难度中等

实现 [pow(*x*, *n*)](https://www.cplusplus.com/reference/valarray/pow/) ，即计算 x 的 n 次幂函数。

**示例 1:**

```
输入: 2.00000, 10
输出: 1024.00000
```

**示例 2:**

```
输入: 2.10000, 3
输出: 9.26100
```

**示例 3:**

```
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
```

**说明:**

- -100.0 < *x* < 100.0
- *n* 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

```js
var myPow = function(x, n, sum = 1, m = 0) {
    n < 0 && (n = -n, m = 1)
    while (n) n & 1 && (sum *= x), x *= x, n >>>= 1
    return m ? 1 / sum : sum
}
```

#### 53.最大子序和

难度简单

给定一个整数数组 `nums` ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

**示例:**

```
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```

###### 动态规划

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



#### 58.最后一个单词的长度

难度简单191收藏分享切换为英文关注反馈

给定一个仅包含大小写字母和空格 `' '` 的字符串 `s`，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

**说明：**一个单词是指仅由字母组成、不包含任何空格字符的 **最大子字符串**。

**示例:**

```
输入: "Hello World"
输出: 5
```

###### 字符串遍历

从字符串末尾开始向前遍历，其中主要有两种情况
第一种情况，以字符串"Hello World"为例，从后向前遍历直到遍历到头或者遇到空格为止，即为最后一个单词"World"的长度5
第二种情况，以字符串"Hello World "为例，需要先将末尾的空格过滤掉，再进行第一种情况的操作，即认为最后一个单词为"World"，长度为5
所以完整过程为先从后过滤掉空格找到单词尾部，再从尾部向前遍历，找到单词头部，最后两者相减，即为单词的长度

```js
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

###### 内置函数

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

###### 字符串

将两个字符串较短的用 00 补齐，使得两个字符串长度一致，然后从末尾进行遍历计算，得到最终结果。

本题解中大致思路与上述一致，但由于字符串操作原因，不确定最后的结果是否会多出一位进位，所以会有 2 种处理方式：

第一种，在进行计算时直接拼接字符串，会得到一个反向字符，需要最后再进行翻转
第二种，按照位置给结果字符赋值，最后如果有进位，则在前方进行字符串拼接添加进位

```js
var addBinary = function(a, b) {
    let ans = "";
    let ca = 0;
    for(let i = a.length - 1, j = b.length - 1;i >= 0 || j >= 0; i--, j--) {
        let sum = ca;
        sum += i >= 0 ? parseInt(a[i]) : 0;
        sum += j >= 0 ? parseInt(b[j]) : 0;
        ans += sum % 2;
        ca = Math.floor(sum / 2);
    }
    ans += ca == 1 ? ca : "";
    return ans.split('').reverse().join('');
};
```

#### 69.x的平方根

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

###### 内置函数

```js
var mySqrt = function(x) {
    return parseInt(Math.sqrt(x));
};
```

###### 牛顿法，迭代公式re_{n+1}=re_{n}-\frac{f(re_n)}{f'(re_n)}re 

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

难度困难

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

#### 70.爬楼梯

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

#### 746.使用最小花费爬楼梯

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

#### 121. 买卖股票的最佳时机

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

###### 动态规划dp法

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

#### 198. 打家劫舍

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

#### 122.买卖股票的最佳时机II

难度简单

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

###### 动态规划

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



#### 83. 删除排序链表中的重复元素

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

###### 链表

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

#### 88. 合并两个有序数组

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

#### 91. 解码方法

难度中等

一条包含字母 `A-Z` 的消息通过以下映射进行了 **编码** ：

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```

要 **解码** 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，`"111"` 可以将 `"1"` 中的每个 `"1"` 映射为 `"A"` ，从而得到 `"AAA"` ，或者可以将 `"11"` 和 `"1"`（分别为 `"K"` 和 `"A"` ）映射为 `"KA"` 。注意，`"06"` 不能映射为 `"F"` ，因为 `"6"` 和 `"06"` 不同。

给你一个只含数字的 **非空** 字符串 `num` ，请计算并返回 **解码** 方法的 **总数** 。

题目数据保证答案肯定是一个 **32 位** 的整数。

**示例 1：**

```
输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
```

**示例 2：**

```
输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
```

**示例 3：**

```
输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
```

**示例 4：**

```
输入：s = "06"
输出：0
解释："06" 不能映射到 "F" ，因为字符串开头的 0 无法指向一个有效的字符。 
```

**提示：**

- `1 <= s.length <= 100`
- `s` 只包含数字，并且可能包含前导零

###### 动态规划

```js
/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
    /**
     * CC : Core Code
     * cur += valid lastOne (0 ~ 10) + valid lastTwo (10 ~ 26)
     */

    // 异常处理
    if(s[0] === '0') return 0

    // 边界处理：多填充一位辅助位（前两位为1）因为后续需要用到
    const len = s.length, dp = [1, 1, ...new Array(len - 1).fill(0)]

    // DP 方程 CC的具体实现
    for (let i = 2; i <= len; i++) {
        let lastOne = s.slice(i - 1, i), lastTwo = s.slice(i - 2, i)

        if(lastOne > 0 && lastOne < 10) dp[i] += dp[i - 1]

        if(lastTwo >= 10 && lastTwo <= 26) dp[i] += dp[i - 2]
    }

    return dp[len]
};
```

### 树的遍历

#### 94.二叉树的中序遍历

难度中等

给定一个二叉树，返回它的*中序* 遍历。

**示例:**

```
输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
```

###### 递归

```js
var inorderTraversal = function(root) {
  const res = []
  function traversal (root) {
    if (root !== null) {
      traversal(root.left)
      res.push(root.val)
      traversal(root.right)
    }
  }
  traversal(root)
  return res
}
```

#### 145.二叉树的后序遍历

难度困难

给定一个二叉树，返回它的 *后序* 遍历。

**示例:**

```
输入: [1,null,2,3]  
   1
    \
     2
    /
   3 

输出: [3,2,1]
```

###### 递归

```js
var postorderTraversal = function(root) {
  const res = []
  function traversal (root) {
    if (root !== null) {
      traversal(root.left)
      traversal(root.right)
      res.push(root.val)
    }
  }
  traversal(root)
  return res
}
```

#### 100. 相同的树

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

###### 深度优先遍历

终止条件与返回值：

- 当两棵树的当前节点都为 null 时返回 true
- 当其中一个为 null 另一个不为 null 时返回 false
- 当两个都不为空但是值不相等时，返回 false

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

#### 101. 对称二叉树

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

#### 102.二叉树的层序遍历

难度中等

给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

###### 递归

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  const res = []
  function traversal (root, depth) {
    if (root !== null) {
      if (!res[depth]) {
        res[depth] = []
      }
      traversal(root.left, depth + 1)
      res[depth].push(root.val)
      traversal(root.right, depth + 1)
    }
  }
  traversal(root, 0)
  return res
}
```

#### 104.二叉树的最大深度

难度简单

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

**说明:** 叶子节点是指没有子节点的节点。

**示例：**
给定二叉树 `[3,9,20,null,null,15,7]`，

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。

###### DFS

```js
var maxDepth = function(root) {
    if(!root){
        return 0;
    }else {
        const left = maxDepth(root.left);
        const right = maxDepth(root.right);
        return Math.max(left, right) + 1;
    }
};
```

###### 递归

```js
var maxDepth = function (root) {
  let res = 0
  function traversal (root, depth) {
    if (root !== null) {
      if (depth > res) {
        res = depth
      }
      if (root.left) {
        traversal(root.left, depth + 1)
      }
      if (root.right) {
        traversal(root.right, depth + 1)
      }
    }
  }
  traversal(root, 1)
  return res
}。
```

#### 107.二叉树的层次遍历II

难度简单

给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

###### BFS

```JS
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
    if(!root) return []
    let q = [root], res = []
    while(q.length){
        let size = q.length, tmp = []
        for(let i = 0; i < size; i++){
            let node = q.shift()
            tmp.push(node.val)

            if(node.left) q.push(node.left)
            if(node.right) q.push(node.right)
        }
        res.unshift(tmp)
    }
    return res
};
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)

###### DFS

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

#### 108. 将有序数组转换为二叉搜索树

难度简单

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过 1。

**示例:**

```
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```

###### 递归 分治

构建 root、构建 root.left 和 root.right
构建 root 时，选数组的中点即可保证平衡
递归函数的传参可以是数组，也可以是指针，因为传参数组所以每次都要切割数组

```js
 var sortedArrayToBST = function(nums) {
    // 将数组分成两半，一半是左子树，另一半是右子树
    if(nums.length === 0) return null;
    const mid = nums.length >> 1;
    const root = new  TreeNode(nums[mid]);

    root.left = sortedArrayToBST(nums.slice(0, mid));
    root.right = sortedArrayToBST(nums.slice(mid + 1))
    return root;
};
```

执行用时：76 ms, 在所有 JavaScript 提交中击败了93.39%的用户

内存消耗：38.7 MB, 在所有 JavaScript 提交中击败了100.00%的用户

#### 110. 平衡二叉树

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

###### 递归

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

#### 111.二叉树的最小深度

难度简单

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

**说明:** 叶子节点是指没有子节点的节点。

**示例:**

给定二叉树 `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最小深度  2.

###### 递归

```js
var minDepth = function(root) {
    if(root === null) return 0;
    const left = minDepth(root.left);
    const right = minDepth(root.right);
    return (left == 0 || right == 0) ? left + right + 1: Math.min(left,right) + 1;
};
```

执行用时：80 ms, 在所有 JavaScript 提交中击败了58.38%的用户

内存消耗：39.6 MB, 在所有 JavaScript 提交中击败了50.00%的用户

###### 递归DFS

当前节点root为空时，最小深度为0
当前节点root的左子树和右子树都为空时，说明此处树的最小深度为1
如果为其他情况，则说明当前节点有值，且需要分别计算其左右子树的最小深度，返回最小深度+1，+1表示当前节点存在有1个深度

```js
var minDepth = function(root) {
    if(root == null) {
        return 0;
    }
    if(root.left == null && root.right == null) {
        return 1;
    }
    let ans = Number.MAX_SAFE_INTEGER;//最大的安全整数
    if(root.left != null) {
        ans = Math.min(minDepth(root.left), ans);
    }
    if(root.right != null) {
        ans = Math.min(minDepth(root.right), ans);
    }
    return ans + 1;
};
```

执行用时：88 ms, 在所有 JavaScript 提交中击败了26.43%的用户

内存消耗：39.9 MB, 在所有 JavaScript 提交中击败了50.00%的用户

#### 112. 路径总和

难度简单

给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

**说明:** 叶子节点是指没有子节点的节点。

**示例:** 
给定如下二叉树，以及目标和 `sum = 22`，

```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
```

返回 `true`, 因为存在目标和为 22 的根节点到叶子节点的路径 `5->4->11->2`。

###### 递归

如果当前节点不是叶子节点，递归它的所有子节点，传递的参数就是 sum 减去当前的节点值；
如果当前节点是叶子节点，判断参数 sum 是否等于当前节点值，如果相等就返回 true，否则返回 false。

```js
var hasPathSum = function(root, sum) {
  // 根节点为空
  if (root === null) return false;
  
  // 叶节点 同时 sum 参数等于叶节点值
  if (root.left === null && root.right === null) return root.val === sum;

  // 总和减去当前值，并递归
  sum = sum - root.val
  return hasPathSum(root.left, sum) || hasPathSum(root.right, sum);
};
```

#### 114. 二叉树展开为链表

难度中等

给定一个二叉树，[原地](https://baike.baidu.com/item/原地算法/8010757)将它展开为一个单链表。

例如，给定二叉树

```
    1
   / \
  2   5
 / \   \
3   4   6
```

将其展开为：

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

###### 遍历

如果按先遍历 right 再遍历 left 生成的「后序遍历」，我们会发现这和 前序遍历 的结果刚好相反。利用这个特点，我们可以在 O(1)O(1) 的空间复杂度内解决这道题。

```js
var flatten = function(root) {
    const helper = (root) => {
        if (!root) {
            return
        }
        helper(root.right)
        helper(root.left)
        root.right = prev
        root.left = null
        prev = root
    }
    let prev = null
    helper(root)
};
```

#### 257. 二叉树的所有路径

难度简单

给定一个二叉树，返回所有从根节点到叶子节点的路径。

**说明:** 叶子节点是指没有子节点的节点。

###### 深度优先搜索

```js
var binaryTreePaths = function(root) {
    const paths = [];
    const construct_paths = (root, path) => {
        if (root) {
            path += root.val.toString();
            if (root.left === null && root.right === null) { // 当前节点是叶子节点
                paths.push(path); // 把路径加入到答案中
            } else {
                path += "->"; // 当前节点不是叶子节点，继续递归遍历
                construct_paths(root.left, path);
                construct_paths(root.right, path);
            }
        }
    }
    construct_paths(root, "");
    return paths;
};
```

时间复杂度：O(N^2)

空间复杂度：O(N^2)

#### 230. 二叉搜索树中第K小的元素

难度中等

给定一个二叉搜索树，编写一个函数 `kthSmallest` 来查找其中第 **k** 个最小的元素。

**说明：**
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

**示例 1:**

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
```

**示例 2:**

```
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
```

###### 递归

```js
var kthSmallest = function (root, k) {
  let arr = []
  function traversal(node) {
    if (node !== null && arr.length < k) {
      traversal(node.left)
      arr.push(node.val)
      traversal(node.right)
    }
  }
  traversal(root)
  return arr[k - 1]
}
```

###### 进一步优化, 使用O(1)的额外空间

```js
var kthSmallest = function (root, k) {
  let res
  let count = 0
  function traversal(node) {
    if (node !== null) {
      if (count < k) {
        traversal(node.left)
      }
      if (++count === k) {
        res = node.val
      }
      if (count < k) {
        traversal(node.right)
      }
    }
  }
  traversal(root)
  return res
}
```

#### 118. 杨辉三角

难度简单

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

#### 119. 杨辉三角 II

难度简单

给定一个非负索引 *k*，其中 *k* ≤ 33，返回杨辉三角的第 *k* 行。

![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

在杨辉三角中，每个数是它左上方和右上方的数的和。

###### 数组

```js
var getRow = function(rowIndex) {
    let res = [], last = [];
    for(let i = 0; i < rowIndex + 1; i++){
        last = res;
        res = [];
        res[0] = 1;
        res[i] = 1;
        if(i > 1){
            for(let j = 1; j < i; j++){
                res[j] = last[j - 1] + last[j];
            }
        }
    }
    return res;
};
```

#### 136. 只出现一次的数字

难度简单

给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

**说明：**

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

###### 异或运算 ⊕

- 异或运算有以下三个性质。

  1.任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
  2.任何数和其自身做异或运算，结果是 0，即a⊕a=0。
  3.异或运算满足交换律和结合,即a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

  ```js
  /**
   * @param {number[]} nums
   * @return {number}
   */
  var singleNumber = function(nums) {
      let single = 0;
      for(let num of nums){
          single ^= num
      }
      return single
  };
  ```

- 时间复杂度：O(n)，其中 n*是数组长度。只需要对数组遍历一次。
- 空间复杂度：O(1)。

    def singleNumber(self, nums: List[int]) -> int:
        a=0
        for i in nums:
            a=a^i
        return a
#### 141. 环形链表

难度简单

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。

**示例 1：**

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

**示例 2：**

```
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

###### 哈希表

- 哈希表存储曾经遍历过的节点
- 遍历每一个节点，都查看哈希表是否存在当前节点，如果存在，则说明链表有环
- 如果不存在，则存入哈希表，并继续遍历下一节点

```js
var hasCycle = (head) => {
  let map = new Map()
  while (head) {
    if (map.has(head)) return true
    map.set(head, true)
    head = head.next
  }
  return false
}
```

###### 快慢指针

- 从同一个起点出发，一个跑得快，一个跑得慢，在某一时刻，速度快的必定会追上速度慢的

```js
var hasCycle = function(head) {
  let fast = head,slow = head
  while (fast) { // 快指针没有指向null
    if (fast.next == null) return false // 下一个为null了，没有环
    slow = slow.next // 快的前面都有节点，慢的前面当然有
    fast = fast.next.next // 推进2个节点
    if (slow === fast) return true // 快慢指针相遇，有环
  }
  return false // fast为null始终不相遇
};
```



#### 167.两数之和II-输入有序数组

难度简单

给定一个已按照***升序排列\*** 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2*。*

**说明:**

- 返回的下标值（index1 和 index2）不是从零开始的。
- 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

**示例:**

```
输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
```

###### 双指针

```js
var twoSum = function (numbers, target) {
  	let left = 0,
    right = numbers.length - 1
  	while (left < right) {
    	// 当两个指针对应的元素和等于 target直接返回
    	if (numbers[left] + numbers[right] === target) {
     		 return [left + 1, right + 1]
   		 } else if (numbers[left] + numbers[right] > target) {
     		 // 当和大于target，则右侧减小(较大的值减小)
      		right--
   		 } else {
     		 // 当和小于target，则左侧增大(较小的值增大)
     		 left++
    	 }
   }
}
```

#### 169.多数元素

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

#### 151. 翻转字符串里的单词

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

#### 125. 验证回文串

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

###### 正则加双指针

正则处理字符串去掉不是字母和数字的

双指针首尾字符对比

```js
var isPalindrome = function(s) {
    let str = s.replace(/\W|_/g, '').toLowerCase()
    let left = 0
    let right = str.length - 1
    while(left < right){
      if(str[left] !== str[right]) return false
      left++
      right--
    }
    return true
  };
```

执行用时：72 ms, 在所有 JavaScript 提交中击败了97.91%的用户

内存消耗：37.9 MB, 在所有 JavaScript 提交中击败了38.46%的用户

Python

str.isalnum()方法检测字符串是否由字母和数字组成。
如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

str.lower()方法转换字符串中所有大写字符为小写。
返回将字符串中所有大写字符转换为小写后生成的字符串。

    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]
#### 66. 加一

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
#### 387. 字符串中的第一个唯一字符

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

###### 遍历

indexof===lastIndexOf则代表只出现一次

```js
var firstUniqChar = function(s) {
    for(let i=0;i<s.length;i++){
        if(s.indexOf(s[i])==s.lastIndexOf(s[i])){
           return i
           }
    }
    return -1
};
```

###### 使用哈希表存储频数

我们可以对字符串进行两次遍历。

在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回它的索引，否则在遍历结束后返回 -1−1。

```js
var firstUniqChar = function(s) {
    const frequency = _.countBy(s);
    for (const [i, ch] of Array.from(s).entries()) {
        if (frequency[ch] === 1) {
            return i;
        }
    }
    return -1;
};
```

- 时间复杂度：O(n)，其中 n 是字符串 s 的长度。我们需要进行两次遍历。
- 空间复杂度：O(∣Σ∣)，其中 Σ 是字符集，在本题中 s 只包含小写字母，因此 ∣Σ∣≤26。我们需要 O(∣Σ∣) 的空间存储哈希映射。

###### 使用哈希表存储索引

我们可以对方法一进行修改，使得第二次遍历的对象从字符串变为哈希映射。

具体地，对于哈希映射中的每一个键值对，键表示一个字符，值表示它的首次出现的索引（如果该字符只出现一次）或者 −1（如果该字符出现多次）。当我们第一次遍历字符串时，设当前遍历到的字符为 c，如果 c 不在哈希映射中，我们就将 c 与它的索引作为一个键值对加入哈希映射中，否则我们将 c 在哈希映射中对应的值修改为 -1。

在第一次遍历结束后，我们只需要再遍历一次哈希映射中的所有值，找出其中不为 −1 的最小值，即为第一个不重复字符的索引。如果哈希映射中的所有值均为 −1，我们就返回 −1。

```js
var firstUniqChar = function(s) {
    const position = new Map();
    const n = s.length;
    for (let [i, ch] of Array.from(s).entries()) {
        if (position.has(ch)) {
            position.set(ch, -1);
        } else {
            position.set(ch, i);
        }
    }
    let first = n;
    for (let pos of position.values()) {
        if (pos !== -1 && pos < first) {
            first = pos;
        }
    }
    if (first === n) {
        first = -1;
    }
    return first;
};
```

- 时间复杂度：O(n)，其中 nn 是字符串 s 的长度。第一次遍历字符串的时间复杂度为 O(n)，第二次遍历哈希映射的时间复杂度为 O(∣Σ∣)，由于 ss 包含的字符种类数一定小于 ss 的长度，因此 O(∣Σ∣) 在渐进意义下小于 O(n)，可以忽略。
- 空间复杂度：O(∣Σ∣)，其中 Σ 是字符集，在本题中 s 只包含小写字母，因此 ∣Σ∣≤26。我们需要 O(∣Σ∣) 的空间存储哈希映射。

###### 第一种

Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）

c = Counter("abcdefgab")		>>>		 c["a"]2

```python
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

```python
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

#### 189. 旋转数组

难度简单

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

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

###### 遍历

1.使用while循环遍历，一次递减
2.将最后一个弹出，同时插入到第一个的位置
3.返回数组

- unshift() 方法可向数组的开头添加一个或更多元素，并返回新的长度。

- pop() 方法将删除 arrayObject 的最后一个元素，把数组长度减 1，并且返回它删除的元素的值。如果数组已经为空，则 pop() 不改变数组，并返回 undefined 值。


```js
 var rotate = function(nums, k) {
      while (k>0) {
          nums.unshift(nums.pop())
          k = k-1
      }
      return nums
 };
```

###### 切片

1、将-k个元素添加到nums的开始，
2、注意，为什么是nums[lenth-k:]而不是nums[-k:]，因为是为了避免k=0的情况

```py
def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ##用切片的方法：k就是将nums的最后k个数放在nums的开始位置即可
    lenth = len(nums)
    nums[:] = nums[lenth-k:]+nums[:lenth-k]
```

#### 191. 位1的个数

难度简单

编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为[汉明重量](https://baike.baidu.com/item/汉明重量)）。

**提示：**

- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
- 在 Java 中，编译器使用[二进制补码](https://baike.baidu.com/item/二进制补码/5295284)记法来表示有符号整数。因此，在上面的 **示例 3** 中，输入表示有符号整数 `-3`。

**进阶**：

- 如果多次调用这个函数，你将如何优化你的算法？

**示例 1：**

```
输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
```

**示例 2：**

```
输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
```

**示例 3：**

```
输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```

**提示：**

- 输入必须是长度为 `32` 的 **二进制串** 。

###### 除k取余法 

执行结果：

超出时间限制

```js
var hammingWeight = function(n) {
    let ans = 0;
    while (n) {
        ans += n % 2;
        n >>= 1;
    }
    return ans;
};
```

###### 循环和位移动

遍历数字的 32 位。如果某一位是 1 ，将计数器加一。

我们使用 位掩码 来检查数字的第 i 位。一开始，掩码 m=1 因为 1 的二进制表示
0000 0000 0000 0000 0000 0000 0000 0001

显然，任何数字跟掩码 1 进行逻辑与运算，都可以让我们获得这个数字的最低位。检查下一位时，我们将掩码左移一位。
0000 0000 0000 0000 0000 0000 0000 0010

并重复此过程。

```js
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let bits = 0;
    let mask = 1;
    for (let i = 0; i < 32; i++) {
        if ((n & mask) != 0) {// 如果第i位和mask都为1，bits++
            bits++;
        }// mask左移一位
        mask <<= 1;
    }
    return bits;
};
```

时间复杂度：O(1) 。运行时间依赖于数字 n 的位数。由于这题中 n 是一个 32 位数，所以运行时间是 O(1) 的。

空间复杂度：O(1)。没有使用额外空间。

###### 位操作的小技巧

把前面的算法进行优化。不再检查数字的每一个位，而是不断把数字最后一个 1 反转，并把答案加一。当数字变成 0 的时候偶，我们就知道它没有 1 的位了，此时返回答案。

这里关键的想法是对于任意数字 n ，将 n 和 n - 1 做与运算，会把最后一个 1 的位变成 0 。为什么？考虑 n 和 n−1 的二进制表示。

```js
/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let sum = 0;
    while (n != 0) {
        sum++;
        n &= (n - 1);
    }
    return sum;
};
```

时间复杂度：O(1) 。运行时间依赖于数字 n 的位数。由于这题中 n 是一个 32 位数，所以运行时间是 O(1) 的。

空间复杂度：O(1)。没有使用额外空间。

#### 位运算的由来

在计算机里面，任何数据最终都是用数字来表示的（不管是我们平时用的软件，看的图片，视频，还是文字）。
并且计算机运算单元只认识高低电位，转化成我们认识的逻辑，也就是 0 1 。

这就是导致计算机里面任何数据最终都是用二进制（0 1）来保存的数字。只是我们平时看到的图片、文字、软件都只从二进行数字转化而来的。

##### 位运算符

![image.png](https://pic.leetcode-cn.com/1615691379-TPWDJp-image.png)

##### 常用位操作

判断奇偶
(x & 1) == 1 ---等价---> (x % 2 == 1)
(x & 1) == 0 ---等价---> (x % 2 == 0)
x / 2 ---等价---> x >> 1
x &= (x - 1) ------> 把x最低位的二进制1给去掉
x & -x -----> 得到最低位的1
x & ~x -----> 0
指定位置的位运算
将X最右边的n位清零：x & (~0 << n)
获取x的第n位值：(x >> n) & 1
获取x的第n位的幂值：x & (1 << n)
仅将第n位置为1：x | (1 << n)
仅将第n位置为0：x & (~(1 << n))
将x最高位至第n位（含）清零：x & ((1 << n) - 1)
将第n位至第0位（含）清零：x & (~((1 << (n + 1)) - 1))

##### 异或结合律

```js
x ^ 0 = x, x ^ x = 0
x ^ (~0) = ~x, x ^ x = ~0
a ^ b = c, a ^ c = b, b ^ c = a

(有没有点乘法结合律的意思)
字母表示：(a ^ b) ^ c = a ^ (b ^ c)
图形表示：(☆ ^ ◇) ^ △ = ☆ ^ (◇ ^ △)
```

解题
利用上面提到的常用位操作：
x &= (x - 1)
从右往左，每次把最低位的 1 给打掉，并累加被打掉1的次数

如：

```js
n     :   0B101011
n - 1 :   0B101010
------------------
&     :   0B101010
n     :   0B101000
n - 1 :   0B100111
------------------
&     :   0B100000
```

#### 193. 有效电话号码

难度简单

给定一个包含电话号码列表（一行一个电话号码）的文本文件 `file.txt`，写一个单行 bash 脚本输出所有有效的电话号码。

你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

你也可以假设每行前后没有多余的空格字符。

**示例：**

假设 `file.txt` 内容如下：

```
987-123-4567
123 456 7890
(123) 456-7890
```

你的脚本应当输出下列有效的电话号码：

```
987-123-4567
(123) 456-7890
```

Bash 是Linux系统自带的脚本语言。 

#### 正则表达式

```Bash 
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
sed -n -r '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$/p' file.txt
awk '/^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-([0-9]{4})$/' file.txt
```

```
注意""不要丢了，其中的空格，()是普通字符，" "不要丢了
^：表示行首，以...开始，这里表示以(xxx) 或者xxx-开始，注意空格
()：选择操作符，要么是([0-9]\{3\}) ，要么是[0-9]\{3\}-
|：或者连接操作符，表示或者
[]：单字符占位，[0-9]表示一位数字
{n}：匹配n位，[0-9]\{3\}匹配三位连续数字
$：表示行尾，结束
```

| 特殊字符 表达                                                |
| ------------------------------------------------------------ |
| 特殊字符	转义表达	特殊含义                             |
| ()	\(\)	标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用 |
| $	\$	匹配输入字符串的结尾位置                          |
| *	\*	匹配前面的子表达式零次或多次                      |
| +	\+	匹配前面的子表达式一次或多次                      |
| .	\.	匹配除换行符 \n 之外的任何单字符                  |
| [ ]	\[\]	标记一个中括号表达式的开始。要匹配 [，请使用 [。 |
| ?	\?	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符 |
| \	\\	将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符 |
| ^	\^	匹配输入字符串的开始位置，除非在方括号表达式中使用，当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合 |
| {}	\{\}	标记限定符表达式的开始                         |
| \                                                            |
| 限定符表达                                                   |
| Note 表含义中的出现次数：限定符前面字符的出现次数。          |
| 限定符	表达含义                                           |
| *	出现次数>=0                                             |
| +	出现次数>=1                                             |
| ?	出现次数 0 or 1, 等价{0,1}                              |
| {n}	出现次数=n                                            |
| {n,}	出现次数>=n                                          |
| {n, m}	n=< 出现次数<= m                                   |
| 定位符                                                       |
| 定位符	表达含义                                           |
| ^	字符串开始的位置                                        |
| $	字符串结束的位置                                        |
| \b	限定单词(字)的字符，常用来确定一个单词，可以结合两个‘\b’使用 |
| \B	限定非单词(字)边界的字符，用的很少                     |

#### 202. 快乐数

难度简单

编写一个算法来判断一个数 `n` 是不是快乐数。

「快乐数」定义为：

- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果 **可以变为** 1，那么这个数就是快乐数。

如果 `n` 是快乐数就返回 `true` ；不是，则返回 `false` 。

**示例 1：**

```
输入：19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**示例 2：**

```
输入：n = 2
输出：false
```

**解题思路**

 根据题意，我们可以分析如下：

1. 找到快乐数
2. 没有快乐数，形成环路，造成死循环。

首先，我们肯定可以使用哈希表记录过程值，若找到 11，皆大欢喜。

如果在找的过程中，哈希表中已存在当前数，则证明进入了环路，也就是死循环了！

此时，我们就可以判断当前数不是一个快乐数了~

但是，为了降低空间复杂度，我们选择使用快慢指针来解决，流程如下：

###### 快慢指针

- 创建一个慢指针，一次走一步，再创建一个快指针，一次走两步。
- 当快慢指针相遇，代表形参环路，该数不是快乐数。
- 若指针移动过程中，找到了 11，则当前数是一个快乐数。

```js
let getNext = function (n) {
    return n.toString().split('').map(i => i ** 2).reduce((a, b) => a + b);
}
let isHappy = function (n) {
    let slow = n;
    let fast = getNext(n);
    while(fast !== 1 && fast !== slow){
        slow = getNext(slow);
        fast = getNext(getNext(fast));
    }
    return fast === 1;
};
```

时间复杂度：O*(log*n)

空间复杂度：O(1)*O*(1)

#### 203. 移除链表元素

难度简单

删除链表中等于给定值 ***val\*** 的所有节点。

**示例:**

```
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
```

###### 哨兵节点

- 初始化哨兵节点为 ListNode 且设置 res.next = head。
- 比较当前节点的值和目标值是否相等，若相等则将指针指向下一个节点；不等，则等于指向当前节点
- 返回 res.next。

```js
var removeElements = function(head, val) {
    let res = new ListNode();//哑节点
    res.next = head;
    let now = res;
    while (now.next) {
        if (now.next.val == val) {
            now.next = now.next.next;
        } else {
            now = now.next;
        }
    }
    return res.next;
};
```

- 时间复杂度：O(*N*)，只遍历了一次。
- 空间复杂度：O(1)。

#### 217.存在重复元素

难度简单

给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 `true` 。如果数组中每个元素都不相同，则返回 `false` 

###### 解法1：集合法

判断原数组和该数组的长度相不相等：

```js
var containsDuplicate = function(nums) {
    return new Set(nums).size != nums.length;
};
```

```
def containsDuplicate(self, nums: List[int]) -> bool:
    return len((set(nums))) != len(nums)
```

解法2：哈希表

```js
var containsDuplicate = function(nums) {
    let set = new Set();
    for(let i = 0, len = nums.length; i < len; i++) {
        if(set.has(nums[i])) {
            return true;
        }
        set.add(nums[i])
    }
    return false;
};
```

```
def containsDuplicate(self, nums: List[int]) -> bool:
    dic = {}
    for i in nums:
        if dic.get(i):
            return True
        dic[i] = 1
    return False
```

###### 解法3：排序法

排序之后，相等元素必相邻：

```js
var containsDuplicate = function(nums) {
    nums.sort((a,b) => a - b);
    for(let i = 1, len = nums.length; i < len; i++) {
        if(nums[i - 1] == nums[i]) {
            return true;
        }
    }
    return false;
};
```

```
def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]:
            return True
    return False
```

#### 237. 删除链表中的节点

难度简单

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 **要被删除的节点** 。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/237_example.png)

 

**示例 1：**

```
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

**示例 2：**

```
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```

**提示：**

- 链表至少包含两个节点。
- 链表中所有节点的值都是唯一的。
- 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
- 不要从你的函数中返回任何结果。

###### 链表与下一个节点交换

因链表无法获取删除节点的上一个节点，所以将删除节点赋值为下一个节点，然后直接删除下一个节点即可

```js
var deleteNode = function(node) {
    node.val = node.next.val;
    node.next = node.next.next;
};
```

- 时间和空间复杂度都是：*O*(1)。

#### 258. 各位相加

难度简单

给定一个非负整数 `num`，反复将各个位上的数字相加，直到结果为一位数。

**示例:**

```
输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
```

###### 数学归纳法

9的倍数递减

num%9，若不为0则返回num，为0则返回9

```js
var addDigits = function(num) {
    if (num < 10) return num
    return num % 9 || 9
};
```

- 时间复杂度：O(1)
- 空间复杂度：O(1)

###### 数字转字符，分割，相加

```js
function addNumber(num) {
    while(num >= 10){
        num = num.toString().split('').reduce((res,i)=>res+=parseInt(i),0);
    }
    return num;
}
```

- 时间复杂度：O(n)
- 空间复杂度：O(1)

#### 263. 丑数

难度简单

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 `2, 3, 5` 的**正整数**。

**示例 1:**

```
输入: 6
输出: true
解释: 6 = 2 × 3
```

**示例 2:**

```
输入: 8
输出: true
解释: 8 = 2 × 2 × 2
```

**示例 3:**

```
输入: 14
输出: false 
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
```

**说明：**

1. `1` 是丑数。
2. 输入不会超过 32 位有符号整数的范围: [−231, 231 − 1]。

###### **对num 不断除以 2,3,5**

```js
/**
 * @param {number} num
 * @return {boolean}
 */
var isUgly = function(num) {
  let arr = [2, 3, 5]
  for(let a of arr){
    while(num % a === 0 && num > 1) num /= a
  }
  return num == 1
};
```

```js
/**
 * @param {number} num
 * @return {boolean}
 */
var isUgly = function (num) {
    if (num < 1) return false;
    if (num === 1) return true;
    while (num % 5 === 0) {
        num /= 5;
    }
    while (num % 3 === 0) {
        num /= 3;
    }
    while (num % 2 === 0) {
        num /= 2;
    }
    return num === 1;
};
```

#### 268. 丢失的数字

难度简单

给定一个包含 `[0, n]` 中 `n` 个数的数组 `nums` ，找出 `[0, n]` 这个范围内没有出现在数组中的那个数。

**进阶：**

- 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

**示例 1：**

```
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
```

**示例 2：**

```
输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
```

**示例 3：**

```
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
```

**示例 4：**

```
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
```

**提示：**

- `n == nums.length`
- `1 <= n <= 104`
- `0 <= nums[i] <= n`
- `nums` 中的所有数字都 **独一无二**

###### 求和公式

```JS
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let len = nums.length;
    let sum = (len * (len + 1)) /2;//求和公式
    let total = 0;
    for (let i = 0; i < len; i++) {
        total += nums[i]; 
    }
    return sum - total;
};
```

时间复杂度：O(n)。求出数组中所有数的和的时间复杂度为 O(n)，高斯求和公式的时间复杂度为 O(1)，因此总的时间复杂度为 O(n)。
空间复杂度：O(1)。算法中只用到了 O(1) 的额外空间，用来存储答案。

###### 排序

首先我们对数组进行排序，随后我们可以在常数时间内判断两种特殊情况：0 没有出现在数组的首位，以及 n 没有出现在数组的末位。如果这两种特殊情况都不满足，那么缺失的数字一定在 0 和 n 之间（不包括两者）。此时我们可以在线性时间内扫描这个数组，如果某一个数比它前面的那个数大了超过 1，那么这两个数之间的那个数即为缺失的数字。

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort((a, b) =>  a - b)
    if(nums[nums.length - 1] != nums.length) {// 判断 n 是否出现在末位
        return nums.length;
    }else if (nums[0] != 0) {// 判断 0 是否出现在首位
        return 0;
    }
    // 此时缺失的数字一定在 (0, n) 中
    for (let i = 1; i < nums.length; i++) {
        let expectedNum = nums[i - 1] + 1;
        if (nums[i] != expectedNum) {//如果这一个数不等于它前面的 + 1
            return expectedNum;
        }
    }
    // 未缺失任何数字（保证函数有返回值）
    return -1;
};
```

时间复杂度：O(nlogn)。由于排序的时间复杂度为 O(nlogn)，扫描数组的时间复杂度为 O(n)，因此总的时间复杂度为 O(nlogn)。
空间复杂度：O(1) 或O(n)。空间复杂度取决于使用的排序算法，根据排序算法是否进行原地排序（即不使用额外的数组进行临时存储），空间复杂度为 O(1) 或 O(n)。

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

###### 内置函数

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

###### 双指针

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

#### 343.整数拆分

难度中等

给定一个正整数 *n*，将其拆分为**至少**两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

**示例 1:**

```
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
```

**示例 2:**

```
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
```

###### 数学

- 当 n≤3 时，最大乘积是 n-1。
- n可以分解最多的3和最少的2个数
- 例如n=10时，最多的3为：3331；但是由于1对于求解乘法最大值没有贡献，所以需将后面的31改为22

```js
var integerBreak = function(n) {
    if (n < 4) return n - 1;

    let result = 1;

    while (n > 4) {
        result *= 3;
        n -= 3;
    }
    return result * n;
};
```

#### 350.两个数组的交集II

难度简单

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

双指针

- 两个数组排序
- 设定两个为0的指针，比较两个指针的元素是否相等
- 如果相等，元素push到返回值里，两个指针同时往前
- 如果不相等，元素小的指针往前
- 如果相等，那肯定比较过的元素就没用了，两个指针++

如果不相等，那把元素小的数组指针++。

因为大元素可能在小元素数组里存在，但是小元素在大元素所在数组肯定不存在。因为已经排过序了。

```js
var intersect = function(nums1, nums2) {
    let p1 = 0
    let p2 = 0
    let res = []
    nums1 = nums1.sort((a, b) => a - b)
    nums2 = nums2.sort((a, b) => a - b)
    while(p1 < nums1.length && p2 < nums2.length) {
        if(nums1[p1] == nums2[p2]) {
            res.push(nums1[p1])
            p1++
            p2++
        } else if(nums1[p1] < nums2[p2]) {
            p1++
        } else {
            p2++
        }
    }
    return res
};
```

###### 内置函数

利用python List中append与remove方法的特点进行操作。循环遍历nums1中的元素，然后在nums2中查找是否存在。如果存在，加入临时list中，并且需要注意：把nums2中的对应元素删掉。比如nums1 = [1, 2, 2, 1]， nums2 = [2]。如果不删除，则会产生错误。因为nums1与nums2的元素个数要保持一致。

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

#### 371.两整数之和

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

###### 通过&运算和^运算实现加法

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

#### 392. 判断子序列

难度简单

给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

你可以认为 **s** 和 **t** 中仅包含英文小写字母。字符串 **t** 可能会很长（长度 ~= 500,000），而 **s** 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，`"ace"`是`"abcde"`的一个子序列，而`"aec"`不是）。

**示例 1:**
**s** = `"abc"`, **t** = `"ahbgdc"`

返回 `true`.

**示例 2:**
**s** = `"axc"`, **t** = `"ahbgdc"`

返回 `false`.

###### 双指针 

- 两个指针分别扫描长串和短串，如果指向的字符相同，两个指针都移动考察下一个字符
- 如果不相同，短串的指针不动，长串的指针移动考察下一个字符
- 如果短串走完了，说明短串中的字符在长串中都有匹配
- 如果短串没有走完，长串走完了，说明考察了整个长串也没能找齐短串的所有字符

```js
var isSubsequence = function(s, t) {
    if(s.length === 0) return true;

    let index = 0;
    let subIndex = 0;
    //判断长串是否走完
    while(index < t.length) {
        if(s[subIndex] === t[index]) {
            //短串的指针移动到下一个字符
            subIndex++;
            //判断短串是否走完，如果短串走完了，说明短串中的字符在长串中都有匹配
            if(subIndex > s.length - 1) {
                return true
            }
        }
        //长串的指针移动到下一个字符
        index++;
    } 
    return false;
};
```

######  递归

如果`s`是空：

- 返回`True`。

```js
var isSubsequence = function(s, t) {
    if(s.length === 0) return true;

    let i = 0;
    while(i < t.length) {//判断长串是否走完
        if(s[0] == t[i]) {
            const rest_s = s.substring(1);
            const rest_t = t.substring(i + 1);
            return isSubsequence(rest_s, rest_t);
        }
        i++;
    } 
    return false
};
```

#### 448. 找到所有数组中消失的数字

难度简单

给定一个范围在 1 ≤ a[i] ≤ *n* ( *n* = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。

找到所有在 [1, *n*] 范围之间没有出现在数组中的数字。

您能在不使用额外空间且时间复杂度为*O(n)*的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

**示例:**

```
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
```

###### 原地修改

用一个哈希表记录数组 nums 中的数字，由于数字范围均在 [1,n][1,n] 中，记录数字后我们再利用哈希表检查 [1,n][1,n] 中的每一个数是否出现，从而找到缺失的数字。

由于数字范围均在 [1,n][1,n] 中，我们也可以用一个长度为 n 的数组来代替哈希表。这一做法的空间复杂度是 O(n) 的。我们的目标是优化空间复杂度到 O(1)。

注意到 nums 的长度恰好也为 n，能否让 nums 充当哈希表呢？

由于nums 的数字范围均在 [1,n][1,n] 中，我们可以利用这一范围之外的数字，来表达「是否存在」的含义。

具体来说，遍历nums，每遇到一个数 x，就让 nums[x−1] 增加 n。由于 nums 中所有数均在 [1,n][1,n] 中，增加以后，这些数必然大于 n。最后我们遍历 nums，若 nums[i] 未大于 n，就说明没有遇到过数 i+1。这样我们就找到了缺失的数字。

注意，当我们遍历到某个位置时，其中的数可能已经被增加过，因此需要对 n 取模来还原出它本来的值。

```js
var findDisappearedNumbers = function(nums) {
    const n = nums.length;
    for (const num of nums) {
        // nums[num−1] + n
        const x = (num - 1) % n;
        nums[x] += n;
    }
    const ret = [];
    for (const [i, num] of nums.entries()) {
        if (num <= n) {//若 nums[i] 未大于 n，就说明没有遇到过数 i+1
            ret.push(i + 1);
        }
    }
    return ret;
};
```

- 时间复杂度：*O*(*n*)。其中 n 是数组 *nums* 的长度。
- 空间复杂度：*O*(1)。返回值不计入空间复杂度。

#### 456. 132 模式

难度中等

给你一个整数数组 `nums` ，数组中共有 `n` 个整数。**132 模式的子序列** 由三个整数 `nums[i]`、`nums[j]` 和 `nums[k]` 组成，并同时满足：`i < j < k` 和 `nums[i] < nums[k] < nums[j]` 。

如果 `nums` 中存在 **132 模式的子序列** ，返回 `true` ；否则，返回 `false` 。

**进阶：**很容易想到时间复杂度为 `O(n^2)` 的解决方案，你可以设计一个时间复杂度为 `O(n logn)` 或 `O(n)` 的解决方案吗？

**示例 1：**

```
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
```

**示例 2：**

```
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
```

**示例 3：**

```
输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
```

######  枚举

```js
var find132pattern = function(nums) {
    const n = nums.length;
    const candidate_k = [nums[n - 1]];
    let max_k = -Number.MAX_SAFE_INTEGER;

    for (let i = n - 2; i >= 0; --i) {
        if (nums[i] < max_k) {
            return true;
        }
        while (candidate_k.length && nums[i] > candidate_k[candidate_k.length - 1]) {
            max_k = candidate_k[candidate_k.length - 1];
            candidate_k.pop();
        }
        if (nums[i] > max_k) {
            candidate_k.push(nums[i]);
        }
    }
    return false;
};
```

时间复杂度：O(n)，枚举 i 的次数为 O(n)，由于每一个元素最多被加入和弹出单调栈各一次，因此操作单调栈的时间复杂度一共为 O(n)，总时间复杂度为 O(n)。

空间复杂度：O(n)，即为单调栈需要使用的空间。

#### 538. 把二叉搜索树转换为累加树

难度简单

给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 原始二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13

前言
二叉搜索树是一棵空树，或者是具有下列性质的二叉树：

若它的左子树不空，则左子树上所有节点的值均小于它的根节点的值；

若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值；

它的左、右子树也分别为二叉搜索树。

由这样的性质我们可以发现，二叉搜索树的中序遍历是一个单调递增的有序序列。如果我们反序地中序遍历该二叉搜索树，即可得到一个单调递减的有序序列。

###### 反序中序遍历

- 反序中序遍历该二叉搜索树，记录过程中的节点值之和，并不断更新当前遍历到的节点的节点值，即可得到题目要求的累加树

```js
var convertBST = function(root) {
    let sum = 0;
    const inOrder = (root) => {
        if(root != null){
            inOrder(root.right);// 先进入右子树
            sum += root.val;// 节点值累加给sum
            root.val = sum; // 累加的结果，赋给root.val
            inOrder(root.left)// 然后才进入左子树
        }
    }
    inOrder(root);
    return root;
};
```

复杂度分析

- 时间复杂度：O(n)，其中 n 是二叉搜索树的节点数。每一个节点恰好被遍历一次。
- 空间复杂度：O(n)，为递归过程中栈的开销，平均情况下为 O(log n)，最坏情况下树呈现链状，为 O(n)

#### 617. 合并二叉树

难度简单

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则**不为** NULL 的节点将直接作为新二叉树的节点。

###### 深度优先搜索

```js
var mergeTrees = function(t1, t2) {
    if(!t1) return t2 //若t1节点为空，那直接返回t2节点，不管t2是否为空
    if(!t2) return t1 //若t2为空，那肯定t1肯定不为空，返回t1节点
    t1.val = t1.val + t2.val //执行到这里证明t1与t2节点均不为空，那就两值相加，替换t1原来的值
    t1.left = mergeTrees(t1.left, t2.left ) //递归遍历两者的左子树
    t1.right = mergeTrees(t1.right, t2.right) ////递归遍历两者的右左子树
    return t1 //t1是返回的根节点，因为都拼到t1树上了
};
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)

#### 657. 机器人能否返回原点

难度简单

在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 **(0, 0) 处结束**。

移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 `R`（右），`L`（左），`U`（上）和 `D`（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

**注意：**机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

###### 模拟

解题思路：用两个变量 x 和 y来表示机器人当前所在的坐标为 (x,y)，起始时 x=0，y=0y。接下来我们遍历指令并更新机器人的坐标：

- 如果指令是 U，则令 y=y-1
- 如果指令是 D，则令 y=y+1
- 如果指令是 L，则令 x=x-1
- 如果指令是 R，则令 x=x+1

最后判断 (x,y) 是否为 (0,0) 即可。

```js
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    var x = 0, y = 0;
    var length = moves.length;
    for(var i = 0; i < length; i ++){
        var move = moves[i]
        if(move == 'U'){
            y--
        }else if(move == 'D'){
            y++
        }else if(move == 'L'){
            x--
        }else if(move == 'R'){
            x++
        }
    }
    return x == 0 && y ==0
};
```

时间复杂度： O(N)，其中 N 表示moves 指令串的长度。我们只需要遍历一遍字符串即可。

空间复杂度： O(1)。我们只需要常数的空间来存放若干变量。

方法二

```js
/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
   let x = 0, y = 0;
   for(let m of moves){
       switch(m){
           case 'U': y--; break;
           case 'D': y++; break;
           case 'L': x--; break;
           case 'R': x++; break;
       }
   }
   return x === 0 && y === 0
};
```

#### 1185. 一周中的第几天

难度简单

给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数：`day`、`month` 和 `year`，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}`。

###### 内置函数

```js
var dayOfTheWeek = function (day, month, year) {
    let listQuery = new Date(year + '-' + month + '-' + day).getDay()
    let tempArr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return tempArr[listQuery]
};
```

###### 模拟

- 计算和1971第一天相隔的天数，然后取余

```js
/**
 * @param {number} day
 * @param {number} month
 * @param {number} year
 * @return {string}
 */
var dayOfTheWeek = function(day, month, year) {
    var weekStr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    //记录每月天数
    var months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    var sum = 4
    if(year > 1971){
        //计算从查找的那一年和1971间隔多少天
        for(var i = 1971; i < year; i++){
            //天数相加
            sum += 365
            if(i % 4 == 0 && i % 100 != 0 || i % 400 == 0){
                //如果是闰年天数再加1
                sum++
            }
        }
        //加上查找的那一年每月的天数
        for(var i = 0; i < month -1; i++){
            sum += months[i]
        }
        if(month >= 3 && (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)){
            sum ++
        }
        //加上查找的那一年当月的天数
        sum += day
        //取余
        return weekStr[sum % 7]
    }  
};
```

#### 1431. 拥有最多糖果的孩子

难度简单

给你一个数组 `candies` 和一个整数 `extraCandies` ，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 `extraCandies` 个糖果分配给孩子们之后，此孩子有 **最多** 的糖果。注意，允许有多个孩子同时拥有 **最多** 的糖果数目。

**示例 1：**

```
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true] 
解释：
孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
```

**示例 2：**

```
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false] 
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
```

**示例 3：**

```
输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]
```

######  遍历

**思路**

如果我们希望某个小朋友拥有的糖果最多，那么最优的方案当然是把额外的所有糖果都分给这个小朋友。因此，我们可以枚举每一个小朋友，并将额外的所有糖果都分给这个小朋友，然后再用 O(n) 的时间遍历其余的小朋友，就可以判断这个小朋友是否拥有最多的糖果。

上述方法的时间复杂度为 O(n^2)，然而我们可以将其优化为 O(n)。事实上，对于每一个小朋友，只要这个小朋友「拥有的糖果数目」加上「额外的糖果数目」大于等于所有小朋友拥有的糖果数目最大值，那么这个小朋友就可以拥有最多的糖果。

**证明**

设某个小朋友的糖果数为 x，其余小朋友拥有的糖果数目最大值为 y，额外的糖果数为 e。这个小朋友可以拥有最多的糖果，当且仅当
x+e≥y

由于x+e≥x 显然成立，那么我们有
														x+e≥max(x,y)

而 max(x,y) 就是所有小朋友拥有的糖果数目最大值。因此我们可以预处理出这个值，随后遍历每一个小朋友，只要这个小朋友「拥有的糖果数目」加上「额外的糖果数目」大于等于这个值，就可以满足要求。

```js
/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    const len = candies.length;
    let maxCandies = 0;
    for (let i = 0; i < len; i++) {
        maxCandies = Math.max(maxCandies, candies[i]);
    }
    let ret = [];
    for (let j = 0; j < len; j++) {
        ret.push(candies[j] + extraCandies >= maxCandies);
    }
    return ret;
};
```

**复杂度分析**

假设小朋友的总数为 n。

时间复杂度：我们首先使用 O(n) 的时间预处理出所有小朋友拥有的糖果数目最大值。对于每一个小朋友，我们需要O(1) 的时间判断这个小朋友是否可以拥有最多的糖果，故渐进时间复杂度为 O(n)

空间复杂度：这里只用了常数个变量作为辅助空间，与 nn 的规模无关，故渐进空间复杂度为 O(1)

#### 1672. 最富有客户的资产总量

难度简单

给你一个 `m x n` 的整数网格 `accounts` ，其中 `accounts[i][j]` 是第 `i` 位客户在第 `j` 家银行托管的资产数量。返回最富有客户所拥有的 **资产总量** 。

客户的 **资产总量** 就是他们在各家银行托管的资产数量之和。最富有客户就是 **资产总量** 最大的客户。

**示例 1：**

```
输入：accounts = [[1,2,3],[3,2,1]]
输出：6
解释：
第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。
```

**示例 2：**

```
输入：accounts = [[1,5],[7,3],[3,5]]
输出：10
解释：
第 1 位客户的资产总量 = 6
第 2 位客户的资产总量 = 10 
第 3 位客户的资产总量 = 8
第 2 位客户是最富有的，资产总量是 10
```

**示例 3：**

```
输入：accounts = [[2,8,7],[7,1,3],[1,9,5]]
输出：17
```

######  暴力解法

```js
/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let max = 0, sum = 0;
    for (let i = 0; i < accounts.length; i++) {
        for (let j = 0; j < accounts[i].length; j++) {
            sum = accounts[i][j] + sum;
        }
        if (sum > max) {
            max = sum;
            sum = 0;
        }else {
            sum = 0;
        }
    }
    return max;
};
```

#### 2. 两数相加

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

15. #### 三数之和

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

###### 数组遍历

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

#### 5. 最长回文子串

难度中等

给定一个字符串 `s`，找到 `s` 中最长的回文子串。你可以假设 `s` 的最大长度为 1000。

**示例 1：**

```
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```

**示例 2：**

```
输入: "cbbd"
输出: "bb"
```

###### 动态规划

如果一个字符串是回文串，那么在它左右分别加上一个相同的字符，那么它一定还是一个回文串
如果在一个不是回文字符串的字符串两端添加任何字符，或者在回文串左右分别加不同的字符，得到的一定不是回文串

```
//状态转移方程
if (s[i] === s[j] && dp[i + 1][j - 1]) {
  dp[i][j] = true;
}
```

```js
var longestPalindrome = function(s) {
  if (!s || s.length === 0) return "";
  let res = s[0];

  const dp = [];
  for (let i = s.length - 1; i >= 0; i--) {
    dp[i] = [];
    for (let j = i; j < s.length; j++) {
      if (j - i === 0) dp[i][j] = true;
      else if (j - i === 1 && s[i] === s[j]) dp[i][j] = true;
      else if (s[i] === s[j] && dp[i + 1][j - 1]) {
        dp[i][j] = true;
      }

      if (dp[i][j] && j - i + 1 > res.length) {
        res = s.slice(i, j + 1);
      }
    }
  }

  return res;
};
```

#### 36. 有效的数独

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

###### 哈希判重

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

###### py按规则逐条判断，9行+9列+9块

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
```

#### 48. 旋转图像

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


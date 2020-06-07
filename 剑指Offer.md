### 剑指OFFER

面试题03. 数组中重复的数字

面试题05. 替换空格

面试题10- I. 斐波那契数列

面试题10- II. 青蛙跳台阶问题

面试题29. 顺时针打印矩阵

面试题64. 求1+2+…+n

面试题 16.11. 跳水板

#### [面试题03. 数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

难度简单

找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

**示例 1：**

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```

**限制：**

```
2 <= n <= 100000
```

###### 遍历数组

由于只需要找出数组中任意一个重复的数字，因此遍历数组，遇到重复的数字即返回。为了判断一个数字是否重复遇到，使用集合存储已经遇到的数字，如果遇到的一个数字已经在集合中，则当前的数字是重复数字。

```JS
var findRepeatNumber = function(nums) {
    const map = {};
    for (const num of nums) {
        if (!map[num]) {
            map[num] = true;
        } else {
            return num;
        }
    }
};
```

###### set

使用set,因为set自动忽略重复元素，遍历数组中元素，若长度未增加，则输出当前元素

```js
var findRepeatNumber = function(nums) {
    let s=new Set();
    for(var i in nums){
        var curLenth=s.size;
        s.add(nums[i]);
        if(s.size==curLenth)
        return nums[i];
    }
};
```

#### [面试题05. 替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/)

难度简单20

请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

**示例 1：**

```
输入：s = "We are happy."
输出："We%20are%20happy."
```

###### 正则表达式

```js
var replaceSpace = function(s) {
    return s.replace(/ /g, '%20');
};
```

###### split() + join()

split() 方法用于把一个字符串分割成字符串数组。
join() 方法用于把数组中的所有元素放入一个字符串。

```js
var replaceSpace = function(s) {
   return s.split(" ").join("%20");
};
```

###### 遍历字符串

```js
var replaceSpace = function(s) {
  let res = "";
  for (const el of s) {
    if (el === " ") {
      res += "%20";
    } else {
      res += el;
    }
  }
  return res;
};
```

#### [面试题10- I. 斐波那契数列](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)

难度简单

写一个函数，输入 `n` ，求斐波那契（Fibonacci）数列的第 `n` 项。斐波那契数列的定义如下：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```
输入：n = 2
输出：1
```

**示例 2：**

```
输入：n = 5
输出：5
```

**提示：**

- `0 <= n <= 100`

###### 递归1

fib会重复计算之前的项，计算结果是一次性的，浪费时间和空间

超出时间限制

```js
var fib = function(n) {
    if(n<=1) return n;
    return  (fib(n-1) + fib(n-2)) % 1000000007;
};
```

###### 循环

```js
var fib = function(n) {
    if(n === 0) return 0
    if(n === 1) return 1
    let a = 0
    let b = 1
    for(let i = 1;i < n;i++){
        let t = a
        a = b
        b = (t + b) % 1000000007
    }
    return b
};
```

执行用时 :72 ms, 在所有 JavaScript 提交中击败了31.28%的用户

内存消耗 :32.2 MB, 在所有 JavaScript 提交中击败了100.00%的用户



#### [面试题10- II. 青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

难度简单34

一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 `n` 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

**示例 1：**

```
输入：n = 2
输出：2
```

**示例 2：**

```
输入：n = 7
输出：21
```

**提示：**

- `0 <= n <= 100`

注意：本题与主站 70 题相同

###### 1.第i个斐波那契数

- 3个变量 每次递归更新前两个子问题所需步数
- 可知递推公式  f(n) = f(n-2) + f(n-1),n>=1

```js
var numWays = function(n) {
    if(n == 0){
        return 1;
    }
    if(n == 1){
        return 1;
    }
    if(n == 2){
        return 2;
    }
    //f1第一阶 f2第二阶 f3下一阶
    var f1 = 1,f2 =2, f3 = 0;
    while(n > 2) {
        f3 = (f1 + f2) % 1000000007;
        f1 = f2;
        f2 = f3;
        n--;
    }
    return f2;
};
```

执行用时 :60 ms, 在所有 JavaScript 提交中击败了85.61%的用户

内存消耗 :32.7 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 2.递归

```js
var numWays = function(n) {
    let arr = [1,1];
    for(let i = 2; i <= n; i++) {
        arr[i] = (arr[i - 1] + arr[i -2]) %1000000007;
    }
    return arr[n];
};
```

执行用时 :64 ms, 在所有 JavaScript 提交中击败了70.67%的用户

内存消耗 :32.8 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 3.动态规划

爬第n阶楼梯的方法数量，等于 2 部分之和

爬上 n-1阶楼梯的方法数量。因为再爬1阶就能到第n阶
爬上 n-2 阶楼梯的方法数量，因为再爬2阶就能到第n阶

```js
var numWays = function(n) {
    var dp = new Array(n+1);
    dp[0]=1;
    dp[1]=1;
    for (var i =2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
        dp[i] %= 1000000007;
    }
    return dp[n]
};
```

执行用时 :64 ms, 在所有 JavaScript 提交中击败了70.67%的用户

内存消耗 :32.6 MB, 在所有 JavaScript 提交中击败了100.00%的用户

#### [面试题29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

难度简单

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

**示例 1：**

```
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

**示例 2：**

```
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

**限制：**

- `0 <= matrix.length <= 100`

- `0 <= matrix[i].length <= 100`

###### 模拟

可以模拟打印矩阵的路径。初始位置是矩阵的左上角，初始方向是向右，当路径超出界限或者进入之前访问过的位置时，则顺时针旋转，进入下一个方向。

- 一层层向里处理，按顺时针依次遍历：上层、右层、下层、左层
- - 不再形成“环”了，剩下一行或一列，循环结束后单独判断

  ###### 矩阵不一定是方阵，循环结束时的情形：

top < bottom && left < right 是 while 循环的条件
无法构成“环”了，就退出循环，分 3 种情况：
top === bottom && left < right —— 剩一行
top < bottom && left === right —— 剩一列
top === bottom && left === right —— 剩一项（也是一行/列）

​     处理剩下的单行或单列

因为是按顺时针推入结果数组的，所以
剩下的一行，从左至右 依次推入结果数组
剩下的一列，从上至下 依次推入结果数组

```js
var spiralOrder = function (matrix) {
  if (matrix.length === 0) return []
  const res = []
  let top = 0, bottom = matrix.length - 1, left = 0, right = matrix[0].length - 1
  while (top < bottom && left < right) {
    for (let i = left; i < right; i++) res.push(matrix[top][i])   // 上层
    for (let i = top; i < bottom; i++) res.push(matrix[i][right]) // 右层
    for (let i = right; i > left; i--) res.push(matrix[bottom][i])// 下层
    for (let i = bo5；ttom; i > top; i--) res.push(matrix[i][left])  // 左层
    right--
    top++
    bottom--
    left++  // 四个边界同时收缩，进入内层
  }
  if (top === bottom) // 剩下一行，从左到右依次添加
    for (let i = left; i <= right; i++) res.push(matrix[top][i])
  else if (left === right) // 剩下一列，从上到下依次添加
    for (let i = top; i <= bottom; i++) res.push(matrix[i][left])
  return res
};
```



#### [面试题64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

难度中等

求 `1+2+...+n` ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

**示例 1：**

```
输入: n = 3
输出: 6
```

**示例 2：**

```
输入: n = 9
输出: 45
```

**限制：**

- `1 <= n <= 10000`

###### 递归 和 &&

&& 特性：

对于 A && B 这个表达式，如果 A 表达式返回 False ，那么 A && B 已经确定为 False ，此时不会去执行表达式 B。同理，对于逻辑运算符 ||， 对于 A || B 这个表达式，如果 A 表达式返回 True ，那么 A || B 已经确定为 True ，此时不会去执行表达式 B

如果左边表达式为 false，不执行右边； 左边为true继续执行右边。

传入 n
return n && n + (n-1) => n + (n-1)
return 1 && n + (n-1) + ... + 1 => n + (n-1) + ... + 1
return 0 && 不执行
最后得到的结果： n + (n-1) + ... + 1

```js
var sumNums = function(n) {
    return n && (n + sumNums(n - 1));
};
```

#### [面试题 16.11. 跳水板](https://leetcode-cn.com/problems/diving-board-lcci/)

难度简单9

你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为`shorter`，长度较长的木板长度为`longer`。你必须正好使用`k`块木板。编写一个方法，生成跳水板所有可能的长度。

返回的长度需要从小到大排列。

**示例：**

```
输入：
shorter = 1
longer = 2
k = 3
输出： {3,4,5,6}
```

**提示：**

- 0 < shorter <= longer
- 0 <= k <= 100000

###### 数学归纳法

k 等于0 时返回 空数组
shorter == longer 相等时 返回一个 值 [shorter*k]

当两类板长度不同时，短板数越多则总长就最短，依次排列即可。

根据数学归纳法，2种长度板子，必须用k块，不同的情况共k+1中，公式为(k - i) * shorter + i * longer

```js
var divingBoard = function(shorter, longer, k) {
    if(k == 0) return []
    if(shorter == longer) return [shorter*k]
    var arr = []
    for(let i = 0;i <= k;i++){
        arr.push(i * longer + shorter * (k-i))
    }
    //for(let i = 0,j = k; i < k+1, j > -1;j--, i++){
      //  arr.push(j * shorter + longer * i)
    //}
    return arr
};
```

执行用时 :152 ms, 在所有 JavaScript 提交中击败了99.00%的用户

内存消耗 :47.7 MB, 在所有 JavaScript 提交中击败了100.00%的用户
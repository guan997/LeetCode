### 剑指OFFER

[面试题 02.01. 移除重复节点](#面试题 02.01. 移除重复节点)

[面试题03. 数组中重复的数字](#面试题03. 数组中重复的数字)

[面试题05. 替换空格](#面试题05. 替换空格)

[面试题06. 从尾到头打印链表](#面试题06. 从尾到头打印链表)

[面试题 08.06. 汉诺塔问题](#面试题 08.06. 汉诺塔问题)

[面试题10- I. 斐波那契数列](#面试题10- I. 斐波那契数列)

[面试题10- II. 青蛙跳台阶问题](#面试题10- II. 青蛙跳台阶问题)

[剑指 Offer 11. 旋转数组的最小数字](#剑指 Offer 11. 旋转数组的最小数字)

[剑指 Offer 18. 删除链表的节点](#剑指 Offer 18. 删除链表的节点)

[剑指 Offer 22.链表中倒数第k个节点](#剑指Offer 22.链表中倒数第k个节点)

[面试题29. 顺时针打印矩阵](#面试题29. 顺时针打印矩阵)

[剑指 Offer 57. 和为s的两个数字](#剑指 Offer 57. 和为s的两个数字)

[面试题64. 求1+2+…+n](#面试题64. 求1+2+…+n)

[面试题 16.11. 跳水板](#面试题 16.11. 跳水板)

[面试题17. 打印从1到最大的n位数](#面试题17. 打印从1到最大的n位数)

[剑指 Offer 24. 反转链表](#剑指 Offer 24. 反转链表)

[面试题46. 把数字翻译成字符串](#面试题46. 把数字翻译成字符串)

#### 面试题 02.01. 移除重复节点

难度简单

编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

**示例1:**

```
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
```

**示例2:**

```
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
```

**提示：**

1. 链表长度在[0, 20000]范围内。
2. 链表元素在[0, 20000]范围内。

###### hash 去重

 利用 map，边遍历边移除
 如果节点值没出现过，那么正常两个指针向后走，
 如果节点值出现过了，那么 curr 向后走，prev.next 指向 curr，跳过这个节点

```js
var removeDuplicateNodes = function(head) {
    let map = {}, 
     newHead = new ListNode(null),
     prev = newHead, 
     curr = head;
     newHead.next = head;

    while(curr) {
        let currVal = curr.val;
        if(map[currVal] === undefined) {
            map[currVal] = true;
            prev = curr;
            curr = curr.next;
        }else {
            curr = curr.next;
            prev.next = curr;
        }
    }
     return newHead.next;
};
```

###### 双指针

固定p指针，右侧q指针扫描，然后移动p，指针q再次扫描

```js
var removeDuplicateNodes = function(head) {
    let p = head;
    while (p) {
        let q = p;
        while (q.next) {
            if (q.next.val == p.val) {
                q.next = q.next.next;
            } else {
                q = q.next;
            }
        }
        p = p.next;
    }
    return head;
};
```

#### 面试题03. 数组中重复的数字

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

#### 面试题05. 替换空格

难度简单

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

#### 面试题06. 从尾到头打印链表

难度简单

输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

**示例 1：**

```
输入：head = [1,3,2]
输出：[2,3,1]
```

###### 1.reverse() 反转法

```js
var reversePrint = function (head) {
  if (head === null) return []
  const res = []
  while (head) {
    res.push(head.val)
    head = head.next
  }
  return res.reverse()
}
```

执行用时 :84 ms, 在所有 JavaScript 提交中击败了42.73%的用户

内存消耗 :36.6 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 2.反转链表

```js
function reverseLink(head) {
    if(!head) return [];
    
    let arr = [];
    do{
        arr.push(head.val);
    }while(head = head.next);
    arr.reverse();
    return arr;
}
```

执行用时 :68 ms, 在所有 JavaScript 提交中击败了95.75%的用户

内存消耗 :36.3 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 3.递归反转链表

```js
function reverseLink(head) {
    if(!head) return []
    let arr = reversePrint(head.next)
    arr.push(head.val)
    return arr
}
```

执行用时 :80 ms, 在所有 JavaScript 提交中击败了60.56%的用户

内存消耗 :37.3 MB, 在所有 JavaScript 提交中击败了100.00%的用户

#### 面试题 08.06. 汉诺塔问题

难度简单

在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

你需要原地修改栈。

**示例1:**

```
 输入：A = [2, 1, 0], B = [], C = []
 输出：C = [2, 1, 0]
```

**示例2:**

```
 输入：A = [1, 0], B = [], C = []
 输出：C = [1, 0]
```

**提示:**

1. A中盘子的数目不大于14个。

###### **递归分治。**

将n个圆盘从A挪动到C步骤
 1. 将n-1个圆盘从A挪动到B

 2. 将第n个圆盘从A挪动到C

 3. 将n-1个圆盘从B挪动到C

  ###### 进一步拆解

  将n-1个圆盘从A挪动到B
  1.1. 将n-2个圆盘从A挪动到C
    1.2. 将第n-1个圆盘从A挪动到B
    1.3. 将n-2个圆盘从C挪动到B

  将第n个圆盘从A挪动到C

  将n-1个圆盘从B挪动到C
  3.1. 将n-2个圆盘从B挪动到A
    3.2. 将第n-1个圆盘从B挪动到C
    3.3. 将n-2个圆盘从A挪动到C

```js
var hanota = function(A, B, C) {
    // n个盘子从A到C
    function dfs(A, B, C, n){
        if(n == 0) return;
        dfs(A, C, B, n - 1)    // n - 1个盘子从A到B
        C.push(A.pop());       // n从A到C
        dfs(B, A, C, n - 1)    // n - 1个盘子从B到C  
    }
    return dfs(A, B, C, A.length);
};
```

#### 面试题10- I. 斐波那契数列

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

#### 面试题10- II. 青蛙跳台阶问题

难度简单

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
    var f1 = 1,f2 = 2, f3 = 0;
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
    for (var i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
        dp[i] %= 1000000007;
    }
    return dp[n]
};
```

执行用时 :64 ms, 在所有 JavaScript 提交中击败了70.67%的用户

内存消耗 :32.6 MB, 在所有 JavaScript 提交中击败了100.00%的用户

#### 剑指 Offer 11. 旋转数组的最小数字

难度简单115

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 `[3,4,5,1,2]` 为 `[1,2,3,4,5]` 的一个旋转，该数组的最小值为1。 

**示例 1：**

```
输入：[3,4,5,1,2]
输出：1
```

**示例 2：**

```
输入：[2,2,2,0,1]
输出：0
```

###### 双指针

```js
var minArray = function(numbers) {
    let res=numbers[0];
    // 循环一半
    for(let i=0; i<numbers.length/2; i++){
        res=Math.min(res,numbers[i],numbers[numbers.length-1-i]) // 对比头尾取最小值
    }
    return res
};
```

#### 剑指 Offer 18. 删除链表的节点

难度简单

给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

**注意：**此题对比原题有改动

**示例 1:**

```
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
```

**示例 2:**

```
输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
```

###### 递归

- 改变val值的head.next指向
- 不相等则递归子链表对比
- 终止条件：值相等

```js
var deleteNode = function(head, val) {
    if(head.val == val){
        return head.next
    }
    head.next = deleteNode(head.next,val);
    return head
};
```

#### 剑指Offer 22.链表中倒数第k个节点

难度简单56

输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

**示例：**

```
给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.
```

###### 双指针

- p,q两个指针，让p先走k步，然后p,q一起走，直到p为null

```js
var getKthFromEnd = function(head, k) {
    let p = head, q = head;

    let i = 0;
    while (p) {
        if (i >= k) {
            q = q.next;
        }
        p = p.next;
        i++;
    }
    return i < k ? null : q;
};
```

#### 面试题29. 顺时针打印矩阵

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

#### 剑指 Offer 57. 和为s的两个数字

难度简单

输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
```

**示例 2：**

```
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
```

###### 双指针法

设置左右两个指针，左指针指向数组首元素，右指针指向数组尾元素
当左右指针指向的两个元素的和大于target时，右指针减一
当左右指针指向的两个元素的和小于target时，左指针加一
当左右指针指向的两个元素的和等于target时，将两元素保存到结果数组中，退出循环即可。

```js
var twoSum = function(nums, target) {
    let left = 0;
    let right = nums.length-1;
    
    while(left < right) {
        let sum = nums[left] + nums[right];
        if(sum === target) {
            return [nums[left], nums[right]];
        }else if(sum > target) {
            -- right;
        }else if(sum < target) {
            ++ left;
        }
    }
    return -1;
};
```

#### 面试题64. 求1+2+…+n

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

#### 面试题 16.11. 跳水板

难度简单

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

#### 面试题17. 打印从1到最大的n位数

难度简单

输入数字 `n`，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

**示例 1:**

```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```

说明：

- 用返回一个整数列表来代替打印
- n 为正整数

###### 内置函数

先获取最大值，再建立一个循环，将1 - max的每一个值push到res数组中，最后返回

```js
var printNumbers = function(n) {
    //const max = 10 ** n - 1;
    const max = Math.pow(10, n) - 1;
    const res = [];
    for (let i = 1; i <= max; ++i) {
        res.push(i);
    }
    return res;
};
```

执行用时 :108 ms, 在所有 JavaScript 提交中击败了98.54%的用户

内存消耗 :45.4 MB, 在所有 JavaScript 提交中击败了100.00%的用户

#### 剑指 Offer 24. 反转链表

难度简单50

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

###### 双指针原地反转

cur:游标，一直往后循环，最后会为null
prev:记录前一个节点
oldNext:变更方向时，需要先用oldNext记住改变前的next节点，否则无法向后循环

```js
var reverseList = function(head) {
    var prev = null,cur = head,temp;
    while(cur){
        temp = cur.next;//修改前先记住下一个节点
        cur.next = prev; //改别指向，第一个节点prev是null,
        prev = cur; //记录前一个节点，供下次循环使用
        cur = temp; // cur通过temp指向下一节点
    }
    return prev;//cur会多循环直到null
};
```

#### 面试题46. 把数字翻译成字符串

难度中等

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

**示例 1:**

```
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
```

###### 1.递归-在青蛙跳台阶基础上解题

在跳台阶基础上增加跳两级的条件。

当 num 对 100 取余的余数在 [0,26) 中，就可以跳两级，否则只能跳一级

跳台阶，f(n) = f(n-1) + f(n-2)

翻译，若 n % 100 ∈ [0,26)，则 f(n) = f(n // 10) + f(n // 100)；

否则 f(n) = f(n // 10) 。// 表示向下取整。

```js
var translateNum = function(num) {
    if(num == 0){
        return 1;
    }
    if(num >= 10 && num < 26){
        return 2;
    }
    let b1 = Math.floor(num / 10), r1 = num % 10,
    b2 = Math.floor(num / 100), r2 = num % 100;
    if(r2 >= 10 && r2 < 26){
        return translateNum(b2) + translateNum(b1);
    }
    return translateNum(b1);
};
```

执行用时 :72 ms, 在所有 JavaScript 提交中击败了32.11%的用户

内存消耗 :32.3 MB, 在所有 JavaScript 提交中击败了100.00%的用户

```js
var translateNum = function(num) {
    if(num <10){
        return 1;
    }
    let dual = num % 100;
    let nextOne = Math.floor(num / 10);
    let nextTwo = Math.floor(num / 100);
    //10-25之间才有 可能双位数
    if(dual >= 10 && dual <= 25){
        return translateNum(nextOne) + translateNum(nextTwo);
    } else {
        return translateNum(nextOne)
    }
};
```

执行用时 :64 ms, 在所有 JavaScript 提交中击败了74.65%的用户

内存消耗 :32.1 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 2.动态规划

dp[0]=1，dp[1]=1 ，dp[2]=2 

dp[2]=dp[0]+dp[1]

递推公式：dp[i]=dp[i−2]+dp[i−1]

```js
const translateNum = (num) => {
  const str = num.toString()
  const n = str.length
  const dp = new Array(n + 1)
  dp[0] = 1
  dp[1] = 1
  for (let i = 2; i < n + 1; i++) {
    const temp = Number(str[i - 2] + str[i - 1])
    if (temp >= 10 && temp <= 25) {
      dp[i] = dp[i - 1] + dp[i - 2]
    } else {
      dp[i] = dp[i - 1]
    }
  }
  return dp[n] // 翻译前n个数的方法数，翻译整个数字
}
```

执行用时 :72 ms, 在所有 JavaScript 提交中击败了32.11%的用户

内存消耗 :32.4 MB, 在所有 JavaScript 提交中击败了100.00%的用户

###### 降维 / 压缩空间

当前 dp 项只和它前面的两项有关，我们无需用数组存储所有的 dp 项

用两个变量去存dp 项前面的两项，在遍历中不断更新这两个变量，可将空间复杂度优化到 O(1)

```js
const translateNum = (num) => {
  const str = num.toString()
  const n = str.length
  let prev = 1
  let cur = 1
  for (let i = 2; i < n + 1; i++) {
    const temp = Number(str[i - 2] + str[i - 1])
    if (temp >= 10 && temp <= 25) {
      const t = cur // 缓存上个状态
      cur = prev + cur // 当前状态=上上个状态+上个状态
      prev = t // 更新上上个状态
    } else {
      // cur = cur
      prev = cur // 这里容易忘了
    }
  }
  return cur
}
```

执行用时 :68 ms, 在所有 JavaScript 提交中击败了50.99%的用户

内存消耗 :32.3 MB, 在所有 JavaScript 提交中击败了100.00%的用户






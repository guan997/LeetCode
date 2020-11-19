### 剑指OFFER

[面试题 02.01. 移除重复节点](#面试题02.01.移除重复节点)

[面试题03. 数组中重复的数字](#面试题03. 数组中重复的数字)

[剑指 Offer 04. 二维数组中的查找](#剑指 Offer 04. 二维数组中的查找)

[面试题05. 替换空格](#面试题05. 替换空格)

[面试题06. 从尾到头打印链表](#面试题06. 从尾到头打印链表)

[剑指Offer07. 重建二叉树](#剑指Offer07. 重建二叉树)

[面试题 08.03. 魔术索](#面试题 08.03. 魔术索)

[面试题 08.06. 汉诺塔问题](#面试题 08.06. 汉诺塔问题)

[面试题10- I. 斐波那契数列](#面试题10- I. 斐波那契数列)

[面试题10- II. 青蛙跳台阶问题](#面试题10- II. 青蛙跳台阶问题)

[剑指 Offer 11. 旋转数组的最小数字](#剑指 Offer 11. 旋转数组的最小数字)

[剑指 Offer 14- I. 剪绳子](#剑指 Offer 14- I. 剪绳子)

[面试题 16.11. 跳水板](#面试题 16.11. 跳水板)

[面试题17. 打印从1到最大的n位数](#面试题17. 打印从1到最大的n位数)

[剑指 Offer 18. 删除链表的节点](#剑指 Offer 18. 删除链表的节点)

[剑指 Offer 22.链表中倒数第k个节点](#剑指Offer 22.链表中倒数第k个节点)

[剑指 Offer 24. 反转链表](#剑指 Offer 24. 反转链表)

[剑指 Offer 25. 合并两个排序的链表](#剑指 Offer 25. 合并两个排序的链表)

[剑指 Offer 27. 二叉树的镜像](#剑指 Offer 27. 二叉树的镜像)

[剑指 Offer 28. 对称的二叉树](#剑指 Offer 28. 对称的二叉树)

[面试题29. 顺时针打印矩阵](#面试题29. 顺时针打印矩阵)

[剑指Offer 30.包含min函数的栈](#剑指Offer 30.包含min函数的栈)

[剑指 Offer 32 - I. 从上到下打印二叉树](#剑指 Offer 32 - I. 从上到下打印二叉树)

[剑指 Offer 32 - III. 从上到下打印二叉树 III](#剑指 Offer 32 - III. 从上到下打印二叉树 III)

[剑指 Offer 34. 二叉树中和为某一值的路径](#剑指 Offer 34. 二叉树中和为某一值的路径)

[面试题46. 把数字翻译成字符串](#面试题46. 把数字翻译成字符串)

[剑指 Offer 50. 第一个只出现一次的字符](#剑指 Offer 50. 第一个只出现一次的字符)

[剑指Offer 52. 两个链表的第一个公共节点](#剑指Offer 52. 两个链表的第一个公共节点)

[剑指 Offer 53 - I. 在排序数组中查找数字 I](#剑指 Offer 53 - I. 在排序数组中查找数字 I)

[剑指 Offer 53 - II. 0～n-1中缺失的数字](#剑指 Offer 53 - II. 0～n-1中缺失的数字)

[剑指 Offer 54. 二叉搜索树的第k大节点](#剑指 Offer 54. 二叉搜索树的第k大节点)

[剑指 Offer 55 - I. 二叉树的深度](#剑指 Offer 55 - I. 二叉树的深度)

[剑指 Offer 55 - II. 平衡二叉树](#剑指 Offer 55 - II. 平衡二叉树)

[剑指 Offer 56 - I. 数组中数字出现的次数](#剑指 Offer 56 - I. 数组中数字出现的次数)

[剑指 Offer 56 - II. 数组中数字出现的次数 II](#剑指 Offer 56 - II. 数组中数字出现的次数 II)

[剑指 Offer 57. 和为s的两个数字](#剑指 Offer 57. 和为s的两个数字)

[剑指 Offer 58 - I. 翻转单词顺序](#剑指 Offer 58 - I. 翻转单词顺序)

[剑指Offer 58 - II.左旋转字符串](#剑指Offer 58 - II.左旋转字符串)

[剑指 Offer 59 - I. 滑动窗口的最大值](#剑指 Offer 59 - I. 滑动窗口的最大值)

[面试题64. 求1+2+…+n](#面试题64. 求1+2+…+n)

[剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](#剑指 Offer 68 - I. 二叉搜索树的最近公共祖先)

#### 面试题02.01.移除重复节点

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

#### 面试题03.数组中重复的数字

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

#### 剑指 Offer 04. 二维数组中的查找

难度简单

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。

###### 线性查找

- 从右上角 往左下找
- 横纵都是递增的, 所以从矩阵的 右上角 往 左下查找
- 当前比目标大, 如果目标存在, 只能在左下边, 此时范围缩小一列
- 当前比目标小, 目标存在的话, 只能在下边, 当前行不存在目标值, 此时范围缩小一行

```js
var findNumberIn2DArray = function(matrix, target) {
  let rows = matrix.length
  if(!rows) return false
  let columns = matrix[0].length
  let row = 0, column = columns - 1
  while (row < rows && column>= 0) {  // 从右上角 往左下找
    let t = matrix[row][column]
    if (t === target) {
      return true
    } else if (t > target) { // 大于目标, 说明在左/下边
      column--
    } else {                 // 小于目标, 说明在下边
      row++
    }
  }
  return false
};
```

时间复杂度：O(n+m)

###### 内置函数

- flat()方法创建一个新数组，其中所有子数组元素都以递归方式连接到该数组中，直到达到指定的深度。

- includes()方法确定数组在其条目中是否包含某个值，是返回值true还是false适当值。

```js
var findNumberIn2DArray = function(matrix, target) {
    return matrix.flat(Infinity).includes(target);
};
```

执行用时：116 ms, 在所有 JavaScript 提交中击败了5.53%的用户

内存消耗：43.3 MB, 在所有 JavaScript 提交中击败了5.80%的用户

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

#### 剑指Offer07. 重建二叉树

难度中等

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出

```
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
```

返回如下的二叉树：

```
    3
   / \
  9  20
    /  \
   15   7
```

注意：本题与主站 105 题重复

###### 递归

- 获取根节点区分左右子树，对于左子树的前序和中序采取同样的操作。

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function (preorder, inorder) {
    if (!preorder.length || !inorder.length) return null
    let root = preorder[0]; // 前序遍历的第一个元素为根节点
    let node = new TreeNode(root); // 确定根节点

    let i = inorder.indexOf(root); // 获取根节点在中序遍历中的位置(用于分割左右子树)

    // 递归
    node.left = buildTree(preorder.slice(1, i + 1), inorder.slice(0, i));
    node.right = buildTree(preorder.slice(i + 1), inorder.slice(i + 1));
    return node
};
```

#### 面试题 08.03. 魔术索

难度简单

魔术索引。 在数组`A[0...n-1]`中，有所谓的魔术索引，满足条件`A[i] = i`。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。

**示例1:**

```
 输入：nums = [0, 2, 3, 4, 5]
 输出：0
 说明: 0下标的元素为0
```

**示例2:**

```
 输入：nums = [1, 1, 1]
 输出：1
```

###### 数组遍历

```js
const findMagicIndex = (nums) => {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] == i) return i;
  }
  return -1;
};
```



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

#### 剑指 Offer 14- I. 剪绳子

难度中等

给你一根长度为 `n` 的绳子，请把绳子剪成整数长度的 `m` 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 `k[0],k[1]...k[m-1]` 。请问 `k[0]*k[1]*...*k[m-1]` 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

###### 动态规划

- dp[i] 表示正整数 i 拆分成的整数的最大乘积
- 前面的代码中的正整数 n 变成了这里的正整数 i，用指针 j 去划分 i，分成了 j 和 i - j。
- 遍历所有的 j，i−j 可以选择拆或者不拆，不拆就是 i-ji−j ，拆就是 dp[i - j]，其实就是对 i - j 调用的结果（子问题的解）。

```js
const integerBreak = (n) => {
  const dp = new Array(n + 1);
  dp[1] = 1;  
  dp[2] = 1; 
  for (let i = 3; i <= n; i++) {
    dp[i] = 0;
    // 对于数字 i，它可以分为两份：j 和 i-j，j 的范围是 1 到 i-j
    for (let j = 1; j <= i - j; j++) {
      // 对于 i-j 这部分可以拆或不拆，不拆就是 i-j，拆就是 dp[i-j]
      dp[i] = Math.max(dp[i], j * (i - j), j * dp[i - j]);
    }
  }
  return dp[n];
};
```

- 空间复杂度是 O(N)

- 时间复杂度是 O(N^2)

#### 剑指Offer 15.二进制中1的个数

难度简单

请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

###### 循环和位移动

- 遍历数字的 32 位。如果某一位是 11 ，将计数器加一

```js
var hammingWeight = function(n) {
    var bits = 0
    var mask = 1
    for(var i = 0; i < 32; i++){
        if((n & mask) != 0){
            bits++
        }
        mask <<= 1
    }
    return bits
};
```

时间复杂度：O(1)

空间复杂度：O(1)

###### 位操作的小技巧

- 不断把数字最后一个 11 反转，并把答案加一。当数字变成 00 的时候偶，我们就知道它没有 11 的位了，此时返回答案。

```js
var hammingWeight = function(n) {
    var sum = 0
    while(n != 0){
        sum++
        n &= (n - 1)
    }
    return sum
};
```

时间复杂度：O(1)

空间复杂度：O(1)

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

#### 剑指 Offer 24. 反转链表

难度简单50

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

**示例:**

```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

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

#### 剑指 Offer 25. 合并两个排序的链表

难度简单

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

###### 递归

- 如果 l1 或者 l2 一开始就是空链表 ，那么没有任何操作需要合并，所以我们只需要返回非空链表。否则，我们要判断 l1 和 l2 哪一个链表的头节点的值更小，然后递归地决定下一个添加到结果里的节点。如果两个链表有一个为空，递归结束。

```js
var mergeTwoLists = function(l1, l2) {
    if (l1 === null) {
        return l2;
    } else if (l2 === null) {
        return l1;
    } else if (l1.val < l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
};
```

- 时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。因为每次调用递归都会去掉 l1 或者 l2 的头节点（直到至少有一个链表为空），函数 mergeTwoList 至多只会递归调用每个节点一次。因此，时间复杂度取决于合并后的链表长度，即 O(n+m)。
- 空间复杂度：O(n + m)，其中 n 和 m分别为两个链表的长度。递归调用 mergeTwoLists 函数时需要消耗栈空间，栈空间的大小取决于递归调用的深度。结束递归调用时 mergeTwoLists 函数最多调用 n+m 次，因此空间复杂度为 O(n+m)。

###### 迭代

思想

- 当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位。

算法

- 首先，我们设定一个哨兵节点 prehead ，这可以在最后让我们比较容易地返回合并后的链表。我们维护一个 prev 指针，我们需要做的是调整它的 next 指针。然后，我们重复以下过程，直到 l1 或者 l2 指向了 null ：如果 l1 当前节点的值小于等于 l2 ，我们就把 l1 当前的节点接在 prev 节点的后面同时将 l1 指针往后移一位。否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都需要把 prev 向后移一位。

在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，所以不管哪个链表是非空的，它包含的所有元素都比前面已经合并链表中的所有元素都要大。这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表即可。

```js
var mergeTwoLists = function(l1, l2) {
    const prehead = new ListNode(-1);

    let prev = prehead;
    while (l1 != null && l2 != null) {
        if (l1.val <= l2.val) {
            prev.next = l1;
            l1 = l1.next;
        } else {
            prev.next = l2;
            l2 = l2.next;
        }
        prev = prev.next;
    }

    // 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
    prev.next = l1 === null ? l2 : l1;

    return prehead.next;
};
```

- 时间复杂度：O(n + m) ，其中 n 和 m 分别为两个链表的长度。因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中， 因此 while 循环的次数不会超过两个链表的长度之和。所有其他操作的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)。
- 空间复杂度：O(1) 。我们只需要常数的空间存放若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）

#### 剑指 Offer 27. 二叉树的镜像

难度简单

请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

`   4  /  \ 2   7 / \  / \1  3 6  9`
镜像输出：

```
   4  /  \ 7   2 / \  / \9  6 3  1
```

**示例 1：**

```
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
```

限制：

0 <= 节点个数 <= 1000

注意：本题与主站 226 题相同：https://leetcode-cn.com/problems/invert-binary-tree/

###### 递归

- 时间复杂度：O(n)
- 空间复杂度：O(n)
- 递归交换当前节点的左右节点，当节点为null时返回

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
 * @return {TreeNode}
 */
var mirrorTree = function(root) {
    if(!root) return null
    const left = mirrorTree(root.left)
    const right = mirrorTree(root.right)
    root.left = right
    root.right = left
    return root
};
```

#### 剑指 Offer 28. 对称的二叉树

难度简单

请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

`  1  / \ 2  2 / \ / \3  4 4  3`
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

```
  1  / \ 2  2  \  \  3   3
```

**示例 1：**

```
输入：root = [1,2,2,3,4,4,3]
输出：true
```

**示例 2：**

```
输入：root = [1,2,2,null,3,null,3]
输出：false
```

###### 递归

- 类似于一张白纸对折的原理

```js
var isSymmetric = function(root) {
    function isMirror(r1,r2){
        //如果都为null 对称
        if(!r1 && !r2){
            return true
        }
        //只要其中一个为空，另一个不为，则不对称
        if(!r1 || !r2){
            return false
        }
        //判断根节点
        //判断r1的左树和r2的右
        //判断r2的左树和r1的右
        return r1.val == r2.val && isMirror(r1.left,r2.right) && isMirror(r1.right,r2.left)
    }
    return isMirror(root,root)
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

#### 剑指Offer 30.包含min函数的栈

难度简单

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

###### 辅助栈

- 当一个元素要入栈时，我们取当前辅助栈的栈顶存储的最小值，与当前元素比较得出最小值，将这个最小值插入辅助栈中；
- 当一个元素要出栈时，我们把辅助栈的栈顶元素也一并弹出；
- 在任意一个时刻，栈内元素的最小值就存储在辅助栈的栈顶元素中。

```js
var MinStack = function() {
    this.x_stack = [];
    this.min_stack = [Infinity];
};

MinStack.prototype.push = function(x) {
    this.x_stack.push(x);
    this.min_stack.push(Math.min(this.min_stack[this.min_stack.length - 1], x));
};

MinStack.prototype.pop = function() {
    this.x_stack.pop();
    this.min_stack.pop();
};

MinStack.prototype.top = function() {
    return this.x_stack[this.x_stack.length - 1];
};

MinStack.prototype.getMin = function() {
    return this.min_stack[this.min_stack.length - 1];
};
```

- 时间复杂度：O(1）

- 空间复杂度：O(n)

###### 同步双栈 即两个数组的长度永远保持一致

```js
var arr = [], sortArr = [];

var MinStack = function() {
    arr = [];
    sortArr = [];
};

//将元素 x 推入栈中
MinStack.prototype.push = function(x) {
    arr.push(x);
    if(!sortArr.length){
        sortArr.push(x);
    }else{
        sortArr.push(x < sortArr[sortArr.length - 1] ? x : sortArr[sortArr.length - 1]);
    }
};

//删除栈顶的元素
MinStack.prototype.pop = function() {
    arr.pop();
    sortArr.pop();
};

//获取栈顶元素
MinStack.prototype.top = function() {
    return arr[arr.length - 1];
};

//检索栈中的最小元素
MinStack.prototype.getMin = function() {
    return sortArr[sortArr.length - 1];
};
```

###### 非同步双栈

```js
var arr = [], sortArr = [];

var MinStack = function() {
    arr = [];
    sortArr = [];
};

//将元素 x 推入栈中
MinStack.prototype.push = function(x) {
    arr.push(x);
    if(!sortArr.length || x <= sortArr[sortArr.length - 1]){
        sortArr.push(x);
    }
};

//删除栈顶的元素
MinStack.prototype.pop = function() {
    if(arr.pop() == sortArr[sortArr.length - 1]){
        sortArr.pop();
    }
};

//获取栈顶元素
MinStack.prototype.top = function() {
    return arr[arr.length - 1];
};

//检索栈中的最小元素
MinStack.prototype.getMin = function() {
    return sortArr[sortArr.length - 1];
};
```

#### 剑指 Offer 32 - I. 从上到下打印二叉树

难度中等

从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回：

```
[3,9,20,15,7]
```

###### 队列

- 利用队列的数据结构，将根节点先保存在队列中，左子树或右子树不为空时，队列中加入该节点
- 另外使用一个数组res，保存队列先进先出的值
- 时间复杂度为O(N),空间复杂度为O(N)

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
 * @return {number[]}
 */
var levelOrder = function(root) {
   if(!root) return [];
   const queue=[root];
    let res=[];
   while(queue.length){
       let t=queue.shift();
       res.push(t.val);
       if(t.left) queue.push(t.left);
       if(t.right) queue.push(t.right);
   }
   return res;
};
```

#### 剑指 Offer 32 - III. 从上到下打印二叉树 III

难度中等

请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

例如:
给定二叉树: `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

返回其层次遍历结果：

```
[
  [3],
  [20,9],
  [15,7]
]
```

###### BFS深度遍历

- level: 当前层级;
- ltor: 当前是否from left to right

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
    const res = [];

    function dfs(root, level, ltor) {
        if (!root) return;
        res[level] = res[level] || [];

        if (ltor) {
            res[level].push(root.val);
        } else {
            res[level].unshift(root.val);
        }

        dfs(root.left, level + 1, !ltor);
        dfs(root.right, level + 1, !ltor);
    }

    dfs(root, 0, true);
    return res;
};
```

#### 剑指 Offer 34. 二叉树中和为某一值的路径

难度中等

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

**示例:**
给定如下二叉树，以及目标和 `sum = 22`，

```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```

返回:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

 

**提示：**

1. `节点总数 <= 10000`

注意：本题与主站 113 题相同：https://leetcode-cn.com/problems/path-sum-ii/

###### 先序遍历+回溯

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
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    var path=[], //保存路径
        res=[];  //保存路经的数组
    /*辅助函数---增加参数列表，用来实现对res,path的引用值的传递，因为res，path为数组，是对象范畴
      本题目中需要根据条件，回溯更新路径path直到符合条件.
    */
    var resuc = function (root, sum, res, path) {
        if (root) {                    
            //单个节点要做的事
            path.push(root.val);
            if (!root.left && !root.right && sum-root.val == 0) {
                res.push([...path]);
            }

            //左右子节点递归调用
            resuc(root.left, sum - root.val,res, path);
            resuc(root.right, sum - root.val, res, path);
            path.pop();   //回溯先序遍历一条路径结束，不符合条件时，将最后一个数弹出如5,4,4,7-->5,4,4,-2。
        }
        return res;
    }
    return resuc(root, sum, res, path); 
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

#### 剑指 Offer 50. 第一个只出现一次的字符

难度简单

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

###### map两次遍历

遍历字符串，将每个字符的值与出现次数记录到 map 中
再次遍历 map.keys() ，获取 map 中每个字符出现的次数，判断是否仅仅只有 1 次，返回第一个仅出现一次的字符

```js
var firstUniqChar = function(s) {
    if(!s) return " "
    let map = new Map()
    for(let c of s) {
        if(map.has(c)) {
            map.set(c, map.get(c) + 1)
        } else {
            map.set(c, 1)
        }
    }
    for(let c of map.keys()) {
        if(map.get(c) === 1) {
            return c
        }
    }

    return  " "
};
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)

#### 剑指 Offer 51. 数组中的逆序对

难度困难

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

######  暴力法（TLE）

双重循环，挨个检查是否为逆序对。

```js
/**
 * @param {number[]} nums
 * @return {number}
 */
var reversePairs = function(nums) {
    let res = 0;
    const length = nums.length;
    for (let i = 0; i < length; ++i) {
        for (let j = i + 1; j < length; ++j) {
            nums[i] > nums[j] && ++res;
        }
    }

    return res;
};
```

 * 时间复杂度是O(N^2)，无法通过

###### 归并排序

- 递归调用，拿到左子数组和右子数组的逆序对（此时，左子数组和右子数组也都排序完成了）
- 指针 i 和 j 分别指向左子数组和右子数组的最右侧，此时会有 2 种情况：
  - arr[i] > arr[j]：那么说明arr[i]大于右子数组中所有元素，逆序对增加j - start - length，向左边移动指针 i
  - arr[i] <= arr[j]: 对arr[i]来说，不存在逆序对，向左边移动指针 j
- i 和 j 遍历完各自数组后，最后返回逆序对之和

```js
var reversePairs = function(nums) {
    return findInversePairNum(nums, 0, nums.length - 1);
};

function findInversePairNum(arr, start, end) {
    if (start >= end) return 0;

    const copy = new Array(end - start + 1);
    const length = Math.floor((end - start) / 2); // 左数组长度
    const leftNum = findInversePairNum(arr, start, start + length);
    const rightNum = findInversePairNum(arr, start + length + 1, end);

    let i = start + length;
    let j = end;
    let copyIndex = end - start;
    let num = 0;
    while (i >= start && j >= start + length + 1) {
        if (arr[i] > arr[j]) {
            num += j - start - length;
            copy[copyIndex--] = arr[i--];
        } else {
            copy[copyIndex--] = arr[j--];
        }
    }

    while (i >= start) {
        copy[copyIndex--] = arr[i--];
    }

    while (j >= start + length + 1) {
        copy[copyIndex--] = arr[j--];
    }

    for (let k = start; k <= end; ++k) {
        arr[k] = copy[k - start];
    }

    return num + leftNum + rightNum;
}
```

- 时间复杂度是O(NlogN)
- 空间复杂度是O(N)

#### 剑指Offer 52. 两个链表的第一个公共节点

难度简单

输入两个链表，找出它们的第一个公共节点。

如下面的两个链表**：**

[![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

在节点 c1 开始相交。

###### 双指针

解题思路：

尝试消除 A、B 链表的长度差，同步遍历链表节点，判断是否有相同节点，若有相同则是两链表相交，返回第一个相同节点 即可。否则返回 null ，两链表不相交。

```js
var getIntersectionNode = function(headA, headB) {
    let headNodeA = headA,headNodeB = headB;

    while(headNodeA || headNodeB) {
        if(headNodeA === headNodeB) return headNodeA
        headNodeA = headNodeA === null ? headB : headNodeA.next
        headNodeB = headNodeB === null ? headA : headNodeB.next
    }
    return null
};
```

- 时间复杂度：O(N)。
- 空间复杂度：O(1)。

#### 剑指 Offer 53 - I. 在排序数组中查找数字 I

难度简单

统计一个数字在排序数组中出现的次数。

**示例 1:**

```
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
```

**示例 2:**

```
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
```

######  二分查找

- 二分查找到等于当前值的索引，把索引赋值给 left，或者直到左指针大于等于右指针停下
- 判断 nums[left] 是否等于 target，不等，返回 0
- 从 left 指针的位置往两边找，看看这个数重复几次，返回

```js
var search = function(nums, target) {
  let count = 0,
      n = nums.length,
      left = 0,
      right = n - 1;
  
  while (left < right) {
    let mid = (left + right) >> 1;
    if (nums[mid] === target) {
      left = mid;
      break;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  
  if (nums[left] !== target) return 0;
  
  // 找到起始位置, 从当前位置往两边找，看看重复几次
  let copy = left - 1;
  while (copy >= 0 && nums[copy] === target) {
    copy--;
    count++;
  }
  
  while (nums[left] === target && left < n) {
    left++;
    count++;
  }
  
  return count;
};
```

#### 剑指 Offer 53 - II. 0～n-1中缺失的数字

难度简单

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

**示例 1:**

```
输入: [0,1,3]
输出: 2
```

**示例 2:**

```
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
```

###### 二分查找

- left 指向 0，right 指向最后一个元素
- 计算中间坐标 mid：
  - 如果mid = nums[mid]，说明[0, mid]范围内不缺失数字，left 更新为 mid + 1
  - 如果mid < nums[mid]，说明[mid, right]范围内不缺失数字，right 更新为 mid - 1
- 检查 left 是否小于等于 mid，若成立，返回第 2 步；否则，向下执行

- 返回 left 即可

根据题意，可以知道mid > nums[mid]这种情况不存在。

```js
var missingNumber = function(nums) {
    let left = 0,
        right = nums.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (mid === nums[mid]) {
            left = mid + 1;
        } else if (mid < nums[mid]) {
            right = mid - 1;
        }
    }

    return left;
};
```

#### 剑指 Offer 54. 二叉搜索树的第k大节点

难度简单

给定一棵二叉搜索树，请找出其中第k大的节点。

**示例 1:**

```
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4
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
输出: 4
```

######  递归

- 最终返回的倒数第k个元素就是arr.length-1-k+1 ，即以arr.length-k为下标的元素

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
 * @param {number} k
 * @return {number}
 */
var kthLargest = function(root, k) {
    let arr = []
    function traversal(node) {
        if(!node) return
        traversal(node.left)
        arr.push(node.val)
        traversal(node.right)
    }
    traversal(root)
    return arr[arr.length - k]
};
```

#### 剑指 Offer 55 - I. 二叉树的深度

难度简单

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 `[3,9,20,null,null,15,7]`，

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。

**提示：**

1. `节点总数 <= 10000`

注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

###### 递归

```js
var maxDepth = function(root) {
    if(!root){
        return 0
    }
    return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1
};
```

#### 剑指 Offer 55 - II. 平衡二叉树

难度简单

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

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

###### 自顶向下的递归

类似于二叉树的前序遍历，即对于当前遍历到的节点，首先计算左右子树的高度，如果左右子树的高度差是否不超过 1，再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。这是一个自顶向下的递归的过程。

```js
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

时间复杂度：O(n ^ 2)

空间复杂度：O(n)

###### 方法二：自底向上的递归

自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 -1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。

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
 * @return {boolean}
 */
var isBalanced = function(root) {
    return height(root) >= 0

    function height(root){
        if(root == null){
            return 0
        }
        let leftHeight = height(root.left)
        let rightHeight = height(root.right)
        if(leftHeight == -1 || rightHeight == -1 || Math.abs(leftHeight - rightHeight) > 1){
            return -1
        }else{
            return Math.max(leftHeight,rightHeight) + 1
        }
    }
};
```

#### 剑指 Offer 56 - I. 数组中数字出现的次数

难度中等

一个整型数组 `nums` 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

**示例 1：**

```
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
```

**示例 2：**

```
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
```

###### 位运算

```js
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumbers = function(nums) {
  // 定义一个 mask，表示要找的两个数字的异或
  // 因为出现了两次的数字的异或为 0，也就不会被记录在 mask 中
  let mask = 0
  for (let num of nums) {
    mask ^= num
  }
  // 获取到 mask 后，此时的任务就是找到其中一个只出现过一次的数字，记为 num1
  // 将 mask 与 num1 进行异或计算，就能获得第二个数字，记为 num2

  // 异或结果的某一位是 1，表示当前位的运算数字一个是 1 ，一个是 0
  // 即找到了不同的一位，以下取最低位的 1

  // 获取最低位的 1，记为 diff
  const diff = mask & -mask
  let num1 = 0
  for (let num of nums) {
    // 若 num 与 diff 的与运算结果为 1，则说明这些 num 是一组的
    // 与此同时，结果为 0 的表示另外一组
    // 原因是：异或为 1，表示运算数分别是 0 / 1
    if (num & diff) {
      // 此时的过程就相当于 在一堆数字(除了一个数字外其它成对)中找个唯一的一个
      num1 ^= num
    }
  }
  // 此时 num1 就是其中一个只出现一次的数字

  // 将 num1 与 mask 异或，得到另外一个
  const num2 = mask ^ num1
  return [num1, num2]
};
```

#### 剑指 Offer 56 - II. 数组中数字出现的次数 II

难度中等

在一个数组 `nums` 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

##### 异或

异或的性质

- 两个数字异或的结果a^b是将 a 和 b 的二进制每一位进行运算，得出的数字。 运算的逻辑是
  如果同一位的数字相同则为 0，不同则为 1

异或的规律

- 任何数和本身异或则为0
- 任何数和 0 异或是本身

###### 位运算

不开辟额外空间

```js
var singleNumber = function(nums) {
  let res = 0;
  for (let i = 0; i < 32; i++) {
    let cnt = 0;
    let bit = 1 << i;
    for (let j = 0; j < nums.length; j++) {
      if (nums[j] & bit) cnt++;
    }
    if (cnt % 3 != 0) res = res | bit;
  }
  return res;
};
```

- 时间复杂度是O(N)

- 空间复杂度是O(1)

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

#### 剑指 Offer 55 - II. 平衡二叉树

难度简单

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

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
 * @return {boolean}
 */
var isBalanced = function(root) {
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

#### 剑指 Offer 57 - II. 和为s的连续正数序列

难度简单

输入一个正整数 `target` ，输出所有和为 `target` 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

**示例 1：**

```
输入：target = 9
输出：[[2,3,4],[4,5]]
```

**示例 2：**

```
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
```

######  滑动窗口

- **窗口的左边界和右边界永远只能向右移动**

- 当窗口的和小于 target 的时候，窗口的和需要增加，所以要扩大窗口，窗口的右边界向右移动

- 当窗口的和大于 target 的时候，窗口的和需要减少，所以要缩小窗口，窗口的左边界向右移动

- 当窗口的和恰好等于 target 的时候，我们需要记录此时的结果。设此时的窗口为 [i, j)，那么我们已经找到了一个 i开头的序列，也是唯一一个 i 开头的序列，接下来需要找 i+1 开头的序列，所以窗口的左边界要向右移动

  ```js
var findContinuousSequence = function(target) {
    var i = 1;//滑动窗口的左边界
    var j = 1;//滑动窗口的有边界
    var sum = 0;//滑动窗口中数字的和
    var res = [];
    while(i <= target / 2){
        if(sum < target){
            // 右边界向右移动
            sum += j;
            j++;
        }else if(sum > target){
            // 左边界向右移动
            sum -= i;
            i ++;
        }else{
            // 记录结果
            var arr = [];
            for(var k = i; k < j; k++){
                arr.push(k);
            }
            res.push(arr);
            // 左边界向右移动
            sum -= i;
            i++;
        }
    }
    return res;
};
  ```

- 时间复杂度是 O(n)
- 空间复杂度是 O(n)

#### 剑指 Offer 58 - I. 翻转单词顺序

难度简单

输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

###### 双指针

- 倒序遍历字符串 s，去掉头尾空格，记录单词左右索引边界 i , j ；
- 每确定一个单词的边界，则将其添加至单词列表 res；
- 最后，将单词列表拼接为字符串，并返回即可。

```js
/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.trim()
    var j = s.length - 1, i = j
    var res = []
    while(i >= 0){
        while(i >= 0 & s[i] != ' '){i -= 1} //搜索首个空格
        res.push(s.slice(i + 1, j + 1)) //添加单词
        while(s[i] == ' '){i -= 1} //跳过单词间空格
        j = i //j 指向下个单词的尾字符
    }
    return res.join(' ')
};
```

- 时间复杂度 O(N)
- 空间复杂度 O(N)

###### 内置函数

- trim()把字符串两端空格去掉
- split(' ')把字符串切割成以空格为界限的单词块
- filter()过滤掉数组中的纯空格
- reverse()进行数组反转
- join(' ')把数组变成中间只带一个空格的字符串

```js
var reverseWords = function(s) {
  let t = s.trim().split(' ').filter(el => el);
  return t.reverse().join(' ');
};
```

- 时间复杂度 O(N)
- 空间复杂度 O(N)

#### 剑指Offer 58 - II.左旋转字符串

难度简单

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

######  字符串切片

-  切片，使用 "++" 运算符拼接
  - slice(start, end) end省略时代表到尾部
    substring(start, end)提取一个字符串,end不支持负数
    substr(start, len)提取一个长度为len的字符串

```js
var reverseLeftWords = function(s, n) {
    return s.slice(n) + s.slice(0, n)
    //return s.substring(n) + s.substring(n, 0);
    //return s.substr(n,s.length-n+1) + s.substr(0, n);
};
```

###### 列表遍历拼接

- 新建一个[]，记为 res ；
- 先向 res添加 “第 n + 1位至末位的字符” ；
- 再向 res 添加 “首位至第 n位的字符” ；
- 将 res转化为字符串并返回。

```js
var reverseLeftWords = function(s, n) {
    var res = []
    for(var i = n; i < s.length; i++){
        res.push(s[i])
    }
    for(var i = 0; i < n; i++){
        res.push(s[i])
    }
    return res.join('')
}
```

利用求余运算，简化代码

```js
var reverseLeftWords = function(s, n) {
    var res = []
    for(var i = n; i < n + s.length; i++){
        res.push(s[i % s.length])
    }
    return res.join('')
}
```

###### 字符串遍历拼接

```js
var reverseLeftWords = function(s, n) {
    var res = ""
    for(var i = n; i < s.length; i++){
        res += s[i]
    }
    for(var i = 0; i < n; i++){
        res += s[i]
    }
    return res
};
```

同理，利用求余运算，简化代码

```js
var reverseLeftWords = function(s, n) {
    var res = ""
    for(var i = n; i < n + s.length; i++){
        res += s[i % s.length]
    }
    return res
};
```

#### 剑指 Offer 59 - I. 滑动窗口的最大值

难度简单

给定一个数组 `nums` 和滑动窗口的大小 `k`，请找出所有滑动窗口里的最大值。

**示例:**

```
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```



#### 剑指 Offer 64. 求1+2+…+n

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

#### 剑指 Offer 68 - I. 二叉搜索树的最近公共祖先

难度简单

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

[百度百科](https://baike.baidu.com/item/最近公共祖先/8918834?fr=aladdin)中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（**一个节点也可以是它自己的祖先**）。”

例如，给定如下二叉搜索树: root = [6,2,8,0,4,7,9,null,null,3,5]

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png)

 

**示例 1:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
```

**示例 2:**

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```

**说明:**

- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉搜索树中。

注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

###### 递归

- 既然是BST，如果p和q都比root.val小，则递归左子树，如果都比root.val大，则递归右子树，否则，root 即为所求
- 因为 root 为 p,q 的最近公共祖先，只可能是下面的情况
  - p,q 分居root的两个子树
  - p 为 root ，q 在root的左或右子树中
  - q 为 root ， p 在root 的左或右子树中

```js
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
const lowestCommonAncestor = (root, p, q) => {
  if (p.val < root.val && q.val < root.val) {
    return lowestCommonAncestor(root.left, p, q);
  }
  if (p.val > root.val && q.val > root.val) {
    return lowestCommonAncestor(root.right, p, q);
  }
  return root;
};
```


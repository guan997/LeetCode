## 递归

#### [70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

难度简单1261收藏分享切换为英文接收动态反馈

假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**注意：**给定 *n* 是一个正整数。

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

- 时间复杂度：O(n)
- 空间 复杂度：O(1)

#### [509. 斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)

难度简单

**斐波那契数**，通常用 `F(n)` 表示，形成的序列称为**斐波那契数列**。该数列由 `0` 和 `1` 开始，后面的每一项数字都是前面两项数字的和。也就是：

```
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
```

给定 `N`，计算 `F(N)`。

###### 暴力递归

```js
var fib = function(N) {
    if( N < 1) return 0;
    if( N <= 2) return 1;
    if( N >=3 ){
        return fib(N-1)+fib(N-2);
    }
};
```

- 时间复杂度：O(n^2),需要指数的时间。
- 空间复杂度：O(n)

###### 备忘录递归

- “备忘录”储存，"剪枝"处理技巧，去除重复的调用计算

```js
function fib(n) {
    if (n === 0) {
        return 0;
    }
    const sumMap = {};
    if (n === 1 || n === 2) {
        return 1;
    }
    if (sumMap[n]) {
        return sumMap[n];
    }
    const rst = fib(n-2) + fib(n-1);
    sumMap[n] = rst;
    return rst;
}
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)
## 二分查找

#### [69. x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

难度简单

实现 `int sqrt(int x)` 函数。

计算并返回 *x* 的平方根，其中 *x* 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

###### 二分查找

```js
var mySqrt = function(x) {
    if (x < 2) return x
    let left = 1, mid, right = Math.floor(x / 2);
    while (left <= right) {
        mid = Math.floor(left + (right - left) / 2)
        if (mid * mid === x) return mid
        if (mid * mid < x) {
            left = mid + 1
        }else {
            right = mid - 1
        }
    }
    return right
};
```

- 时间复杂度：O(logx)
- 空间复杂度：O(1)
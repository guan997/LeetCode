## 字符串

## [344. 反转字符串](https://leetcode-cn.com/problems/reverse-string/)

难度简单

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `char[]` 的形式给出。

不要给另外的数组分配额外的空间，你必须**[原地](https://baike.baidu.com/item/原地算法)修改输入数组**、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 [ASCII](https://baike.baidu.com/item/ASCII) 码表中的可打印字符。

#### 双指针

- 将 left 指向字符数组首元素，right 指向字符数组尾元素。

- 当 left < right：

  - 交换 s[left] 和 s[right]；
  - left 指针右移一位，即 left = left + 1；
  - right 指针左移一位，即 right = right - 1。
- 当 left >= right，反转结束，返回字符数组即可

```js
var reverseString = function(s) {
    const n = s.length;
    for (let left = 0, right = n - 1; left < right; ++left, --right) {
        [s[left], s[right]] = [s[right], s[left]];
    }
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

#### 双指针 + 解构赋值

- 从`队头`和`队尾`向中间逼近，用`解构赋值`交换值

```js
var reverseString = function(s) {
    let x = 0, y = s.length - 1;
    while(x < y){
        [s[x], s[y]] = [s[y], s[x]];
        x++,y--;
    }
    return s;
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)
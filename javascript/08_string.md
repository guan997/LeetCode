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
        //等号的左边和右边相等。
        [s[x], s[y]] = [s[y], s[x]];
        x++,y--;
    }
    return s;
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

## [151. 翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)

难度中等

给定一个字符串，逐个翻转字符串中的每个单词。

**说明：**

- 无空格字符构成一个 **单词** 。
- 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
- 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

#### 正则 + JS API

- 使用 `split` 把一个字符串分割成字符串数组。
- 使用`trim`去除首尾空格
- 使用 `reverse` 将字符串数组进行反转；
- 使用 `join` 方法将字符串数组拼成一个字符串。

```js
var reverseWords = function(s) {
    return s.trim().split(/\s+/).reverse().join(' ');
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(N)

##### 双端队列

- 首先去除字符串左右空格
- 逐个读取字符串中的每个单词，依次放入双端队列的对头
- 再将队列转换成字符串输出（已空格为分隔符）

```js
var reverseWords = function(s) {
    let left = 0
    let right = s.length - 1
    let queue = []
    let word = ''
    while (s.charAt(left) === ' ') left ++
    while (s.charAt(right) === ' ') right --
    while (left <= right) {
        let char = s.charAt(left)
        if (char === ' ' && word) {
            queue.unshift(word)
            word = ''
        } else if (char !== ' '){
            word += char
        }
        left++
    }
    queue.unshift(word)
    return queue.join(' ')
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(N)
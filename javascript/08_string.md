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

## [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

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
- 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231, 231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

#### 内置函数

parseInt() 函数可解析一个字符串，并返回一个整数。

```js
var myAtoi = function (str) {
    const number = parseInt(str, 10);
    const Max = Math.pow(2, 31) - 1;
    const Min = Math.pow(-2, 31);
    
    // 无法转换的情况返回 0
    if (isNaN(number)) {
        return 0;
    }
    // 转换结果超出范围的情况
    if (number < Min || number > Max) {
        return number < 0 ? Min : Max;
    }
    return number;
};
```

#### 正则表达式

```js
var myAtoi = function (str) {
    const input = str.trim();
    let reg = new RegExp(/^[\+\-]?\d+/g);
    if (!reg.test(input)) {
        return 0
    }
    return Math.max(Math.min(input.match(reg)[0], Math.pow(2, 31) - 1), Math.pow(-2, 31))
};
```


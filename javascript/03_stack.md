### 栈

[20. 有效的括号](#20. 有效的括号)

#### [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

难度简单

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

###### 遍历

解题思路：

- 利用`栈`的特性：左括号入栈（记录），右括号出栈（匹配-消除），先入后出：保证了有序入栈，每次出栈操作的都是最新入栈的值

解题步骤：

- 边遍历边匹配，遍历的时候遇到左括号存入数组，下次遇到的第一个右括号必须和数组中最后一个元素匹配，否则为无效字符串，匹配完成后从数组中删除此元素。若最终数组为空，表示括号已全部匹配完，字符串有效。

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

- 时间复杂度：O(n)
- 空间复杂度：O(n)

#### [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)

难度困难

给定一个只包含 `'('` 和 `')'` 的字符串，找出最长的包含有效括号的子串的长度。

###### 栈

- 从左往右扫描，已扫描的左括号等待被匹配，用一个栈暂存起来。
- 求长度，存左括号的索引即可，没必要存符号本身。
- 在栈中预置索引 -1 作为一个“参照物”。当左括号匹配光时，栈需要留一个「垫底」的「参照物」，用于计算一段连续的有效长度。
- 当扫描到右括号，它匹配最近一个左括号，即栈顶元素被匹配而出栈，有效长度 = 当前索引 - 出栈后新的栈顶索引，并判断一下是不是全局的最大

```js
var longestValidParentheses = function(s) {
    let maxLen = 0;
    const stack = [];
    stack.push(-1);
    for(let i = 0; i <s.length; i++){
        const c = s[i];
        if(c == '('){// 左括号的索引，入栈
            stack.push(i);
        }else{// 遍历到右括号
            stack.pop();// 栈顶的左括号被匹配，出栈
            if(stack.length){// 栈未空
                const curMaxLen = i - stack[stack.length - 1];// 计算有效连续长度
                maxLen = Math.max(maxLen, curMaxLen); // 最大值
            }else{// 栈空了
                stack.push(i);// 入栈充当参照
            }
        }
    }
    return maxLen;
};
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)

#### [150. 逆波兰表达式求值](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

难度中等189

根据[ 逆波兰表示法](https://baike.baidu.com/item/逆波兰式/128437)，求表达式的值。

有效的运算符包括 `+`, `-`, `*`, `/` 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

**说明：**

- 整数除法只保留整数部分。
- 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

###### 栈

```js
var evalRPN = function(tokens) {
    let stack = [];
    let num;
    for(let char of tokens){
        switch(char){
            case "+":
                stack.push(stack.pop() + stack.pop());
                break;
            case "-":
                num = stack.pop();
                stack.push(stack.pop() - num);
                break;
            case "*":
                stack.push(stack.pop() * stack.pop());
                break;
            case "/":
                num = stack.pop();
                stack.push(parseInt(stack.pop() / num, 10));
                break;
            default:
                stack.push(parseInt(char, 10));
        }
    }
    return stack.pop();
};
```

- 时间复杂度：O(n)
- 空间复杂度：O(n)

逆波兰表达式：

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。

- 平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
- 该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。

逆波兰表达式主要有以下两个优点：

- 去掉括号后表达式无歧义，上式即便写成 1 2 + 3 4 + * 也可以依据次序计算出正确结果。
- 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中。

#### [155. 最小栈](https://leetcode-cn.com/problems/min-stack/)

难度简单

设计一个支持 `push` ，`pop` ，`top` 操作，并能在常数时间内检索到最小元素的栈。

- `push(x)` —— 将元素 x 推入栈中。
- `pop()` —— 删除栈顶的元素。
- `top()` —— 获取栈顶元素。
- `getMin()` —— 检索栈中的最小元素。

###### 辅助栈

解题思路：使用一个辅助栈，与元素栈同步插入与删除，用于存储与每个元素对应的最小值。

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

- 时间复杂度：O(1)
- 空间复杂度：O(n)

 
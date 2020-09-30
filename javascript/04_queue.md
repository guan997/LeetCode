## 队列

#### [641. 设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)

难度中等

设计实现双端队列。
你的实现需要支持以下操作：

- MyCircularDeque(k)：构造函数,双端队列的大小为k。
- insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
- insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
- deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
- deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
- getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
- getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
- isEmpty()：检查双端队列是否为空。
- isFull()：检查双端队列是否满了。

###### 队列

创建数组：

- 先按照队列的容量，创建相应长度的数组，所有元素都默认为-1。这样获得元素时，只要直接返回即可。
  使用head指针，指向队首元素。使用tail指针，指向将要从队尾插入元素的位置，及队尾+1。

插入元素：

- 从头部添加元素时，先将head指针向前移动一位，再将元素插入。从头部移除元素的操作相反。
  从尾部添加元素时，先将元素插入到tail指针的位置，再将tail指针向后移动一位。从尾部移除元素的操作相反。

判断队列为空或已满：

- 如果不断添加元素，最终head指针和tail指针会相遇，此时由于tail指针的位置已有head对应的值占据，则队列已满。
  如果不断删除元素，最终head指针和tail指针会相遇，此时它们指向的位置都为-1，则队列为空。

```js
/*
 * Initialize your data structure here. Set the size of the deque to be k.
 * @param {number} k
 */
var MyCircularDeque = function (k) {
  // 队列的容量
  this.capacity = k;
  // 使用数组存放队列元素，所有的初始值都是-1，取值的时候直接返回
  this.queue = new Array(k).fill(-1);
  // 队列的头指针，即队列头元素的位置
  this.head = 0;
  // 队列的尾指针，即尾部要插入元素的位置，也就是队列的尾元素的位置+1
  this.tail = 0;
};

// 将index-1，需要考虑index到达数组首尾时需要循环
MyCircularDeque.prototype.reduceIndex = function (index) {
  return (index + this.capacity - 1) % this.capacity;
};

// 将index+1，需要考虑index到达数组首尾时需要循环
MyCircularDeque.prototype.addIndex = function (index) {
  return (index + 1) % this.capacity;
};

/**
 * Adds an item at the front of Deque. Return true if the operation is successful.
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function (value) {
  // 判断队列是否已满
  if (this.isFull()) {
    return false;
  }

  // 从头部插入元素时，要先将头指针向前移动一位
  this.head = this.reduceIndex(this.head);
  // 在新的头指针位置插入元素
  this.queue[this.head] = value;

  return true;
};

/**
 * Adds an item at the rear of Deque. Return true if the operation is successful.
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function (value) {
  // 判断队列是否已满
  if (this.isFull()) {
    return false;
  }

  // 在尾指针的位置插入元素
  this.queue[this.tail] = value;
  // 将尾指针向后移动一位，指向下一次插入元素的位置
  this.tail = this.addIndex(this.tail);

  return true;
};

/**
 * Deletes an item from the front of Deque. Return true if the operation is successful.
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function () {
  // 判断队列是否为空
  if (this.isEmpty()) {
    return false;
  }

  // 将头指针的值置为-1，表示元素被删除
  this.queue[this.head] = -1;
  // 删除元素后，要将头指针向后移动一位
  this.head = this.addIndex(this.head);

  return true;
};

/**
 * Deletes an item from the rear of Deque. Return true if the operation is successful.
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function () {
  // 判断队列是否为空
  if (this.isEmpty()) {
    return false;
  }

  // 先将尾指针向前移动一位，指向队尾元素
  this.tail = this.reduceIndex(this.tail);
  // 将队尾元素设置为-1
  this.queue[this.tail] = -1;

  return true;
};

/**
 * Get the front item from the deque.
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function () {
  // 直接返回头指针的元素即可，由于初始值是-1，因此如果队列为空，会返回-1
  return this.queue[this.head];
};

/**
 * Get the last item from the deque.
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function () {
  // 直接返回尾指针-1的元素即可，由于初始值是-1，因此如果队列为空，会返回-1
  return this.queue[this.reduceIndex(this.tail)];
};

/**
 * Checks whether the circular deque is empty or not.
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function () {
  // 如果头尾指针的位置相同，且对应位置的值为-1，表示队列中已无元素，则为空
  return this.head === this.tail && this.queue[this.head] < 0;
};

/**
 * Checks whether the circular deque is full or not.
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function () {
  // 如果头尾指针的位置相同，且对应位置的值不为-1，此时无法再插入元素，则队列已满
  return this.head === this.tail && this.queue[this.head] >= 0;
};
```

- `转载自`Lee [Chen](https://leetcode-cn.com/problems/design-circular-deque/solution/leetcodeti-jie-641-she-ji-xun-huan-shuang-duan-d-2/)

#### [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)

难度困难

给定一个数组 *nums*，有一个大小为 *k* 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 *k* 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

###### 双向队列

解题思路： 使用一个双端队列存储窗口中值的 索引 ，并且保证双端队列中第一个元素永远是最大值，那么只需要遍历一次 nums，就可以取到每次移动时的最大值。

- 比较当前元素 i 和双端队列第一个元素（索引值），相差 >= k 时队首出列
- 依次比较双端队列的队尾与当前元素 i 对应的值，队尾元素值较小时出列，直至不小于当前元素 i 的值时，或者队列为空，这是为了保证当队头出队时，新的队头依旧是最大值
- 当前元素入队
- 从第 K 次遍历开始，依次把最大值（双端队列的队头）添加到结果 result 中

```js
var maxSlidingWindow = function (nums, k) {
    const deque = []
    const result = []
    for (let i = 0; i < nums.length; i++) {
        // 把滑动窗口之外的踢出
        if (i - deque[0] >= k) {
            deque.shift()
        }
        while (nums[deque[deque.length - 1]] <= nums[i]) {
            deque.pop()
        }
        deque.push(i)
        if (i >= k - 1) {
            result.push(nums[deque[0]])
        }
    }
    return result
}
```

- 时间复杂度：{O}(N)
- 空间复杂度：{O}(N)

`转载自`[前端瓶子君](https://leetcode-cn.com/problems/sliding-window-maximum/solution/javascriptjie-leetcodehua-dong-chuang-kou-zui-da-z/)
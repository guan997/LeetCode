## 链表

## [141. 环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)

难度简单

给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 `pos` 是 `-1`，则在该链表中没有环。**注意：`pos` 不作为参数进行传递**，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 `true` 。 否则，返回 `false` 。

#### 快慢指针

- 定义两个指针，一快一满。慢指针每次只移动一步，而快指针每次移动两步。
- 如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表

```js
var hasCycle = function(head) {
  let fast = head,slow = head
  while (fast) { // 快指针没有指向null
    if (fast.next == null) return false // 下一个为null了，没有环
    slow = slow.next // 快的前面都有节点，慢的前面当然有
    fast = fast.next.next // 推进2个节点
    if (slow === fast) return true // 快慢指针相遇，有环
  }
  return false // fast为null始终不相遇
};
```

- 时间复杂度：O(N)
- 空间复杂度：O(1)

## [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

难度简单

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

#### 迭代

- 当 l1 和 l2 都不是空链表时，判断 l1 和 l2 哪一个链表的头节点的值更小，将较小值的节点添加到结果里，当一个节点被添加到结果里之后，将对应链表中的节点向后移一位
- 设定一个哨兵节点 prehead ，用于返回合并后的链表。维护一个 prev 指针，调整它的 next 指针。然后，重复以下过程，直到 l1 或者 l2 指向了 null ：如果 l1 当前节点的值小于等于 l2 ，我们就把 l1 当前的节点接在 prev 节点的后面同时将 l1 指针往后移一位。否则，我们对 l2 做同样的操作。不管我们将哪一个元素接在了后面，我们都需要把 prev 向后移一位
- 在循环终止的时候， l1 和 l2 至多有一个是非空的。由于输入的两个链表都是有序的，所以不管哪个链表是非空的，它包含的所有元素都比前面已经合并链表中的所有元素都要大。这意味着我们只需要简单地将非空链表接在合并链表的后面，并返回合并链表即可

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

- 时间复杂度：O(n + m)
- 空间复杂度：O(1)

##  [23. 合并K个升序链表](https://leetcode-cn.com/problems/merge-k-sorted-lists/)

难度困难

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

#### 分治合并

- 在合并两个有序链表的基础上，将 k 个链表配对并将同一对中的链表合并
- 第一轮合并以后， k个链表被合并成了k/2个链表，平均长度为2n/k 
  然后是k/4个链表， k/8个链表等
- 重复这一过程，直到我们得到了最终的有序链表

```js
var mergeKLists = function (lists) {
  /* 分而治之 */
  if (lists.length <= 1) return lists[0] || null;
  const newLists = [];
  for (let i = 0; i < lists.length; i += 2) {
    newLists.push(merge(lists[i], lists[i + 1] || null));
  }
  return mergeKLists(newLists);
};

const merge = (list_1, list_2) => {
  const head = new ListNode(0);
  let tail = head;

  while (list_1 && list_2) {
    if (list_1.val < list_2.val) {
      tail.next = list_1;
      list_1 = list_1.next;
    } else {
      tail.next = list_2;
      list_2 = list_2.next;
    }
    tail = tail.next;
  }

  tail.next = list_1 ? list_1 : list_2;
  return head.next;
};
```

- 时间复杂度：O(kn × logk)
- 空间复杂度：O(log k))
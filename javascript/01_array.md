# 数组

## [88. 合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)

难度简单

给你两个有序整数数组 *nums1* 和 *nums2*，请你将 *nums2* 合并到 *nums1* 中*，*使 *nums1* 成为一个有序数组。

**说明：**

- 初始化 *nums1* 和 *nums2* 的元素数量分别为 *m* 和 *n* 。
- 你可以假设 *nums1* 有足够的空间（空间大小大于或等于 *m + n*）来保存 *nums2* 中的元素。

**示例：**

```
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]
```

#### 合并后排序

数组拼接后`sort`排序。缺点是没有利用`nums1`和`nums2`本身是有序数组的优势。

```js
var merge = function(nums1, m, nums2, n) {
    for(var i = 0; i < nums2.length; i++){
        nums1[ m + i] = nums2[i];
    }
    nums1.sort((a, b) => {
        return a-b;
    });
};
```

- 时间复杂度 : O((n + m)log(n + m))。
- 空间复杂度 : O(1)。

#### 双指针 / 从后向前

- 因为 nums1 的空间都集中在后面，所以从后向前处理排序的数据会更好，节省空间，一边遍历一边将值填充进去
- 设置指针 len1 和 len2 分别指向 nums1 和 nums2 的有数字尾部，从尾部值开始比较遍历，同时设置指针 len 指向 nums1 的最末尾，每次遍历比较值大小之后，则进行填充
  当 len1<0 时遍历结束，此时 nums2 中还有数据未拷贝完全，将其直接拷贝到 nums1 的前面，最后得到结果数组
- 时间复杂度：O(m+n)

```js
var merge = function(nums1, m, nums2, n) {
    let len1 = m - 1;
    let len2 = n - 1;
    let len = m + n - 1;
    while(len1 >= 0 && len2 >= 0) {
        // 注意--符号在后面，表示先进行计算再减1，这种缩写缩短了代码
        nums1[len--] = nums1[len1] > nums2[len2] ? nums1[len1--] : nums2[len2--];
    }
    function arrayCopy(src, srcIndex, dest, destIndex, length) {
        dest.splice(destIndex, length, ...src.slice(srcIndex, srcIndex + length));
    }
    // 表示将nums2数组从下标0位置开始，拷贝到nums1数组中，从下标0位置开始，长度为len2+1
    arrayCopy(nums2, 0, nums1, 0, len2 + 1);
};
```

- 时间复杂度 : O(n + m)。
- 空间复杂度 : O(1)。

## [15. 三数之和](https://leetcode-cn.com/problems/3sum/)

难度中等

给你一个包含 *n* 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 *a，b，c ，*使得 *a + b + c =* 0 ？请你找出所有满足条件且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

#### 数组遍历

- 首先对数组进行排序，排序后固定一个数 nums[i]，再使用左右指针指向 nums[i]后面的两端，数字分别为 nums[L] 和 nums[R]，计算三个数的和 sum 判断是否满足为 0，满足则添加进结果集
- 如果 nums[i]大于 0，则三数之和必然无法等于 0，结束循环
- 如果 nums[i]== nums[i−1]，则说明该数字重复，会导致结果重复，所以应该跳过
- 当 sum == 0时，nums[L]== nums[L+1] 则会导致结果重复，应该跳过，L++
- 当 sum == 0时，nums[R] == nums[R-1]则会导致结果重复，应该跳过，R--

```js
var threeSum = function(nums) {
    let ans = [];
    const len = nums.length;
    if(nums == null || len < 3) return ans;
    nums.sort((a, b) => a - b); // 排序
    for (let i = 0; i < len ; i++) {
        if(nums[i] > 0) break; // 如果当前数字大于0，则三数之和一定大于0，所以结束循环
        if(i > 0 && nums[i] == nums[i-1]) continue; // 去重
        let L = i+1;
        let R = len-1;
        while(L < R){
            const sum = nums[i] + nums[L] + nums[R];
            if(sum == 0){
                ans.push([nums[i],nums[L],nums[R]]);
                while (L<R && nums[L] == nums[L+1]) L++; // 去重
                while (L<R && nums[R] == nums[R-1]) R--; // 去重
                L++;
                R--;
            }
            else if (sum < 0) L++;
            else if (sum > 0) R--;
        }
    }        
    return ans;
};
```

- 时间复杂度：O(n^2)

`转载自`[画手大鹏](https://leetcode-cn.com/problems/3sum/solution/hua-jie-suan-fa-15-san-shu-zhi-he-by-guanpengchn/)

## [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

难度简单

给定一个大小为 *n* 的数组，找到其中的多数元素。多数元素是指在数组中出现次数**大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

用对象记录数出现的次数, 大于一半的就是了

```js
var majorityElement = function(nums) {
   let half = nums.length / 2
   let obj = {}
   for(let num of nums){
      obj[num] = (obj[num] || 0) + 1
      if(obj[num] > half) return num
   }
};
```

- 时间复杂度: O(n) 
- 空间复杂度: O(n) 

## [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

难度困难

给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

解题思路：

- 先将小于等于0的元素转换成大于数组长度的数
- 再遍历出所有小于数组长度的元素，以这些元素当下标，使此下标的元素变为负数
- 最后遍历出第一个正数，返回它的下标+1，如遍历完也没有就返回数组长度+1

```js
var firstMissingPositive = function(nums) {
   let n = nums.length
    for(let i = 0; i < n ;i++){        
        if(nums[i] <=0) nums[i] = n + 1
    }
    for(let i = 0 ; i < n ;i++){
        let num = Math.abs(nums[i])
        if(num <= n){
            nums[num - 1] = -Math.abs(nums[num - 1])
        }
    }
    for(let i =0 ; i < n; i++){
        if(nums[i] > 0) return i + 1
    }
    return n + 1
};
```

- 时间复杂度: O(n) 
- 空间复杂度: O(n) 

## [283. 移动零](https://leetcode-cn.com/problems/move-zeroes/)

难度简单

给定一个数组 `nums`，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

**示例:**

```
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
```

**说明**:

1. 必须在原数组上操作，不能拷贝额外的数组。
2. 尽量减少操作次数。

#### 双指针+两次遍历

创建两个指针i和j，第一次遍历的时候指针j用来记录当前有多少非0元素。即遍历的时候每遇到一个非0元素就将其往数组左边挪，第一次遍历完后，j指针的下标就指向了最后一个非0元素下标。
第二次遍历的时候，起始位置就从j开始到结束，将剩下的这段区域内的元素全部置为0。

```js
var moveZeroes = function(nums) {
    if(nums == null){
        return;
    }
    let n = nums.length, j = 0;
    //第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]
    for(let i = 0; i < n; i++){
        //当前元素!=0，就把其交换到左边，等于0的交换到右边
        if(nums[i] != 0){
            nums[j++] = nums[i];
        }
    }
    //非0元素统计完了，剩下的都是0了
	//所以第二次遍历把末尾的元素都赋为0即可
    for(let i = j; i < nums.length; ++i){
        nums[i] = 0;
    }
};
```

- 时间复杂度: O(n)
- 空间复杂度: O(1)

#### 双指针+一次遍历

参考快速排序的思想，首先确定一个待分割的元素做中间点x，然后把所有小于等于x的元素放到x的左边，大于x的元素放到其右边。
用0当做这个中间点，把不等于0(注意题目没说不能有负数)的放到中间点的左边，等于0的放到其右边。
这的中间点就是0本身，使用两个指针i和j，只要nums[i]!=0，我们就交换nums[i]和nums[j]

```js
var moveZeroes = function(nums) {
    if(nums == null){
        return;
    }
    let n = nums.length, j = 0;
    //两个指针i和j
    for(let i = 0; i < n; i++){
        //当前元素!=0，就把其交换到左边，等于0的交换到右边
        if(nums[i] != 0){
            let tmp = nums[i];
            nums[i] = nums[j];
            nums[j++] = tmp;
        }
    }
};
```

- 时间复杂度: O(n)
- 空间复杂度: O(1)
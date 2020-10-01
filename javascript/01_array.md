### 数组

#### [15. 三数之和](https://leetcode-cn.com/problems/3sum/)

难度中等

给你一个包含 *n* 个整数的数组 `nums`，判断 `nums` 中是否存在三个元素 *a，b，c ，*使得 *a + b + c =* 0 ？请你找出所有满足条件且不重复的三元组。

**注意：**答案中不可以包含重复的三元组。

###### 数组遍历

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

#### [169. 多数元素](https://leetcode-cn.com/problems/majority-element/)

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

#### [41. 缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/)

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
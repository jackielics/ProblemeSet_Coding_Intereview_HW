# 300 相同数字的积木游戏1

## 题目描述
小华和小薇一起通过玩积木游戏学习数学。
他们有很多积木，每个积木块上都有一个数字，
积木块上的数字可能相同。
小华随机拿一些积木挨着排成一排，请小薇找到这排积木中数字相同且所处位置最远的2块积木块，计算他们的距离。
小薇请你帮忙替她解决这个问题。

## 输入描述
第一行输入为 N ，表示小华排成一排的积木总数。
接下来 N 行每行一个数字，表示小花排成一排的积木上数字。 \
$0 <= 积木上的数字 < 10^9$ \
$1 <= 积木长度 <= 10^5$
## 输出描述
相同数字的积木的位置最远距离；
如果所有积木数字都不相同，请返回 -1
### 示例一
**输入：**
```shell
5
1
2
3
1
4
```

**输出：**
```shell
3
```

**说明：**  

### 示例二
**输入：**
```shell
2
1
2
```

**输出：**
```shell
-1
```

**说明：**  

## 解题思路
该题的思路是求出数组中数字出现最多的数字，以及该数字的出现次数
- 首先，定义了一个字典 num_count 用于存储数组中的每个数字出现的次数，对数组进行遍历，如果该数字未出现在字典中，则将其记录在字典中，如果该数字已出现在字典中，则将其记录的次数加一。
- 如果字典的长度等于数组的长度，说明数组中的数字不重复，直接返回-1。否则，遍历字典只，对于每个出现次数大于等于 2 的数字，在数组中寻找该数字第一次出现的位置和最后一次出现的位置，并用它们的差值与当前的 maxLen 取最大值。
- 最后返回 maxLen。
## 解题代码

```python
# 输入获取
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
 
 
# 算法入口
def getResult(arr, n):
    idx = {}
 
    for i in range(n):
        num = arr[i]
        if idx.get(num) is None:
            idx[num] = [i]
        else:
            idx[num].append(i)
 
    ans = -1
    for k in idx.keys():
        if len(idx[k]) > 1:
            ans = max(ans, idx[k][-1] - idx[k][0])
 
    return ans
 
 
# 算法调用
print(getResult(arr, n))
```
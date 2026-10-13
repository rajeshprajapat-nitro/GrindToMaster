
<div align="center">

# Maximum Alternating Score

![Medium](https://img.shields.io/badge/Difficulty-Medium-orange?style=flat-square)
![Array](https://img.shields.io/badge/Topic-Array-blue?style=flat-square)
![Greedy](https://img.shields.io/badge/Approach-Greedy-brightgreen?style=flat-square)

</div>

---

## Problem Description

You are given an integer array `nums`. You may rearrange the elements in any order.

The **alternating score** of an array `arr` is defined as:

\[
\text{score} = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + \cdots
\]

Return an integer denoting the **maximum possible alternating score** of `nums` after rearranging its elements.

---

## Examples

### Example 1

**Input**
```text
nums = [1, 2, 3]
```

**Output**
```text
12
```

**Explanation**

One optimal rearrangement is `[2, 1, 3]`.

```text
2² - 1² + 3²
= 4 - 1 + 9
= 12
```

### Example 2

**Input**
```text
nums = [1, -1, 2, -2, 3, -3]
```

**Output**
```text
16
```

**Explanation**

One optimal rearrangement is `[-3, -1, -2, 1, 3, 2]`.

```text
(-3)² - (-1)² + (-2)² - 1² + 3² - 2²
= 9 - 1 + 4 - 1 + 9 - 4
= 16
```

---

## Constraints

- `1 <= nums.length <= 10^5`
- `-4 * 10^4 <= nums[i] <= 4 * 10^4`

---

## Approach — Greedy

The key observation is that the score depends on the **squares** of the elements, not their original signs.

1. Square every element and store the values.
2. Sort the squared values in ascending order.
3. Subtract the smallest `n / 2` values.
4. Add all remaining values.

This maximizes the alternating score by assigning larger squares to positive positions and smaller squares to negative positions.

---

## C++ Solution

```cpp
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        vector<long long> squares;

        for (int x : nums) {
            squares.push_back(1LL * x * x);
        }

        sort(squares.begin(), squares.end());

        long long score = 0;
        int n = squares.size();

        for (int i = 0; i < n; i++) {
            if (i < n / 2) {
                score -= squares[i];
            } else {
                score += squares[i];
            }
        }

        return score;
    }
};
```

---

## Complexity Analysis

| Complexity | Value |
|:--|:--|
| Time | `O(n log n)` |
| Space | `O(n)` |

---

<div align="center">

**Happy Coding!** 💻

</div>


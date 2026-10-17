<h2><a href="https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/">Minimum Swaps to Sort by Digit Sum</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>


<p>You are given an array <code>nums</code> of <strong>distinct positive integers</strong>.</p>


<p>
You need to sort the array in increasing order based on the <strong>sum of the digits</strong> of each number.
If two numbers have the same digit sum, the smaller number appears first in the sorted order.
</p>


<p>
Return the <strong>minimum number of swaps</strong> required to rearrange <code>nums</code> into this sorted order.
</p>

<p>A swap is defined as exchanging the values at two distinct positions in the array.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [37,100]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Compute the digit sum for each integer:
[3 + 7 = 10, 1 + 0 + 0 = 1] → [10, 1]

Sort the integers based on digit sum:
[100, 37]

Swap 37 with 100 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 1.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [22,14,33,7]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Compute the digit sum for each integer:
[2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7 = 7] → [4, 5, 6, 7]

Sort the integers based on digit sum:
[22, 14, 33, 7]

The array is already sorted.
Thus, the minimum number of swaps required to rearrange nums is 0.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [18,43,34,16]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Compute the digit sum for each integer:
[1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1 + 6 = 7] → [9, 7, 7, 7]

Sort the integers based on digit sum:
[16, 34, 43, 18]

Swap 18 with 16, and swap 43 with 34 to obtain the sorted order.
Thus, the minimum number of swaps required to rearrange nums is 2.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
  <li><code>nums</code> consists of distinct positive integers.</li>
</ul>

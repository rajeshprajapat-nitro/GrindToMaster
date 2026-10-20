<h2><a href="https://leetcode.com/problems/sum-of-sortable-integers/">Sum of Sortable Integers</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>
An integer <code>k</code> is called <strong>sortable</strong> if <code>k</code> divides <code>n</code> and you can sort <code>nums</code> in non-decreasing order by sequentially performing the following operations:
</p>

<ul>
  <li>Partition <code>nums</code> into consecutive subarrays of length <code>k</code>.</li>
  <li>Cyclically rotate each subarray independently any number of times to the left or to the right.</li>
</ul>

<p>Return an integer denoting the <strong>sum of all possible sortable integers <code>k</code></strong>.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,1,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
For n = 3, possible divisors are 1 and 3.

For k = 1: each subarray has one element. No rotation can sort the array.

For k = 3: the single subarray [3, 1, 2] can be rotated once to produce [1, 2, 3], which is sorted.

Only k = 3 is sortable. Hence, the answer is 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [7,6,5]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
For n = 3, possible divisors are 1 and 3.

For k = 1: each subarray has one element. No rotation can sort the array.

For k = 3: the single subarray [7, 6, 5] cannot be rotated into non-decreasing order.

No k is sortable. Hence, the answer is 0.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [5,8]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
For n = 2, possible divisors are 1 and 2.

Since [5, 8] is already sorted, every divisor is sortable. Hence, the answer is 1 + 2 = 3.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

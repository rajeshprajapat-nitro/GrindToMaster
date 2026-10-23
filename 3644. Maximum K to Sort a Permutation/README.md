<h2><a href="https://leetcode.com/problems/maximum-k-to-sort-a-permutation/">Maximum K to Sort a Permutation</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>
You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a permutation of the numbers in the range <code>[0..n - 1]</code>.
</p>

<p>
You may swap elements at indices <code>i</code> and <code>j</code> only if
<code>nums[i] AND nums[j] == k</code>, where <code>AND</code> denotes the bitwise AND operation and <code>k</code> is a non-negative integer.
</p>

<p>
Return the <strong>maximum value of <code>k</code></strong> such that the array can be sorted in non-decreasing order using any number of such swaps. If <code>nums</code> is already sorted, return <code>0</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,3,2,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Choose k = 1. Swapping nums[1] = 3 and nums[3] = 1 is allowed
since nums[1] AND nums[3] == 1, resulting in a sorted permutation:
[0, 1, 2, 3].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1,3,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Choose k = 2. Swapping nums[2] = 3 and nums[3] = 2 is allowed
since nums[2] AND nums[3] == 2, resulting in a sorted permutation:
[0, 1, 2, 3].</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [3,2,1,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
Only k = 0 allows sorting since no greater k allows the required swaps
where nums[i] AND nums[j] == k.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
  <li><code>nums</code> is a permutation of integers from <code>0</code> to <code>n - 1</code>.</li>
</ul>

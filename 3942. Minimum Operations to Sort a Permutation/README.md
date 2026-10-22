<h2><a href="https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/">3942. Minimum Operations to Sort a Permutation</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>
You are given an integer array <code>nums</code> of length <code>n</code>, where <code>nums</code> is a permutation of the integers from <code>0</code> to <code>n - 1</code>.
</p>

<p>You may perform only the following operations:</p>

<ul>
  <li><strong>Reverse the entire array.</strong></li>
  <li><strong>Rotate Left by One:</strong> Move the first element to the end of the array, and shift the remaining elements to the left by one position.</li>
</ul>

<p>
Return an integer denoting the <strong>minimum number of operations</strong> required to sort the array in increasing order. If it is not possible to sort the array using only the given operations, return <code>-1</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [0,2,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Rotate Left by one: [2, 1, 0]
Reverse the array: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1,0,2]
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Reverse the array: [2, 0, 1]
Rotate Left by one: [0, 1, 2]

The array becomes sorted in 2 operations, which is minimal.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [2,0,1,3]
<strong>Output:</strong> -1
<strong>Explanation:</strong>
It is impossible to reach [0, 1, 2, 3] using only the given operations.
Thus, the answer is -1.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
  <li><code>nums</code> is a permutation of integers from <code>0</code> to <code>n - 1</code>.</li>
</ul>

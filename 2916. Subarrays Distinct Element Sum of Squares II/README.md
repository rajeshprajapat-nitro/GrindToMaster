<h2><a href="https://leetcode.com/problems/sum-of-squares-of-distinct-counts/">Sum of Squares of Distinct Counts</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>You are given a <strong>0-indexed integer array <code>nums</code>.</strong></p>

<p>The <strong>distinct count</strong> of a subarray of <code>nums</code> is defined as:</p>

<ul>
  <li>
    Let <code>nums[i..j]</code> be a subarray of <code>nums</code>
    consisting of all the indices from <code>i</code> to <code>j</code>
    such that <code>0 &lt;= i &lt;= j &lt; nums.length</code>.
    Then the number of distinct values in <code>nums[i..j]</code>
    is called the distinct count of <code>nums[i..j]</code>.
  </li>
</ul>

<p>
Return the <strong>sum of the squares of distinct counts</strong> of all subarrays of <code>nums</code>.
</p>

<p>Since the answer may be very large, return it modulo <code>10<sup>9</sup> + 7</code>.</p>

<p>A subarray is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> 15
<strong>Explanation:</strong>
Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values

The sum of the squares of the distinct counts in all subarrays is equal to
1² + 1² + 1² + 2² + 2² + 2² = 15.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [2,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value

The sum of the squares of the distinct counts in all subarrays is equal to
1² + 1² + 1² = 3.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
  <li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<hr>

<p><strong>Seen this question in a real interview before?</strong></p>

<p>1/6</p>

<ul>
  <li>Yes</li>
  <li>No</li>
</ul>

<p><strong>Accepted:</strong> 20,612/48.9K</p>

<p><strong>Acceptance Rate:</strong> 42.2%</p>

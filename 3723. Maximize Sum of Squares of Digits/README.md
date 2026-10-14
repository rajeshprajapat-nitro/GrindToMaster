<h2><a href="#">Maximum Good Integer</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>You are given two positive integers <code>num</code> and <code>sum</code>.</p>

<p>A positive integer <code>n</code> is <strong>good</strong> if it satisfies both of the following conditions:</p>

<ul>
  <li>The number of digits in <code>n</code> is exactly <code>num</code>.</li>
  <li>The sum of digits in <code>n</code> is exactly <code>sum</code>.</li>
</ul>

<p>The <strong>score</strong> of a good integer <code>n</code> is the sum of the squares of its digits.</p>

<p>Return a string denoting the good integer <code>n</code> that achieves the maximum score. If there are multiple possible integers, return the maximum one. If no such integer exists, return an empty string.</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> num = 2, sum = 3
<strong>Output:</strong> "30"
<strong>Explanation:</strong> The good integers are 12, 21, and 30.
The score of 12 is 1² + 2² = 5.
The score of 21 is 2² + 1² = 5.
The score of 30 is 3² + 0² = 9.
The maximum score is 9, achieved by "30".</pre>

<hr>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> num = 2, sum = 17
<strong>Output:</strong> "98"
<strong>Explanation:</strong> The good integers are 89 and 98.
Both have a score of 145, so the maximum integer "98" is returned.</pre>

<hr>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> num = 1, sum = 10
<strong>Output:</strong> ""
<strong>Explanation:</strong> No one-digit integer has a digit sum of 10.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= num &lt;= 2 * 10<sup>5</sup></code></li>
  <li><code>1 &lt;= sum &lt;= 2 * 10<sup>6</sup></code></li>
</ul>

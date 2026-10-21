<h2><a href="https://leetcode.com/problems/minimum-operations-to-sort-a-string/">Minimum Operations to Sort a String</a></h2>

<img src="https://img.shields.io/badge/Difficulty-Medium-orange" alt="Difficulty: Medium" />

<hr>

<p>You are given a string <code>s</code> consisting of lowercase English letters.</p>

<p>
In one operation, you can select any substring of <code>s</code> that is <strong>not the entire string</strong> and sort it in non-descending alphabetical order.
</p>

<p>
Return the <strong>minimum number of operations</strong> required to make <code>s</code> sorted in non-descending order. If it is not possible, return <code>-1</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> s = "dog"
<strong>Output:</strong> 1
<strong>Explanation:</strong>
Sort substring "og" to "go".
Now, s = "dgo", which is sorted in ascending order.
Thus, the answer is 1.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> s = "card"
<strong>Output:</strong> 2
<strong>Explanation:</strong>
Sort substring "car" to "acr", so s = "acrd".
Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order.
Thus, the answer is 2.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> s = "gf"
<strong>Output:</strong> -1
<strong>Explanation:</strong>
It is impossible to sort s under the given constraints.
Thus, the answer is -1.</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
  <li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
  <li><code>s</code> consists of only lowercase English letters.</li>
</ul>

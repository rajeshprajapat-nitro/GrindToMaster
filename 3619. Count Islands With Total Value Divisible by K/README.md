<h2>
    <a href="https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/">
        Count Islands With Total Value Divisible by K
    </a>
</h2>

<p>
    <img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty Medium">
</p>

<hr>

<p>
    You are given an <code>m x n</code> matrix <code>grid</code> and a positive integer <code>k</code>. An <strong>island</strong> is a group of <strong>positive</strong> integers (representing land) that are <strong>4-directionally</strong> connected (horizontally or vertically).
</p>

<p>
    The <strong>total value</strong> of an island is the sum of the values of all cells in the island.
</p>

<p>
    Return the number of islands with a total value <strong>divisible by</strong> <code>k</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<img src="https://assets.leetcode.com/uploads/2025/03/06/example1griddrawio-1.png" alt="Example 1 grid illustration">

<pre>
<strong>Input:</strong> grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5
<strong>Output:</strong> 2
<strong>Explanation:</strong> The grid contains four islands. The islands highlighted in blue have a total value that is divisible by 5, while the islands highlighted in red do not.
</pre>

<p><strong class="example">Example 2:</strong></p>

<img src="https://assets.leetcode.com/uploads/2025/03/06/example2griddrawio.png" alt="Example 2 grid illustration">

<pre>
<strong>Input:</strong> grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3
<strong>Output:</strong> 6
<strong>Explanation:</strong> The grid contains six islands, each with a total value that is divisible by 3.
</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>m == grid.length</code></li>
    <li><code>n == grid[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 1000</code></li>
    <li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
    <li><code>0 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
    <li><code>1 &lt;= k &lt;= 10<sup>6</sup></code></li>
</ul>

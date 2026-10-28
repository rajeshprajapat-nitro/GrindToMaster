<h2>
    <a href="https://leetcode.com/problems/minimum-path-xor/">
        Minimum Path XOR
    </a>
</h2>

<p>
    <img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty Medium">
</p>

<hr>

<p>
    You are given a 2D integer array <code>grid</code> of size <code>m * n</code>.
</p>

<p>
    You start at the top-left cell <code>(0, 0)</code> and want to reach the bottom-right cell <code>(m - 1, n - 1)</code>.
</p>

<p>
    At each step, you may move either right or down.
</p>

<p>
    The cost of a path is defined as the <strong>bitwise XOR</strong> of all the values in the cells along that path, including the start and end cells.
</p>

<p>
    Return the <strong>minimum possible XOR value</strong> among all valid paths from <code>(0, 0)</code> to <code>(m - 1, n - 1)</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,2],[3,4]]
<strong>Output:</strong> 6
<strong>Explanation:</strong>
There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 1 XOR 2 XOR 4 = 7

(0, 0) → (1, 0) → (1, 1) with XOR: 1 XOR 3 XOR 4 = 6

The minimum XOR value among all valid paths is 6.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[6,7],[5,8]]
<strong>Output:</strong> 9
<strong>Explanation:</strong>
There are two valid paths:

(0, 0) → (0, 1) → (1, 1) with XOR: 6 XOR 7 XOR 8 = 9

(0, 0) → (1, 0) → (1, 1) with XOR: 6 XOR 5 XOR 8 = 11

The minimum XOR value among all valid paths is 9.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[2,7,5]]
<strong>Output:</strong> 0
<strong>Explanation:</strong>
There is only one valid path:

(0, 0) → (0, 1) → (0, 2) with XOR: 2 XOR 7 XOR 5 = 0

The XOR value of this path is 0, which is the minimum possible.
</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= m == grid.length &lt;= 1000</code></li>
    <li><code>1 &lt;= n == grid[i].length &lt;= 1000</code></li>
    <li><code>m * n &lt;= 1000</code></li>
    <li><code>0 &lt;= grid[i][j] &lt;= 1023</code></li>
</ul>

<h2>
    <a href="https://leetcode.com/problems/construct-a-grid-with-unique-paths/">
        Construct a Grid With Unique Paths
    </a>
</h2>

<p>
    <img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty Medium">
</p>

<hr>

<p>
    You are given two integers <code>m</code> and <code>n</code>, representing the number of rows and columns of a grid.
</p>

<p>
    Construct any <code>m x n</code> grid consisting only of the characters <code>'.'</code> and <code>'#'</code>, where:
</p>

<ul>
    <li><code>'.'</code> represents a free cell.</li>
    <li><code>'#'</code> represents an obstacle cell.</li>
</ul>

<p>
    A valid path is a sequence of free cells that:
</p>

<ul>
    <li>Starts at the top-left cell <code>(0, 0)</code>.</li>
    <li>Ends at the bottom-right cell <code>(m - 1, n - 1)</code>.</li>
    <li>
        Moves only:
        <ul>
            <li>Right, from <code>(i, j)</code> to <code>(i, j + 1)</code>, or</li>
            <li>Down, from <code>(i, j)</code> to <code>(i + 1, j)</code>.</li>
        </ul>
    </li>
</ul>

<p>
    Return any grid such that there is <strong>exactly one valid path</strong> from the top-left cell to the bottom-right cell.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> m = 2, n = 3
<strong>Output:</strong> ["..#","#.."]
<strong>Explanation:</strong>
The only valid path is:
(0,0) → (0,1) → (1,1) → (1,2)
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> m = 3, n = 3
<strong>Output:</strong> ["..#","#..","##."]
<strong>Explanation:</strong>
The only valid path is:
(0,0) → (0,1) → (1,1) → (1,2) → (2,2)
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> m = 1, n = 4
<strong>Output:</strong> ["...."]
<strong>Explanation:</strong>
The only valid path is:
(0,0) → (0,1) → (0,2) → (0,3)
</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= m, n &lt;= 25</code></li>
</ul>

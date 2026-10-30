 <h2>
    <a href="https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/">
        3970. Shortest Path With at Most K Consecutive Identical Characters
    </a>
</h2>

  
<p>
    <img src="https://img.shields.io/badge/Difficulty-Medium-yellow" alt="Difficulty Medium">
</p>
 
<hr>

<p>
    You are given an integer <code>n</code> representing the number of nodes in a directed weighted graph, numbered from <code>0</code> to <code>n - 1</code>. This is represented by a 2D integer array <code>edges</code>, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code> represents a directed edge from node <code>u<sub>i</sub></code> to node <code>v<sub>i</sub></code> with weight <code>w<sub>i</sub></code>.
</p>

<p>
    You are also given a string <code>labels</code> of length <code>n</code>, where <code>labels[i]</code> is the character assigned to node <code>i</code>, and an integer <code>k</code>.
</p>

<p>
    Return the minimum total edge weight of a path from node <code>0</code> to node <code>n - 1</code> such that the concatenation of the labels of the nodes along the path contains at most <code>k</code> consecutive identical characters.
</p>

<p>
    If no valid path exists, return <code>-1</code>.
</p>

<hr>

<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

<strong>Output:</strong> 3

<strong>Explanation:</strong>
The optimal valid path from node 0 to node 2 is as follows:

Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.

The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters.

Thus, the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

<strong>Output:</strong> 2

<strong>Explanation:</strong>
The optimal valid path from node 0 to node 2 is as follows:

Use edges[0] = [0, 1, 1] to reach node 1 with a weight wi = 1.

Use edges[1] = [1, 2, 1] to reach node 2 with a weight wi = 1.

The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters.

Thus, the answer is 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

<strong>Output:</strong> -1

<strong>Explanation:</strong>
There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters.

Thus, the answer is -1.
</pre>

<hr>

<p><strong>Constraints:</strong></p>

<ul>
    <li><code>1 &lt;= n == labels.length &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>0 &lt;= edges.length &lt;= 5 * 10<sup>4</sup></code></li>
    <li><code>edges[i] == [u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>]</code></li>
    <li><code>0 &lt;= u<sub>i</sub>, v<sub>i</sub> &lt;= n - 1</code></li>
    <li><code>u<sub>i</sub> != v<sub>i</sub></code></li>
    <li><code>1 &lt;= w<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
    <li><code>labels</code> consists of lowercase English letters.</li>
    <li><code>1 &lt;= k &lt;= 50</code></li>
</ul>

# [Prefix and Suffix Search](https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/)
<p>Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.</p>

<p>Implement the <code>WordFilter</code> class:</p>

<ul>
	<li><code>WordFilter(string[] words)</code> Initializes the object with the <code>words</code> in the dictionary.</li>
	<li><code>f(string prefix, string suffix)</code> Returns <em>the index of the word in the dictionary</em> which has the prefix <code>prefix</code> and the suffix <code>suffix</code>. If there is&nbsp;more than one valid index, return <strong>the largest</strong> of them. If there is no such word in the dictionary, return <code>-1</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input</strong>
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
<strong>Output</strong>
[null, 0]

<strong>Explanation</strong>
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 15000</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= prefix.length, suffix.length&nbsp;&lt;= 10</code></li>
	<li><code>words[i]</code>, <code>prefix</code> and <code>suffix</code> consist of lower-case English letters only.</li>
	<li>At most <code>15000</code> calls will be made to the function <code>f</code>.</li>
</ul>


#### Solutions:
- [ ] **C :** [solution.c](solution.c)
- [x] **Python3 :** [solution.py](solution.py)

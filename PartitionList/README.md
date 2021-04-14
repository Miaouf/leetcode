# [Partition List](https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3707/)

Given the ``head`` of a linked list and a value ``x``, partition it such that all nodes **less than** ``x`` come before nodes **greater than or equal** to ``x``.

You should **preserve** the original relative order of the nodes in each of the two partitions.

#### Example 1:
<p align="center">
  <img width="700" src=img/partition.jpg>
</p>

```
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
```

#### Example 2:

```
Input: head = [2,1], x = 2
Output: [1,2]
```

#### Constraints:

- The number of nodes in the list is in the range ``[0, 200]``.
- ``-100 <= Node.val <= 100``
- ``-200 <= x <= 200``

#### Solutions:
- C : [solution.c](solution.c)
- Python3 : [solution.py](solution.py)

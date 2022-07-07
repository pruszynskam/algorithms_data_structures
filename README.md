# Algorithms & data structures

There are 3 tasks completed with use of specific algorithms & data structures in this repository.

1. Matrix escape 

Problem Definition
Input: positive integers p, n, m, a list a[0..n-1] containing n non-negative integers, and a list b[0..m-1] containing m non-negative integers.

The grid cell (i,j) is filled with value (a[i]*b[j])%p. (% is the modulo operator.)
Neo is at grid cell (0,0).
Every grid cell with coordinates (n-1,j) (for 0 ≤ j < m) is an exit point.
Neo can move only to the right (from position (i,j) to (i,j+1)), or to the bottom (from position (i,j) to (i+1,j)).
Moving to the right costs 2*x seconds, where x is the value of the target cell.
Moving to the bottom costs x seconds, where x is the value of the target cell.

The task: For each exit point, compute how fast it can be reached by Neo.

Output: A list of m integers (numbers of seconds to reach each exit point).

![image](https://user-images.githubusercontent.com/100381554/177749520-fc93cce6-8691-4aa2-aa26-917fc3c7423c.png)
![image](https://user-images.githubusercontent.com/100381554/177749703-78269f9d-dbf4-48d3-b0ff-b6fc8c7ba269.png)


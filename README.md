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

Sample input: File input0.txt

![image](https://user-images.githubusercontent.com/100381554/177749520-fc93cce6-8691-4aa2-aa26-917fc3c7423c.png)
![image](https://user-images.githubusercontent.com/100381554/177750251-13078f39-193e-4adf-bef7-151768b4f9b4.png)


2. Tower Game

Problem Definition
Input: a positive integer n, and a two-dimensional list blocks[0..n-1][0..1] of integers.

The i-th block is described by block[i]: the x-coordinate of its left end is block[i][0] (allowed to be negative), and its length is block[i][1] (only positive).
If a block has length 1, it is a golden block (a unit square).
If a block has length 2 or 3, it is a horizontal block.
If a block has length 4 or more, it is a vertical block.
In the beginning, the total score is 0.
For each block (in the order 0 to n-1), the total score is computed as follows: move the block (at its x-coordinate) from infinite height downwards until it touches the ground (height 0) or another block.
If its upper end is higher than that of any block that has been already placed, the total score increases by 1.
If the block is the first golden block that has been placed at its height (there is no other golden block yet whose upper end has the same height), the total score increases by 1.
Thus, for each block, the total score can increase by 0, 1 or 2 points.
The task: For each block, compute the total score after placing it.

Output: A list of n integers (total score after placing each block).

Sample input: File input1.txt

![image](https://user-images.githubusercontent.com/100381554/197005963-69e002de-9a1e-40cc-a1ed-3d228cd40511.png)
![image](https://user-images.githubusercontent.com/100381554/197006114-c4ba7aaf-e30a-46bd-bcf8-64637614ef0a.png)

3. Best Influencer

Problem Definition
Input: integers n, m, s, a list of m links where each link is given by a list of three integers, and a 2D list inf_vals of size s times n of integers. All integers are non-negative.

There are n users in the network numbered from 0 to n-1.
There are m directed links. Each link is given by a list of three values [A,B,C] with the meaning that the links connects user A to user B (i.e., "user B follows user A") and has the fading value C. The fading value is at least 1.
There are s hours. Each inf_vals[i] corresponds to a different hour and contains the so-called influence values of all messages posted in that hour. In more detail, inf_vals[h][A] is the influence value of the message that user A posted at the hour h (inf_vals[h][A]=0 if user A didn't post any message).
Each message is unique, that is, no two users post the same message.
The spreading and impact of a message

When a user posts a message, it is spread in form of copies throughout the network, where each copy's influential value decreases by the fading values of the respective link.

In more detail: If a user A posts or receives a message with some influential value X, a copy of the message is automatically sent along (spread) to each of its followers. Every copy has initially the same influence X, but as the copy moves along the link from A to the respective follower, its influence decreases by the link's fading value (influence value minus fading value). That is, if C is the fading value, the copy's influence decreases to X-C. If the resulting influence is negative or 0, the message does not arrive to the follower. If the influential value is positive, the follower receives the message (as a copy with the decreased influence value of X-C) and the whole process continues recursively.

After the spreading of a message has finished, which happens instantly before the next hour starts, you measure its impact on the network as follows:

You look at all users who received that message (not counting the user who posted it first).
If such a user received several copies of that message (e.g. from different links), you just consider the copy with maximum influence value.
You sum up the influence values of that message over all these users. This sum is called the impact. In other words, the impact of a message (and the user who posted it) is the total influence value of all its copies in the network when counting only one copy per user (the one with maximum influence value) and ignoring the user who posted it.
The impact of a user who did not post any message is 0.
The task: For each of the s hours, your task is to determine the best influencer, that is, the user with the largest impact. If there are several users with the same impact, you return the one with the smallest user ID number.

Output: a list of s integers (the best influencers for each hour).

![image](https://user-images.githubusercontent.com/100381554/197006444-dc6fdc00-253f-4b07-a673-cbcec6e202d7.png)



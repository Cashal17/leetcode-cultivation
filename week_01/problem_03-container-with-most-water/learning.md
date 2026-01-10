## Takeaways:

To understand this question, we had two options. We could brute-force it very easily by just calculating the area for every single pair of lines and keeping track of the maximum value. Since we are just using a couple of pointers, this already means an optimal space complexity of O(1).

However, this would mean a very poor time complexity of O(N^2).
To optimize this to a time complexity of O(N), we take a two-pointer approach
where we start at opposite ends and go towards the middle. For every pair of lines, we only increment the pointer that points to the shorter line because for the area between any two lines, the height will be determined by the minimum height between the two lines and the width will be the difference in index between the two lines. So, as long as we move the shorter pointer between every pair of lines and start at opposite ends, we will maintain maximum width while iterating towards maximum height, so we can get to the combination that gives us the maximum area in a greedy O(N) linear solution.

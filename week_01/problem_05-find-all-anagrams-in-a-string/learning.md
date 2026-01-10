## Takeaways:

We could brute-force this problem by simply building a new frequency map for every single substring of s and comparing it against our frequency map for p, but this would be a horrible time complexity of O(N\*M) where M = length of p string. To understand this problem, we had to take a sliding window approach where we maintain two separate hashmaps (one for the frequency map of the p string and one for the current substring of s that we are comparing against p), and we compare the hashmaps directly to determine if current substring of s is anagram of p, to append the starting index.

Sliding window works here to reduce this problem to a linear O(N+M) complexity since it takes O(M) to build its freq map and then O(N) for our sliding window to cover the entire s string. We avoid multiplying by M because we aren't building a new frequency map of size M each iteration compared to the brute-force solution, we are simply updating a single existing map.

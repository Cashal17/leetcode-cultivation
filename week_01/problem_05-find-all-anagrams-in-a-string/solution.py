class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        if s_len < p_len: # since constraints don't limit p.length < s.length
            return []

        p_count = {}    # build freq. map for p word
        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1    

        s_win_count = {}    # build freq. map for first s window
        for ch in s[:p_len]:       
            s_win_count[ch] = s_win_count.get(ch, 0) + 1   

        ans = [0] if p_count == s_win_count else []
        for i in range (p_len, s_len):  # shift window to next window of s
            # add incoming char
            s_win_count[s[i]] = s_win_count.get(s[i], 0) + 1

            # remove outgoing char
            out = s[i-p_len]
            s_win_count[out] -= 1
            if s_win_count[out] == 0:
                del s_win_count[out]

            if p_count == s_win_count:
                ans.append(i - p_len + 1)

        return ans
            

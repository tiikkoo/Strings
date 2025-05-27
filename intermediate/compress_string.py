def compress_string(s):
    """
    Problem: Compress string using character counts (e.g., "aabcccccaaa" -> "a2b1c5a3")
    Example: "aabcccccaaa" -> "a2b1c5a3"
    """
    if not s:
        return ""
    
    compressed = []
    count = 1
    prev_char = s[0]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

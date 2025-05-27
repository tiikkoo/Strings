def longest_word(s):
    """
    Problem: Find the longest word in a string.
    Example: "The quick brown fox" -> "quick"
    """
    words = s.split()
    return max(words, key=len) if words else ""
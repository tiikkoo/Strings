def are_anagrams(s1, s2):
    """
    Problem: Check if two strings are anagrams.
    Example: "listen" and "silent" -> True
    """
    return sorted(s1.lower()) == sorted(s2.lower())

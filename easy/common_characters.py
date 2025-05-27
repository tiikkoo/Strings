def common_characters(s1, s2):
    """
    Problem: Find common characters between two strings.
    Example: common_characters("hello", "world") -> ['l', 'o']
    """
    return list(set(s1) & set(s2))
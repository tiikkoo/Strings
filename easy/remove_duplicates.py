def remove_duplicates(s):
    """
    Problem: Remove duplicate characters from string while maintaining order.
    Example: "hello" -> "helo"
    """
    seen = set()
    result = ""
    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result
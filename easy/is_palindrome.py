def is_palindrome(s):
    """
    Problem: Check if a string reads the same forwards and backwards.
    Example: "racecar" -> True, "hello" -> False
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]
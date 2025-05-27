def is_empty_or_whitespace(s):
    """
    Problem: Check if string is empty or contains only whitespace.
    Example: "   " -> True, "hello" -> False
    """
    return not s.strip()
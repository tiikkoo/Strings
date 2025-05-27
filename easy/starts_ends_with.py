def starts_ends_with(s, prefix, suffix):
    """
    Problem: Check if string starts with prefix and ends with suffix.
    Example: starts_ends_with("hello world", "hello", "world") -> True
    """
    return s.startswith(prefix) and s.endswith(suffix)
def reverse_words(s):
    """
    Problem: Reverse the order of words in a string.
    Example: "hello world" -> "world hello"
    """
    return ' '.join(s.split()[::-1])
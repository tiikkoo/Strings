def capitalize_words(s):
    """
    Problem: Capitalize the first letter of each word.
    Example: "hello world" -> "Hello World"
    """
    return ' '.join(word.capitalize() for word in s.split())
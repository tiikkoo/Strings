def word_frequency(s):
    """
    Problem: Count frequency of each word in a string.
    Example: "hello world hello" -> {"hello": 2, "world": 1}
    """
    words = s.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
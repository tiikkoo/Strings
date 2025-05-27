def count_vowels(s):
    """
    Problem: Count the number of vowels in a string.
    Example: "hello" -> 2
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
def extract_numbers(s):
    """
    Problem: Extract all numbers from a string.
    Example: "abc123def456" -> [123, 456]
    """
    import re
    return [int(x) for x in re.findall(r'\d+', s)]
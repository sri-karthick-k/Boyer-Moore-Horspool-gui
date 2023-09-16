def boyer_moore_horspool(text, pattern):
    # Create a bad character table
    bad_char = {}
    pattern_length = len(pattern)
    
    for i in range(pattern_length - 1):
        bad_char[pattern[i]] = pattern_length - 1 - i
    
    i = 0
    while i <= len(text) - pattern_length:
        j = pattern_length - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            # Pattern found
            yield i

            # Shift the pattern based on bad character heuristic
            i += pattern_length if i + pattern_length < len(text) else 1
        else:
            # Shift the pattern based on bad character heuristic
            i += max(1, bad_char.get(text[i + j], 1))

def search_pattern_in_file(file_path, pattern):
    with open(file_path, 'r') as file:
        text = file.read()
        for match in boyer_moore_horspool(text, pattern):
            print(f"Pattern found at index {match}")

# Example usage:
file_path = 'hello.txt'  # Replace with the path to your file
pattern = "srikarthick1001"

search_pattern_in_file(file_path, pattern)

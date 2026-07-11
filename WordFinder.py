
def word_finder(text, pattern):
    i = 0
    count = 0
    positions = []

    text_length = len(text)
    pattern_length = len(pattern)

    while i <= text_length - pattern_length:
        if text[i:i + pattern_length] == pattern:
            count += 1
            positions.append(i)
        i += 1

    if count > 0:
        return True, count, positions
    else:
        return False, 0, []


# ---- User Input ----
text = input("Enter text: ")
pattern = input("Enter word to find: ")

found, total, places = word_finder(text, pattern)

# ---- Output ----
if found:
    print("Word found!")
    print("Total occurrences:", total)
    print("Positions:", places)
else:
    print("Word not found.")
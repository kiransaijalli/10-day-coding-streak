# Day 3: Check if a String is a Palindrome

def is_palindrome(text):
    # Convert to lowercase and remove spaces
    cleaned_text = text.lower().replace(" ", "")
    return cleaned_text == cleaned_text[::-1]

# Test cases
test_words = ["radar", "python", "A man a plan a canal Panama"]

for word in test_words:
    print(f"'{word}' is palindrome? {is_palindrome(word)}")
def validateInput(value:str) -> bool:
    isString = isinstance(value,str)
    isProperLength = len(value) > 0

    return isString and isProperLength

def checkLongestWordInSentence(sentence:str):
    isValidSentence = validateInput(sentence)
    if(isValidSentence):
        words = sentence.split(" ")
        longestWord =''
        for word in words:
            if len(word) >= len(longestWord):
                longestWord = word 

        return longestWord
    else:
        raise Exception("Please enter a proper sentence")


try:
    sentence = input("Enter the sentence to check longest word: ")
    result = checkLongestWordInSentence(sentence=sentence)
    print("the result is: ",result)
except Exception as e:
    print(str(e))


''' 
ChatGpt Code Review
    1. Correctness
        Your solution works correctly for typical inputs and successfully finds the longest word.
        It handles an empty string scenario and validates input, which is good.
    2. Optimization and Efficiency
        The code is functional, but there are some optimizations and best practices that could make it more concise and efficient.
        The validateInput() function performs two checks (isinstance() and len()), but since Python's str.split() will work safely with an empty string, you could eliminate explicit length checking.
    3. Edge Case Handling
        One edge case to consider is handling punctuation. If the input string contains punctuation like ,, . or !, those characters will be included in the word length calculation, which can lead to inaccurate results.
        For example, with the input "Hello, world!", the longest word would be "world!", including the exclamation mark.
    4. Code Style and Readability
        Overall, your code is readable, but there are a few areas for improvement:
        Variable names: Use more descriptive names, e.g., isString could be isStringType.
        Control flow: Using exceptions to handle invalid input is fine, but a simple return with None or an empty string might make the logic cleaner.

Rating: 7/10
    What you did well:
        The solution works, handles basic edge cases, and has a solid structure.
        Good use of isinstance() and input validation.
    Areas to improve:
        Handle punctuation properly (you didn't account for special characters in words).
        Make the solution more Pythonic and efficient by using built-in functions like max() with key=len.
        You could simplify the validation logic and reduce unnecessary checks, like checking string length explicitly.
    Suggestions:
        Focus on reducing the code's complexity while ensuring it handles all edge cases (e.g., punctuation, empty strings).
        Utilize Python’s built-in features like max(), filter(), or list comprehensions where possible to make your code more concise and optimized.
'''
#Chat Gpt improved code 
import re

def check_longest_word_in_sentence(sentence: str) -> str:
    # Validate input directly, no need for a separate function.
    if not sentence:
        raise ValueError("Please enter a valid sentence.")
    
    # Use regex to remove punctuation and split words.
    words = re.findall(r'\b\w+\b', sentence)
    
    # Find the longest word using max with a key function.
    longest_word = max(words, key=len)
    
    return longest_word

try:
    sentence = input("Enter the sentence to check the longest word: ")
    result = check_longest_word_in_sentence(sentence)
    print("The longest word is:", result)
except Exception as e:
    print(str(e))

import operator
from core.voice import speak
from core.listen import get_input

# Define supported operations
OPERATIONS = {
    "plus": operator.add,
    "sum": operator.add,
    "add": operator.add,
    "minus": operator.sub,
    "Difference": operator.sub,
    "subtract": operator.sub,
    "times": operator.mul,
    "multiply": operator.mul,
    "multiplied": operator.mul,
    "divided": operator.truediv,
    "divide": operator.truediv,
    "mod": operator.mod,
    "modulus": operator.mod,
    "power": operator.pow,
    "raised": operator.pow
}

# Basic word-to-number mapping
WORD_TO_NUM = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20
}

def word_to_number(word):
    return WORD_TO_NUM.get(word.lower())

def extract_numbers(text):
    numbers = []
    for word in text.lower().split():
        if word.isdigit():
            numbers.append(int(word))
        elif word in WORD_TO_NUM:
            numbers.append(WORD_TO_NUM[word])
    return numbers

def detect_operation(text):
    for keyword in OPERATIONS:
        if keyword in text:
            return OPERATIONS[keyword], keyword
    return None, None

def calculate_from_text(text):
    try:
        # Try direct evaluation
        result = eval(text)
        speak(f"The result is {result}")
        return result
    except:
        # Try word-based
        nums = extract_numbers(text)
        op_func, op_word = detect_operation(text)

        if op_func and len(nums) >= 2:
            result = op_func(nums[0], nums[1])
            speak(f"{nums[0]} {op_word} {nums[1]} is {result}")
            return result
        else:
            speak("Sorry, I couldn't understand the calculation.")
            return None

# Main function to handle calculation interaction
def handle_calculation(mode):
    speak("What calculation should I perform?")
    query = get_input(mode)
    if query:
        return calculate_from_text(query)
    else:
        speak("No input received.")
        return None

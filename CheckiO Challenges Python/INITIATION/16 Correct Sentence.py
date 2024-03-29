# Correct Sentence
# https://py.checkio.org/mission/correct-sentence/share/7977b95b0a9d48515e0be1ed85f1114c/
# By Evans Hua @ 20220801

def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    # your code here
    a = text[0]
    a = a.capitalize()
    text = text.replace(text[0], a, 1)
    if text[-1] != '.':
        text = text + '.'
    return text

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."
    
    print("Coding complete? Click 'Check' to earn cool rewards!")

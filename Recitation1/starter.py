# Recitation Activity 1

def translate(translation:dict, msg:str) -> str:
    """
        Write the function translate(translation, msg) where translation is a dictionary and msg a string. The dictionary contains 
        keys of strings that have a value of another string. Your function will be translating msg using the key-value pairs in the 
        dictionary to create a new string that has replaced all the words in the input string with the words' value in the dictionary. 
        If a word in the string is not in the translation dictionary, the word will retain its original form. You can assume that all 
        the keys in the dictionary are lowercase strings and that msg is a non-empty string with no punctuation. You are not allowed 
        to use the re module or any other methods not covered in this activity.

        >>> translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1':'2'} , '1 UP 2 down left right forward')
        '2 down 2 up right left forward'
        >>> translate({'a':'b', 'candy':'three cookies'}, 'We are in a house of CANDY')
        'we are in b house of three cookies'
    """ 
    translated_output = ""
    msg_split = msg.lower().split()

    for word in msg_split:    
        if word in translation:
            translated_output += f"{translation[word]} "
        else:   
            translated_output += f"{word} "
    return translated_output.strip()









if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    pass
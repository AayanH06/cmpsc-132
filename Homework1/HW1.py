# HW1
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
import math


def get_path(file_name):
    """
        Returns a string with the absolute path of a given file_name located in the same directory as this script

        # Do not modify this function in any way

        get_path('words.txt')   # HW1.py and words.txt located in HW1 folder
        'G:\\My Drive\\CMPSC132\\HW1\\words.txt'
    """
    import os
    target_path = os.path.join(os.path.dirname(__file__), file_name)
    return target_path

#Q1
def rectangle(perimeter,area):
    """
        >>> rectangle(14, 10)
        5
        >>> rectangle(12, 5)
        5
        >>> rectangle(25, 25)
        False
        >>> rectangle(50, 100)
        20
        >>> rectangle(11, 5)
        False
        >>> rectangle(11, 4)
        False
    """
    for height in range(1, perimeter // 2):
        width = area / height
        if (2 * width + 2 * height == perimeter) and width.is_integer():
            return int(max(width, height))
    return False

        

#Q2
def to_decimal(oct_num):
    """
        >>> to_decimal(237) 
        159
        >>> to_decimal(35) 
        29
        >>> to_decimal(600) 
        384
        >>> to_decimal(420) 
        272
    """
    total_deci = 0
    n = 0
    while oct_num > 0:
        temp_digit = oct_num % 10
        total_deci += temp_digit * 8**n
        oct_num = oct_num // 10
        n += 1
    return total_deci


#Q3
def has_hoagie(num):
    """
        >>> has_hoagie(737) 
        True
        >>> has_hoagie(35) 
        False
        >>> has_hoagie(-6060) 
        True
        >>> has_hoagie(-111) 
        True
        >>> has_hoagie(6945) 
        False
    """
    num = abs(num)
    seen_num = [False] * 10

    while num > 0:
        digit = num % 10
        if seen_num[digit]:
            return True
        seen_num[digit] = True
        num = num // 10

    return False


#Q4
def compress(num):
    result = 0
    multiplier = 1
    prev_digit = -1

    while num > 0:
        digit = num % 10
        if digit != prev_digit:
            result += digit * multiplier
            multiplier *= 10
        prev_digit = digit
        num = num // 10

    # Reverse the result to restore original digit order
    final = 0
    while result > 0:
        final = final * 10 + (result % 10)
        result = result // 10

    return final


def is_identical(num_1, num_2):
    """
        >>> is_identical(51111315, 51315)
        True
        >>> is_identical(7006600, 7706000)
        True
        >>> is_identical(135, 765) 
        False
        >>> is_identical(2023, 20) 
        False
    """
    return compress(num_1) == compress(num_2)


#Q5
def hailstone(num):
    """
        >>> hailstone(10)
        [10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(1)
        [1]
        >>> hailstone(27)
        [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(7)
        [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        >>> hailstone(19)
        [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    output = [num]
    while num > 1:
        if num % 2 == 0:
            output.append(int(num / 2))
            num /= 2
        else:
            output.append(int(3*num + 1))
            num = 3*num + 1
    return output



def overloaded_add(d, key, value):
    """
        Adds the key value pair to the dictionary. If the key is already in the dictionary, the value is made a list and the new value is appended to it.
        >>> d = {"Alice": "Engineer"}
        >>> overloaded_add(d, "Bob", "Manager")
        >>> overloaded_add(d, "Alice", "Sales")
        >>> d == {"Alice": ["Engineer", "Sales"], "Bob": "Manager"}
        True
    """
    if key not in d:
        d[key] = value
    elif isinstance(d[key], list):
        d[key].append(value)
    else:
        d[key] = [d[key]]
        d[key].append(value)
    return None


def by_department(d):
    """
        >>> employees = {
        ...    1: {'name': 'John Doe', 'position': 'Manager', 'department': 'Sales'},
        ...    2: {'position': 'Budget Advisor', 'name': 'Sara Miller', 'department': 'Finance'},
        ...    3: {'name': 'Jane Smith', 'position': 'Engineer', 'department': 'Engineering'},
        ...    4: {'name': 'Bob Johnson', 'department': 'Finance', 'position': 'Analyst'},
        ...    5: {'position': 'Senior Developer', 'department': 'Engineering', 'name': 'Clark Wayne'}
        ...    }

        >>> by_department(employees)
        {'Sales': [{'emp_id': 1, 'name': 'John Doe', 'position': 'Manager'}], 'Finance': [{'emp_id': 2, 'name': 'Sara Miller', 'position': 'Budget Advisor'}, {'emp_id': 4, 'name': 'Bob Johnson', 'position': 'Analyst'}], 'Engineering': [{'emp_id': 3, 'name': 'Jane Smith', 'position': 'Engineer'}, {'emp_id': 5, 'name': 'Clark Wayne', 'position': 'Senior Developer'}]}
    """
    output = {}

    for emp_id in d:
        info = d[emp_id]
        dept = info["department"]
        entry = {
            'emp_id'    : emp_id,
            'name'      : info['name'],
            'position'  : info['position']
        }
        if dept not in output:
            output[dept] = []
        
        output[dept].append(entry)

    return output


def successors(file_name):
    """
        >>> expected = {'.': ['We', 'Maybe'], 'We': ['came'], 'came': ['to'], 'to': ['learn', 'have', 'make'], 'learn': [',', 'how'], ',': ['eat'], 'eat': ['some'], 'some': ['pizza'], 'pizza': ['and', 'too'], 'and': ['to'], 'have': ['fun'], 'fun': ['.'], 'Maybe': ['to'], 'how': ['to'], 'make': ['pizza'], 'too': ['!']}
        >>> returnedDict = successors('items.txt')
        >>> expected == returnedDict
        True
        >>> returnedDict['.']
        ['We', 'Maybe']
        >>> returnedDict['to']
        ['learn', 'have', 'make']
        >>> returnedDict['fun']
        ['.']
        >>> returnedDict[',']
        ['eat']
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better
    result = {}
    word = ''
    prev = '.'

    for char in contents:
        if char.isalnum():
            word += char
        else:
            if word:    
                if prev not in result:
                    result[prev] = []
                if word not in result[prev]:
                    result[prev].append(word)
                prev = word
                word = ''
            if not char.isspace():
                if prev not in result:
                    result[prev] = []
                if char not in result[prev]:
                    result[prev].append(char)
                prev = char

    if word:
        if prev not in result:
            result[prev] = []
        if word not in result[prev]:
            result[prev].append(word)

    return result





def addToTrie(trie, word):
    """
        The following dictionary represents the trie of the words "A", "I", "Apple":
            {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}}}
       
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> addToTrie(trie_dict, 'art')
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}}
        >>> addToTrie(trie_dict, 'moon') 
        >>> trie_dict
        {'a': {'word': True, 'p': {'p': {'l': {'e': {'word': True}}}}, 'i': {'word': True}, 'r': {'t': {'word': True}}}, 'm': {'o': {'o': {'n': {'word': True}}}}}
    """
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    current['word'] = True




def createDictionaryTrie(file_name):
    """        
        >>> trie = createDictionaryTrie("words.txt")
        >>> trie == {'b': {'a': {'l': {'l': {'word': True}}, 't': {'s': {'word': True}}}, 'i': {'r': {'d': {'word': True}},\
                     'n': {'word': True}}, 'o': {'y': {'word': True}}}, 't': {'o': {'y': {'s': {'word': True}}},\
                     'r': {'e': {'a': {'t': {'word': True}}, 'e': {'word': True}}}}}
        True
    """
    file_path = get_path(file_name)
    with open(file_path, 'r') as file:   
        contents = file.read()  # You might change .read() for .readlines() if it suits your implementation better 
    trie = {}
    words = contents.split('\n')

    for word in words:
        word = word.lower()
        if word:  # skip empty lines
            addToTrie(trie, word)

    return trie




def wordExists(trie, word):
    """
        >>> trie_dict = {'a' : {'word' : True, 'p' : {'p' : {'l' : {'e' : {'word' : True}}}}, 'i' : {'word' : True}}} 
        >>> wordExists(trie_dict, 'armor')
        False
        >>> wordExists(trie_dict, 'apple')
        True
        >>> wordExists(trie_dict, 'apples')
        False
        >>> wordExists(trie_dict, 'a')
        True
        >>> wordExists(trie_dict, 'as')
        False
        >>> wordExists(trie_dict, 'tt')
        False
    """
    current = trie
    for char in word:
        if char not in current:
            return False
        current = current[char]
    return 'word' in current and current['word'] == True





def run_tests():
    import doctest
    # Run start tests in all docstrings
    doctest.testmod(verbose=False)
    
    # Run start tests per function - Uncomment the next line to run doctest by function. Replace rectangle with the name of the function you want to test
    #doctest.run_docstring_examples(hailstone, globals(), name='HW1',verbose=False)   

if __name__ == "__main__":
    run_tests()
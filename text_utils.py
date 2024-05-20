# function for: Capitalizing the first letter of a word.
def cap_func():
    my_statement = "this is my statement"
    my_value = my_statement.capitalize()
    return(my_value)


# function for: Input function: input() recieves user input and returns a string.
def input_func():
    print("what is your favorite color?")
    y = input()
    return(y+ " is my favorite color!")


# function for: split function split() breaks bigger strings into smaller strings
def split_func():    
    sentence = "I like to learn python"
    mysentence = sentence.split()
    return(mysentence)


# function for: string function str() turns a specified object into a string.
def string_func():    
    value = str(555555)
    return(value)


# function for: join function join() : returns a string ny joining all items in an iterable together.
def join_func():
    sentence = ("join","these", "words")
    x = " ".join(sentence)
    return(x)


# function for: reversed string function: reversed()
def rev_string():
    my_string = 'Hello World'
    reversed_string = reversed(my_string)
    return("".join(reversed_string))


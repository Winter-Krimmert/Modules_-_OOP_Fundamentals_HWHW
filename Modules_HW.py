# 1. Python Modules and Data Handling Assignment
import mood_responses as mr
# Task 1: Your Mood Today

# Problem Statement: Create a Python program using a custom module that asks 
# the user how they are feeling today and responds with a custom message 
# based on the mood entered.


def main():
    mood = input("How are you feeling today? ")
    response = mr.mood_response(mood)
    print(response)

if __name__ == "__main__":
    main()











# 2. Mastering Python Modules and Aliases


import text_utils as tu

capita_word = tu.cap_func()
print (f"We capitalized the first word in: {capita_word}")


reversed_text = tu.rev_string()
print(f"Reversed: {reversed_text}")


variable = tu.input_func()
print(f"print statement: {variable}")


variable1 = tu.split_func()
print(f"the split function splits the string into a list of smaller strings {variable1}")


variable2 = tu.string_func()
print(variable2)


variable3 = tu.join_func()
print(variable3)


variable4 = tu.rev_string()
print(variable4)

"""
This program will read in text input from a file, find any instances of {},
generate a prompt to the user to provide input in the form of whatever text
is between the {}. It will then replace the {} with the user's input.
"""

import re


def get_template():
    """
    Function that reads in text from a file called `madlib_template.txt`
    that exists in the same folder. It generates a string from this text.
    """

    with open('./madlib_template.txt', 'r') as template:
        read_data = template.read()
    return read_data


def generate_prompts():
    """
    Function that takes in a string and returns two arrays. The `words` array
    will contain the content between the {} from the original string. The
    `user_input` array will contain the user's responses to prompts using each
    element of the words array.
    """
    words += re.findall(r"(?<={)[\w<>' -]+(?=})", original_string)
    for word in words:
        user_input.append(input('Give me a new ' + word + ': '))


def generate_new_string():
    """
    
    """
    emptied_string = re.sub((r"(?<={)[\w<>' -]+(?=})"), '', original_string)
    final_string = emptied_string.format(*user_input)
    return final_string


def write_result(str):
    """
    Function that writes a string to a new file called madlib_result.txt
    in the same folder as this module.
    """
    with open('./madlib_result.txt', 'w') as result:
        result.write(str)


words = []
user_input = []
original_string = get_template()
generate_prompts()
write_result(generate_new_string())
print(final_string)

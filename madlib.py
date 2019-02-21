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


def generate_prompts(str):
    """
    Function that takes in a string and returns two arrays. The `words` array
    will contain the content between the {} from the original string. The
    `user_input` array will contain the user's responses to prompts using each
    element of the words array.
    """
    words = []
    user_input = []
    words += re.findall(r"(?<={)[\w<>' -]+(?=})", str)
    for word in words:
        user_input.append(input('Give me a new ' + word + ': '))
    return user_input


def generate_new_string(arr, str):
    """
    
    """
    emptied_string = re.sub((r"(?<={)[\w<>' -]+(?=})"), '', str)
    final_string = emptied_string.format(*arr)
    return final_string


def write_result(str):
    """
    Function that writes a string to a new file called madlib_result.txt
    in the same folder as this module.
    """
    with open('./madlib_result.txt', 'w') as result:
        result.write(str)


original_string = get_template()
user_input = generate_prompts(original_string)
final_string = generate_new_string(user_input, original_string)
write_result(final_string)
print(final_string)

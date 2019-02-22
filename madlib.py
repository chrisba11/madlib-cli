"""
This program will read in text input from a file, find any instances of {},
generate a prompt to the user to provide input in the form of whatever text
is between the {}. It will then replace the {} with the user's input.
"""

import re


def get_template(path, permission):
    """
    Function that reads in text from a file at path with specified permission
    that exists in the same folder as this module. It creates and returns a
    string from this text.
    """
    with open(path, permission) as template:
        read_data = template.read()
    return read_data


def generate_prompts(str):
    """
    Function that takes in a string and returns an array. The returned array
    will contain the user's responses to prompts generated using the content
    between each instance of `{` and `}` from the input string.
    """

    welcome = """


Hello, and welcome to my game! We are going to produce a MadLib story.
I will begin to ask you to choose and write down various word classes
(i.e. Noun, Verb, Adjective). We will use your responses to produce our
story. Please be sure to press enter after each response. Let's go!


    """
    print(welcome)
    words = []
    user_input = []
    words += re.findall(r"(?<={)[\w<>' -]+(?=})", str)
    for word in words:
        user_input.append(input('Give me a new ' + word + ': '))
    return user_input


def generate_new_string(arr, str):
    """
    Function that takes in an array and a string and returns a new string.
    A new string will be emptied of all contents between any instance of `{}`
    and then all instances of `{}` will be replaced with each element of the
    input array. The new string is then returned.
    """
    emptied_string = re.sub((r"(?<={)[\w<>' -]+(?=})"), '', str)
    final_string = emptied_string.format(*arr)
    return final_string


def write_result(str, path, permission):
    """
    Function that takes in a string and writes that string to a new file
    called madlib_result.txt in the same folder as this module.
    """
    with open(path, permission) as result:
        result.write(str)


if __name__ == "__main__":
    original_string = get_template('./madlib_template.txt', 'r')
    user_input = generate_prompts(original_string)
    final_string = generate_new_string(user_input, original_string)
    write_result(final_string, './madlib_result.txt', 'w')
    print(final_string)

# madlib
This program will generate a madlip story from user prompts

**Author**: Chris Ball
**Version**: 1.1.0

## Overview
This app will read a text file, create a string from that file, find all occurances of text inside {} and generate prompts for user input, then it will user the user input to replace all {} and print the new string to a new file.

## Getting Started
Run the program and respond to all prompts. Read the resulting story. It's pretty to use.

## Architecture
This application requires a file that contains some text and one or more cases of '{ with some text here }'. The app opens the file specified and uses regular expressions to find the '{}' in order to pull the contents out to produce a prompt for user input. Whatever the user types in gets captured and stored in an array. When all of the inputs are complete, it will then find and replace all of the '{}' statements and replace the contents with empty strings. The .format() string method can be used with an f-string to grab all empty curly blocks and replace them with values. So, we are iterating through the user_input array and using each element as a replacement value for the curly block. Then we are writing the new string to a new file and printing it to the console.

## API


## Attribution
Paul Williamsen and I worked on this together for a few hours toward the end of the lab after we struggled for hours individually. We found some uses of various string methods online that proved very helpful. (.findall() being the real lifesaver)



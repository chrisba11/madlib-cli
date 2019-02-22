from madlib import get_template, generate_prompts, generate_new_string, write_result

test_array = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22']
test_string = """Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number > 1} {Plural Noun} and {Number > 1} {Plural Noun} in the game, along with hundreds of other {Plural Noun} for you to find."""

test_new_string = """Make Me A Video Game!

I the 1 and 2 3 have 4 5's 6 sister and plan to steal her 7 8!

What are a 9 and backpacking 10 to do? Before you can help 11, you'll have to collect the 12 13 and 14 15 that open up the 16 worlds connected to A 17's Lair. There are 18 19 and 20 21 in the game, along with hundreds of other 22 for you to find."""


def test_get_template():
    actual = get_template('./madlib_template.txt', 'r')
    expected = test_string
    assert actual == expected


# def test_generate_prompts():
#     actual = generate_prompts(get_template())
#     expected = 
#     assert actual == expected


def test_generate_new_string():
    actual = generate_new_string(test_array, test_string)
    expected = test_new_string
    assert actual == expected


# def test_write_result():
#     actual = write_result(test_new_string, './madlib_result.txt', 'w')
#     expected = get_template('./madlib_result.txt', 'r')
#     assert actual == expected

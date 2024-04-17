'''Regular expressions (regex) in Python are powerful tools for pattern matching and text manipulation. Python provides the re module for working with regular expressions. '''

import re
pattern = "you+[a-z]"   # pattern to find in text.
text = '''The principle purpose of the introduction is to present your position (this is also known as the "thesis" or "argument") on the issue at hand but effective introductory paragraphs are so much more than that. Before you even get to this thesis statement, for example, the essay should begin with a "hook" that grabs the reader’s attention and makes them want to read on. Examples of effective hooks include relevant quotations ("no man is an island") or surprising statistics ("three out of four doctors report that…").
Only then, with the reader’s attention "hooked," should you move on to the thesis. The thesis should be a clear, one-sentence explanation of your position that leaves no doubt in the reader’s mind about which side you are on from the beginning of your essay.
Following the thesis, you should provide a mini-outline which previews the examples you will use to support your thesis in the rest of the essay. Not only does this tell the reader what to expect in the paragraphs to come but it also gives them a clearer understanding of what the essay is about.'''

# match = re.search(pattern,text)  # using search  we can get only first match in text.
# print(match)


matches = re.finditer(pattern,text)  # but using finditer we can get all available matches in text.
for match in matches :
    print(match)
    print(match.span())


#AI
#'''1: Regex Flags:
#Flags can modify how the regular expressions behave. For example, re.IGNORECASE makes the pattern case-insensitive.'''
pattern = r"hello"
text = "Hello World"
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Match found:", match.group())


#'''Substitution : You can use regular expressions to replace parts of a string.'''
text = "hello world"
new_text = re.sub(r"world", "universe", text)
print(new_text)  # Output: hello universe

import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, but not the other term'

for pattern in patterns:
    print ('Searching for "%s" in : \n"%s"' %(pattern, text))

    if re.search(pattern, text):
        print('Match was found.')
    else:
        print('No match was found.')

match = re.search(patterns[0], text)
print(type(match))
print(match.start())
print(match.end())


split_term = '@'
phrase = 'What is your email, It is jiya10101@gmail.com'
print(re.split(split_term, phrase))
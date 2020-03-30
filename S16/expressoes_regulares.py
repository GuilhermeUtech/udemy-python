#Aula sobre expressões regulares
import re

patterns = ['term1','term2']
text = 'this is a string with term1. This another with term2'
print(re.search(patterns[0], text))
for pattern in patterns:
    print('searching for "%s" in "%s"' % (pattern,text))
    if re.search(pattern,text):
        print('\n')
        print('match was found')
    else:
        print('\n')
        print('no match was found')

print(match = re.search(pattern[0], text))


test_phrase = "sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd"
test_patterns = ['sd*', #s seguido de zero ou mais d's
                'sd+', #s seguido de um ou mais d's
                'sd?', #s seguido de 3 d's
                'sd{3}', #s seguido de 2 a 3 d's
                'sd{2,3}',
                ]
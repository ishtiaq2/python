import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other term'

for pattern in patterns:
    print ('Searching for %s in %s' %(pattern, text))

    if re.search(pattern, text):
        print ('Match found')
        print ('Start Index: %d' %(re.search(pattern, text).start()))
        print ('End Index: %d' %(re.search(pattern, text).end()))
    else:
        print ('Match not found')


print ('***********************************************************************')

phrase = 'My email domain part is ishtiaq@yahoo.com'
print (phrase)
print re.split('@', phrase)[1]



print ('***********************************************************************')

phrase = 'Muq, ishtiaq2, ishtia1, Muq, ishtiaq2, Muq'
print (re.findall('Muq', phrase), ', total: ', len(re.findall('Muq', phrase)))


print ('***********************************************************************')

def multi_re_find(patterns, phrase):

    for pattern in patterns:
        print ('Searching the phrase using the re check: %r' %pattern)
        print (re.findall(pattern, phrase))
        print ('\n')

test_phrase = 'sdsd...sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{2,3}']
# sd? = zero or one d not more than that
# sd{3} = s followed by three d's
# sd{2, 3} = s followed by two or three d's

print ('test_phrase: {}'.format(test_phrase))
multi_re_find(test_patterns, test_phrase)

print ('******************************Character set *******************************')

print (multi_re_find(['[sd]'], test_phrase))


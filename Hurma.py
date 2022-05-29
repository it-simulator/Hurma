str1 = '!3@567H569$%#@U)%#6767R7345$%#$M987665#$@##A*^&^%%$'

char = ''
for i in str1:
    if i.isalpha():
        char = ''.join([char,i])

print ('Repository: ', str(char))


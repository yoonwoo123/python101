def negative(num):
    return -1*num

def gutenTag():
    return 'Guten Tag'

# def vietnam(number):
    # member_base = '황여진'
    # return f'{member_base}와 {member}가 베트남에 가요.'

def concat(str1, str2):
    return '%s - %s' % (str1, str2)

def check_long_str(string):
    if len(string) > 10:
        return True
    else:
        return False

if check_long_str(concat('Happy', 'Hacking')):
    print('LONG STRING')
else:
    print('SHORT STRING')

print(concat('Happy', 'Hacking'))
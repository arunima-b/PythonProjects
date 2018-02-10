'''
CIS 122 Spring 2016 Project7-2
Author: Arunima Bhattacharjee
Credit: Lab help hours.
Description: Loops and lists, part-2
'''
#0(a & b)
def middle(L):
    '''
    List -> num
    In the function middle(L), L should have a list of numbers, strings or a mix of both and it should return the middle value of L if its in a length of odd numbers.
    If the length of the list is in an even number then it should return 999999.

    >>>middle([1,2,3,4,5]
    >>>3

    >>>middle([1,2,3,4])
    999999

    >>>middle(['red','blue','green','yellow','black'])
    'green'
    '''
    odd = L[len(L)//2]
    if len(L) % 2 == 0:
        return 999999
    else:
        return odd

#(1)
def passwordChecker(password):
    if no_e_character(password):
        return False
    if not (not_alpha_numeric(password)):
        return False
    if not (any_uc_alpha(password)):
        return False
    if frequent(password):
        return False
    else:
        print('This is a frequently used password')
    if not longer_then_four(password):
        return False
    else:
        print('password is less then four words')
    if not two_numbers(password):
        return False
    else:
        print('Password has less then two numbers')
    
    return True
            
    ''' str -> bool
    The function should return True if it goes through these criteria:
    1)Passwords must be at least 5 characters long
    2)Passwords must contain at least one upper case letter
    3)Passwords must contain at least two numbers
    4)Passwords must include at least one non-alphanumeric character.

    The function should return False if it has any of these criterias:
    1)Passwords may not contain the characters "E" or "e"
    2)The password  may  not  be a frequently  used  password: ['password','Two34!','qwerty', 'letmein', 'trustno1','000000', 'passw0rd']

    >>>passwordChecker('Arun1ma#')
    False
    #It returned False because there is only one number but it is suppose to be two or more numbers.

    >>>passwordChecker('Arunima122#')
    True
    #It returned True because the input has a length of more than five and there are more than two numbers and there is an uppercase and a alphanumeric number.

    >>>passwordChecker('password')
    False
    #This is the frequently used password.
    '''
def no_e_character(password):
    if ('E' in (password)) or ('e' in (password)):
        return False
    
def not_alpha_numeric(password):
    if(password.isalnum()):
        return True

def any_uc_alpha(password):
    for ch in password:
            if ch.isupper():
                return True
        
def frequent(psw):
    pasw = ['password','Two34!','qwerty','letmein','trustno1','000000','passw0rd']
    return not(password in pasw)

def longer_then_four(password):
    if (len(password)>= 5):
        return True

def two_numbers (password):
    counter = 0
    for ch in password:
        if ch.isdigit():
            counter += 1
        if counter == 2:
            return True
    

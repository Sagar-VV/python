# def testing (s):
    
#     a = 20
#     b = 40 
#     Z = 22 + s + a + b
    
#     return (print(Z))


# testing (10)

def romanToInt(s):
    n = len(s)
    i = 0
    j = i + 1
    sum = 0
    
    for i in s :
        
        if (i == 'I') and (j == 'V'):
            print (' inside condition ')
            sum = sum + 4   
        elif i == 'I':
            sum = sum + 1
        elif i == 'V':
            sum = sum + 5
        elif i == 'X':
            sum = sum + 10
        elif i == 'L':
            sum = sum + 50
        elif i == 'C':
            sum = sum + 100
        elif i == 'D':
            sum = sum + 500
            # i +=1
        elif i == 'M':
            sum = sum + 1000
    
    print (sum)
    
romanToInt('V')

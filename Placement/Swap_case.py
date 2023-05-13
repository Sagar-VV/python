def swap_case(s):
    
    s_new = []
    for i in list(s):
        if i.islower():
            s_new.append(i.upper()) 
        elif i.isupper():
            s_new.append(i.lower())
        else:
            s_new.append(i)
    print( "".join(s_new))
    
swap_case('My Name Is Sagar')
my_dict = {}

for i in range(int(input('Total element in dictonary : '))):
    
    name = input('write the name : ')
    score = input('write the score : ')

    
    my_dict[name] = score


arange = (sorted(my_dict.items(), key=lambda kv:
                 (kv[1], kv[0])))

print (arange)
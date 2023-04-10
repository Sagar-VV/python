if __name__ == '__main__':
    
    #MyFunc defined as key for sorting using the second element of the sublist
    def myFunc(x):
        return x[1]
    
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    
    records.sort(key=myFunc)
    
    #Find index till which lowest score is repeated
    i=1
    while i<len(records) and records[i][1]==records[i-1][1]:
        i=i+1
    
    
    #Index i is the first index of second lowest score
    names=[]
    
    #Append name for index i into names []
    names.append(records[i][0])
    i=i+1
    
    #Append rest of names with same second lowest score
    while i<len(records) and records[i][1]==records[i-1][1]:
        names.append(records[i][0])
        i=i+1
    
    #sort list of names
    names.sort()
    for name in names:
        print(name)
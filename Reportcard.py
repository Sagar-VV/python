while True:
    marks=int(input())
    if (marks>90):
        print ('excellent')
    elif (80<marks<=90):
        print('good')
    elif (70<marks<=80):
        print('fair')       
    elif (60<marks<=70):
        print('meets expectations')
    elif (marks <= 60):
        print('below par')

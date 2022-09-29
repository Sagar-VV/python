known_user = ['Tushar','Sagar','Saikiran','Sanjeev','Gokul','Himanshu','Vivek']

while True:
    print('Hi! My name is Jarvis')
    name = input('What is your name: ').strip().capitalize()

    if name in known_user:
        
            print('''Hi{}! Hope you are having a great day'''.format(name))
            remove = input('would you like to be removed(y/n)?:').lower().strip()
        

            if remove == 'y':
                known_user.remove(name)

            elif remove== 'n':
                print('No problem! I dont want you to leave anyway!')
                

    else:
           print('Hmmm I dont think i have met you {}'.format(name).strip())
           add_me = input('Would you like join dark army?(y/n): ')

           if add_me=='y':
            known_user.append(name)

           elif add_me =='n':
            print('Nice to meet you')  
          

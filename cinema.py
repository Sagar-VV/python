films = {
     'Rangrez' : [16,10],
     'Shinchan': [14,10],
     'Indra' : [12,3],
     'Dhoom' : [16,10]
     }

while True:

    choice = input('Which movie would you like to watch?: ').strip().title()

    if choice in films:
        age = int(input('what is your age?: ').strip())

        if age>= films[choice][0]:
            
            
            num_seats = films[choice][1]

            if num_seats >0:
                    print('Enjoy your film')

                    films[choice][1] = films[choice][1]-1

            else:
                 print('sorry we are sold out')

        else:
            print('Sorry Sir! You are underage for that movie')
                    
    else :
        print('Sorry!! We are not able to screen that movie')

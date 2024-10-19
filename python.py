print("select your ride:")
print("1. Bike")
print("2. Car")
choice =int(input("Enter your choice:"))
if(choice ==1): #conditional 1 outer if statement
    print( "what type of Bike?" )
    print("1.scooty\n")
    print("2.scooter\n")
    #condition for selecting the type of bike
    choice2=int(input("Enter choice2:"))
    if choice2==1: #inner if statement
        print("you have selected scooty")
    else:
        print("you have selected scooter")
#User entering option 2
elif( choice ==2): #outer elif statement
    print( "what type of car?" )
    print("1.sedan")
    print("2.XUV")
    choice3=int(input("enter your choice3:"))
    if choice3==1: #inner if statement
    #condition for selecting the type of car
      print("you have selected sedan")
    else:
        print("you have selected XUV")
else: #outer else statement
    print("wrong choice!")
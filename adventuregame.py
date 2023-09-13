name = input("Type your name: ").upper()
print("Welcome", name ,"to this adventure game.")

answer = input("You are on a dirt road and it ended here. Do you wanna go left or right? ").lower()

if answer == "left":
    answer = input("You came across a river? Do you wanna swim or walk? ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an crocodile.")

    elif answer == "walk":
        print("You walked for many miles and died.")

    else:
        print("You chose an invalid option. You lost")

elif answer == "right":
    answer =  input("You come to a bridge. Do you want to cross it? Please right yes or no: ").lower()

    if answer == "no":
        print("You came back to the old road and just got hit by a car and died.")
    
    elif answer == "yes":
        print("You crossed the bridge and got murdered by an armed guy.")

    else:
        print("You chose an invalid option. You lost!")

else:
    print("Not a valid option. You lose.")
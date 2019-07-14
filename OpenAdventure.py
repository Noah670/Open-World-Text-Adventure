answer = raw_input(
    " Traveler, Would you like to start playing and enter the digital world? [ yes / no] ")

if answer.lower().strip() == "yes":

    answer = raw_input(
        "Your physical body has been instantly warped inside some strange and colorful gateway with a large plasma wall blocking the entrance, would you like to go left or right?").lower().strip()
    if answer == "left":
        answer = raw_input(
            "You encounter a lone hiker holding a large broadsword to his chest sitting on a rock in the corner, would you like to talk or run?")

        if answer == "talk":
            print("...Cough...Cough..")
            print("Young traveler... this desolate world of ruin is beyond saving...")
            print("Everyone has dissapeared to seek the path beyond the valley edge ")
            print("Take this broadsword and run as far away as you can from the valley while you still can")
            print("... Good luck, you'll need it traveler...")
            print(" ")
            print(" You pick up the broadsword from the hands of the hiker")
            print("You use the broadsword to cut through the barrier and are able to escape the forcefield wall")
            print("Congragulations traveler, you have won the game! ")

        else:
            print("Good choice, you made it away.")

    elif answer == "right":
        print("You keep on walking towards the right and pick up an energy sword but the plasma is too hot and burns your hands.")
        print( "Game Over !")

    else:
        print("Invalid movement detected, Game Over!")

else:
    print("You have made a terrible choice traveler!")

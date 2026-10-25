print("######## Save the Princess ########")
print("1. You have given the mission to save the princess. Will you accept it ? ")
print("a) Yes")
print("b) No")
choice = input("Enter you choice (a/b) : ")
is_walking = False 
if choice == "a":
    print("The princess was abducted by a monster")
    print("The monster stays in a dark forest inside the lion den.\n It takes 3 days for you to reach the destination by walk")
    print("2. Which one of the below you prefer to travel to the monster location")
    print("a) By walk - without any soldiers , it will take 3 days ")
    print("b) By Horse - with 100 soldiers , it will take 1 day")
    choice = input("Enter you choice (a/b) : ")
    if choice == "a":
        is_walking = True 
    print("Now your outside the monster Den .\n You called the monster.\n It came outside from the den. ")
    print("The monster offered you two choices ")
    print("a) Join hands with him and become the most powerful and richest person in the world")
    print("b) Start a fight and loose everything")
    choice = input("Enter you choice (a/b) : ")
    if choice == "a":
        print("You became the richest and powerful person in the world. Princess die")
        print("You are declared as betrayer and sentenced to death by the King")
        print("--- Game End ---")
    else:
        if is_walking:
            print("You lost the fight. You are killed by the monster. Try again")
            print("--- Game End ---")
        else:
            print("You won the fight along with your 100 soldiers. You returned the kingdom with the Princess")
            print("You are awarded with King's treasure")
            print("--- Game End ---")
else:
    print("The king is angry with you. You have been sentenced to death")
    print("--- Game End ---")
import random

#  2 Modes
#  Mode_Select
print("1. Manual mode\t 2. Automatic mode\nSelect mode: ")
script_type = int(input())

#  Range_Select
print("Enter a range: ")
range = int(input())

#  Randomly Generated Number
the_num = random.randint(1,range+1)
print(the_num)

#  Main_Code
def main():
    guesses = 1

# 1. Manual mode: You have to Guess.
    if int(script_type) == 1:
        #  Keeps going until you guess the_num
        user_guessed_num = 0   
        while user_guessed_num != the_num:
            user_guessed_num = int(input())
            print(num_check(user_guessed_num))
            guesses += 1
        print("Congrats! You guessed the number in {} guesses".format(guesses))
    
# 2. Computer Mode:
# Computer Guesses.
    elif int(script_type) == 2:
        # Used Binary something to search for the_num (I Have no idea)
        mid = int(range/2)
        cond_ = num_check(mid)
        halfer = int(mid/2)

        while cond_: # Using Truthy/Falsy Values
        # loop keeps going til we don't get the empty string (Line no. 60,return value)
            if cond_ == "Higher!":
                mid = int(mid+halfer)
                print("Added {:>6} to mid: {:>6}".format(halfer,mid))
                cond_ = num_check(mid)

            elif cond_ == "Lower!":
                mid = int(mid - halfer)
                print("Removed {:>4} from mid: {:>4}".format(halfer,mid))
                cond_ = num_check(mid)
            guesses += 1    
            halfer /= 2
            halfer = round(halfer)               
        print("Computer guessed the number in {} guesses".format(guesses))

    else:
        print("Invalid Mode")

# Higher/lower Function
def num_check(guessed_num):
    if guessed_num < the_num:
        return "Higher!"
    elif guessed_num > the_num:
        return "Lower!"
    elif guessed_num == the_num:
        return ""

main()

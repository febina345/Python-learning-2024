secret_number=10
guess_count =0
guess_max = 3

while guess_count<guess_max:
    guess=int(input("Guess: "))
    guess_count +=1
    if(guess == secret_number):
        print("You won!")
        break

else:
    print("You lose")
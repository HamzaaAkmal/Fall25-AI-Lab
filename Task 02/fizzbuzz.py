import random

def get_answer(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Number"

def play_now():
    computer = 0
    score= 0
    previous_number= 0


    while True:
        number =random.randint(1, 100)
        computer =previous_number+ number
        print("Number on screen:", number)
        guess = input("Your guess (Fizz/Buzz/FizzBuzz/Number): ").strip()
        correct = get_answer(computer)
        if guess.lower() == correct.lower():
            print("Correct!")
            score += 1
            previous_number = number
        else:
            print("Wrong! Answer was:", correct)
            print("Hidden number was:", computer)
            cont = input("Do you want to continue? (Yes/No): ").strip().lower()
            if cont != "yes":
                print("Your final score is:", score)
                score = 0
                computer = 0
                previous_number= 0
                break

    print("Your final score is:", score)


play_now()
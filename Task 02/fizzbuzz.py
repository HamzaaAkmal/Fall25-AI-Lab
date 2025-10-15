import random

# Core logic that checks divisibility
def check_pattern(value):
    if value % 3 == 0 and value % 5 == 0:
        return "FizzBuzz"
    elif value % 3 == 0:
        return "Fizz"
    elif value % 5 == 0:
        return "Buzz"
    else:
        return "Number"


# Main gameplay function
def start_game():
    total_score = 0
    last_num = 0
    result_sum = 0

    while True:
        current_num = random.randint(1, 100)
        result_sum = last_num + current_num
        print("Generated number:", current_num)

        user_guess = input("Enter your guess (1:Buzz  2:FizzBuzz  3:Number): ").strip()
        actual = check_pattern(result_sum)

        if user_guess.lower() == actual.lower():
            print("Correct answer!")
            total_score += 1
            last_num = current_num
        else:
            print("Incorrect! The right answer was:", actual)
            print("The hidden calculated number was:", result_sum)
            retry = input("Do you want to continue playing? (yes/no): ").strip().lower()
            if retry != "yes":
                print("Final Score:", total_score)
                total_score = 0
                last_num = 0
                result_sum = 0
                break

    print("Game Over. Your total score:", total_score)


# Start the program
start_game()

# Developed by Hamza Akmal — All Rights Reserved.

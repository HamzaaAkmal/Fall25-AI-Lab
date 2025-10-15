# Sample data to test program functionality
film_records = [
    ("Interstellar", 165000000),
    ("Joker", 55000000),
    ("Dune", 165000000),
    ("Avatar: The Way of Water", 350000000),
    ("The Dark Knight Rises", 230000000),
    ("Black Panther", 200000000)
]

film_records = []


def insert_film():
    title = input("Enter the film title: ")
    cost = int(input("Enter the production cost: "))
    film_records.append((title, cost))
    print(f"{title} added successfully!\n")


def analyze_budget():
    if not film_records:
        print("No films available. Please add some first!")
        return

    total_cost = sum(price for _, price in film_records)
    avg_cost = total_cost / len(film_records)
    print(f"Average film production cost: {avg_cost}")

    above_average = []
    for film, cost in film_records:
        if cost > avg_cost:
            gap = cost - avg_cost
            above_average.append((film, gap))
            print(f"{film} exceeds the average by {gap}")

    if above_average:
        print(f"Total films with higher-than-average cost: {len(above_average)}")
    else:
        print("No film has a cost above the average.\n")


print("Welcome to the Film Budget Analyzer!")
print("1 → Add a New Film")
print("2 → Check Film Budget Summary")
print("3 → Exit Program\n")

while True:
    
        user_choice = int(input("Select an option: "))
        if user_choice == 1:
            insert_film()
        elif user_choice == 2:
            analyze_budget()
        elif user_choice == 3:
            print("Exiting program xd.... Have a great day!")
            break
        else:
            print("Invalid choice. Please pick 1, 2, or 3.")
   

    

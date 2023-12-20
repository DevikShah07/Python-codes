def sorting_hat():
    # Initialize house points
    gryffindor_points = 0
    ravenclaw_points = 0
    hufflepuff_points = 0
    slytherin_points = 0

    # Question 1
    q1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))

    if q1 == 1:
        gryffindor_points += 1
        ravenclaw_points += 1
    elif q1 == 2:
        hufflepuff_points += 1
        slytherin_points += 1
    else:
        print("Wrong input.")

# Question 2
    q2 = int(input("Q2) When I’m dead, I want people to remember me as:\n"
                   "1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))

    if q2 == 1:
        hufflepuff_points += 2
    elif q2 == 2:
        slytherin_points += 2
    elif q2 == 3:
        ravenclaw_points += 2
    elif q2 == 4:
        gryffindor_points += 2
    else:
        print("Wrong input.")
# Question 3
    q3 = int(input("Q3) Which kind of instrument most pleases your ear?\n"
                   "1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))

    if q3 == 1:
        slytherin_points += 4
    elif q3 == 2:
        hufflepuff_points += 4
    elif q3 == 3:
        ravenclaw_points += 4
    elif q3 == 4:
        gryffindor_points += 4
    else:
        print("Wrong input.")
# Determine the house with the most points
    houses = {
        "Gryffindor": gryffindor_points,
        "Ravenclaw": ravenclaw_points,
        "Hufflepuff": hufflepuff_points,
        "Slytherin": slytherin_points
    }

    max_house = max(houses, key=houses.get)
    print(f"\nCongratulations! You belong to {max_house}!")

# Run the sorting hat function
sorting_hat()

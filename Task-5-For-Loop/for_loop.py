

import random


rolls = []
six_count = 0
one_count = 0
two_sixes_in_a_row = 0

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1

    if i > 0 and rolls[i] == 6 and rolls[i - 1] == 6:
        two_sixes_in_a_row += 1

print("Dice rolls:", rolls)
print("Number of times rolled 6:", six_count)
print("Number of times rolled 1:", one_count)
print("Number of times rolled two 6s in a row:", two_sixes_in_a_row)

print()

total_jacks = 0
target = 100

while total_jacks < target:
    total_jacks += 10
    print("You completed", total_jacks, "jumping jacks")

    if total_jacks >= target:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip == "yes" or skip == "y":
            print("You completed a total of", total_jacks, "jumping jacks.")
            break
    else:
        remaining = target - total_jacks
        print(remaining, "jumping jacks remaining")

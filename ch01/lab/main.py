import random
# Part A
def main():
    weeks = 16
    classes = 5
    tuition = 6000
    cost_per_week = (tuition / classes) / weeks
    print("Cost per week:", cost_per_week)
    classes_per_week = 3
    cost_per_class = (cost_per_week/classes_per_week)

    print(weeks, type(weeks))
    print(classes, type(classes))
    print(tuition, type(tuition))
    print(cost_per_week, type(cost_per_week))
    print(classes_per_week, type(classes_per_week))
    print(cost_per_class, type(cost_per_class))

    print("The cost per class is:", cost_per_class)

    snacks = ["pizza", "apple", "cookies", "chips", "soda"]

    print(snacks, type(snacks))
    random_snack = random.choice(snacks)
    type(random_snack)

    print("The randomly selected snack is", random_snack)

main()
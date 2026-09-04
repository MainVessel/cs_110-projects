import random

# Part A
def main():

weeks = 16
classes = 5
tuition = 6000
cost_per_week = (tuition / classes) / weeks
print("Cost per week:", cost_per_week)

snacks = ["pizza", "apple", "cookies", "chips", "soda"]

print(snacks, type(snacks))
random_snack = random.choice(snacks)
type(random_snack)

print("The randomly selected snack is", random_snack)

main()

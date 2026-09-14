import random

def main():
        low = int(input("Pick a number "))
        high = int(input("Pick one more number "))

        num_number = int(input("How many numbers would you like to generate? "))

        for i in range(1, num_number):
            rand_num = random.randint(low, high)
            print(f"Random Number {i}:", f"{rand_num}")

main()
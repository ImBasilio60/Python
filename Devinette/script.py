import random
secret_number = random.randint(1, 100)
isFind = False
while not isFind:
    number = input("Enter a number: ")
    if number == "":
        print("You didn't enter a number.")
    else:
        if int(number) == secret_number:
            isFind = True
            print(f"You entered the correct number. {number}")
        else:
            if int(number) > secret_number:
                print("Too high.")
            else:
                print("Too low.")
            isFind = False
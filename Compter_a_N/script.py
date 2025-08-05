def countNumber(number):
    for num in range(number):
        print(num + 1)

number = input("Enter a number: ")
if number == "":
    print("You didn't enter a number.")
else:
    countNumber(int(number))
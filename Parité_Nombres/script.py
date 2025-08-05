def testNumber(value):
    number = int(value)
    result = "pair"
    if number % 2 != 0:
        result = "impair"

    return result

isStoped = False
while not isStoped:
    number = input("Enter a number: ")
    if number == "":
        isStoped = True
        print("Stopping process...")
    else:
        isStoped = False
        print(testNumber(int(number)))

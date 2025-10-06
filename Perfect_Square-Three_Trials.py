mport math

trailCount = 3
for i in range(trailCount):
    print(f"This is your attempt number: {i+1}/{trailCount}")
    userInput = int(input("Enter a number: "))
    if userInput < 0:
        continue
    squareRoot = math.sqrt(userInput)
    if squareRoot * squareRoot == userInput:
        print("Yay!!! Entered number is a perfect square")
        break
    else:
        print("Entered number is not a perfect square!") 
else:
    print("You are out of attempts!!!")

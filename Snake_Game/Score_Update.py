CurrentScore = int(input("Enter current score: "))
with open("data.txt", mode="r") as file:
    data = file.read()
    data = int(data)
    if CurrentScore > data:
        with open("data.txt", mode="w") as file:
            CurrentScore = str(CurrentScore)
            file.write(CurrentScore)
        with open("data.txt", mode="r") as file:
            data = file.read()
            print(f"{data}! You have Recoreded new Record.")
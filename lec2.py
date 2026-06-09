# attempts = 7
# secretno = 5

# for i in range (attempts):
#     guessNo = int(input())
#     if guessNo == secretno:
#         print("congrats you find it") 
#         break
#     elif guessNo<secretno:
#         print("number is low")
    
#     else:
#         print("number is high")    

attempts = 7
secretno = 5

for i in range(attempts):
    guessNo = int(input("Enter your guess: "))

    if guessNo == secretno:
        print("Congrats! You found it.")
        break
    elif guessNo < secretno:
        print("Number is low")
    else:
        print("Number is high")
else:
    print("Sorry, you did not find the number.")
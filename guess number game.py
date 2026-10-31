import random

number = random.randint(1, 10)



answer = input("guess the number between 10 and 1: ").strip()


while True:
 
 if answer == "":
    print("you cant just print a blank")
    answer = input("guess the number between 10 and 1: ").strip()
    
    
 else:
    answer = int(answer)
    break
    

    

while answer != number:

    if answer > number:
        answer = int(input("too high.try again: "))

    
    elif answer < number:
        answer = int(input("too low.try again: "))
        
    



print("BINGO")
  



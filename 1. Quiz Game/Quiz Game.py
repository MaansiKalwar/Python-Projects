print("Welcome to my computer quiz!")

playing =input("Do you want to play?")

if playing.lower() != "yes":
       quit()

print(" OKay! Let's Play :)")
score=0;

answer = input ("What does CPU stands for? ")
if answer.lower() == "central processing unit":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')

answer = input ("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')

answer = input ("What does RAM stands for? ")
if answer.lower() == "random access memory":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')

answer = input ("What does PSU stand for? ")
if answer.lower() == "power supply":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')

answer = input ("What does LAN stands for? ")
if answer.lower() == "local area network":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')

answer = input ("What does WAN? ")
if answer.lower() == "wide area network":
       print('Correct!')
       score += 1
else: 
       print('Incorrect!')  

print("You got " + str(score) + " questions correct! ")  
print("You got " + str(score/6*100) + "%.")    


       


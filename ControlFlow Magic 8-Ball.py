# Magic 8 Ball - Project

#program to select based on if conditions number for fortune telling 

#import random module to make use of randint() to generate random number form range
import random
#assigning a person who is going to play magic- 8 ball

name= "Gayathri"

#Question that you would like to ask the magic 8 ball

question ="Will I win the lottery"

#Store the answer of magic 8 ball's outcome

answer =""

#generate a random number and store it to a variable.

random_number=random.randint(1,14)

#print random_number to check if its generating a number

#print(random_number)

#Logic

if random_number == 1:
   answer = "Yes - definitely"
elif random_number ==2:
 answer="It is decidedly so"
elif random_number ==3:
 answer ="Without a doubt"
elif random_number ==4:
 answer= "Reply hazy, try again"
elif random_number ==5:
  answer = "Ask again later"
elif random_number ==6:
 answer= "Better not tell you now"
elif random_number ==7:
 answer= "My sources say no"
elif random_number ==8:
  answer="Outlook not so good"
elif random_number ==9:
  answer ="Very doubtful"
  #additional range - optional challenge
elif random_number ==10:
  answer ="New 10"
elif random_number ==11:
  answer ="Its choice 11"
elif random_number ==12:
  answer ="Teeny twelve"
elif random_number ==13:
  answer ="Thoughtful 13 choice"
elif random_number ==14:
  answer ="Choice seems to 14 percent"
  #error for anything that might possibly be out of range
else:
  answer= "Error"



#print statement on the terminal:
# if question string is empty - if empty say the user error message, else print with the answer.#optional challenges:
if question =="":
  print("Error, please ask a question to continue playing")

#if name string is empty/ or user not willing to provide change the output format:

elif name =="":
  print("Question:",question)
else:#magic balls result:
  print(name,"asks: ",question)
  print("Magic 8-Ball's answer:"+ answer)









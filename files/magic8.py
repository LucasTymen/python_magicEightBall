import random

random_name = ""
question = "Will I win the lottery?"
answer = ""

random_name = random.randint(1, 5)
#print(random_name)

random_number = random.randint(1, 13)
#print(random_number)

random_question = random.randint(1, 7)
#print(random_question)

# ### defining random_questions ###
if random_question == 1:
  random_question = "Will I win the lottery ?"
elif random_question == 2:
  random_question = "is there an end to the multiverse ?"
elif random_question == 3:
  random_question = "something good, for dinner tonight ?"
elif random_question == 4:
  random_question = "shall i wipe DC Comics from the surface of the earth ?"
elif random_question == 5:
  random_question = "am i a real avenger ?"
elif random_question == 6:
  random_question = "Netflix & Chill ?"
else :
  random_question = " what do you mean ?"

# ### defining random_names ###
if random_name == 1:
  random_name = "the hulk"
elif  random_name == 2:
  random_name = "Spider Man"
elif  random_name == 3:
  random_name = "DeadPool"
elif  random_name == 4:
  random_name = "iron Man"
else:
  random_name = "the invisible guy"
# ### defining  answers as random_number ###
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "You should know"
elif random_number == 11:
  answer = "you maybe not ready for my answer"
elif random_number == 12:
  answer = "Shut it and praise Cthuluh"
elif random_number == 13:
  answer = "i nkow the answer but naaaaah ! don't wanna tell you !"
else :
  answer = "Error"

# ### solving empty strings ###
if len(random_name) == 0:
  print("Question: " + random_question)
else:
  print(random_name + " asks: " + random_question)

print(random_name + " asks:  --->  " + random_question)
print("Magic 8-Ball's answer: ---->  " + answer)

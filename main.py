# Made by Ryan and Aprille
# Took some of the code made by Alicia, Maxwell and Victoria(There was no TM)
#2020-07-11

print("Hello and welcome to a quiz for the first semester\n note: please enter the answer in a LETTER\n")
space=input("Press space and enter to continue:\n")
if space==" ":

    class Question:
        def __init__(self, prompt, answer):
            self.prompt = prompt
            self.answer = answer

question_list = [
    "1. What is the difference between a raster image and a vector image? \n  a) They're the same type of picture but have different names\n  b) A vector image is higher quality and a raster image has lower quality(less and more pixels)\n  c) A raster image is higher quality and a vector image has lower quality\n\n",
  
    "2. Which is the correct code?\n a) print(hello world)\n b) print('hello world)\n c) print('hello world')\n\n",

    "3. What is a set? \n a) An unordered list of items\n b) A list of items that is ordered first in first out\n c) A list of items that is ordered last in first out, first in last out\n\n",

    "4. What is digital forensics? \n a) \n b)\n c)\n",

    "5. What is a stack? \n a) An unordered list of items\n b) A list of items that is ordered first in first out\n c) A list of items that is ordered last in first out, first in last out\n\n",

    "6. What is camel case? \n a) \n b)\n c)\n"
]

question_answers = [
    Question(question_list[0], "b"),
    Question(question_list[1], "c"),
    Question(question_list[2], "a"),
    Question(question_list[3], "a"),
    Question(question_list[4], "c"),
    Question(question_list[5], "a")
]

def run_test(question_answers):
  score = 0
  for question in question_answers:
        answer = input(question.prompt)
        answer = answer.lower
        if answer == question.answer:
            score += 1           
            print("You got " + str(score) + " out of " + str(len(question_answers)) + " correct")
              

run_test(question_answers)
import random


#Simple chat program

#responses to questions
def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "No way!!",
    "Awesome!",
    "That's amazing!",
    "Wow!!!!!",
    "That's crazy!!!",
    "Unbelievable!"
  ]
  return random.choice(responses)

#questions 
def generate_questions(user_input):
  questions = [
    "How old are you?",
    "What's your favorite color?",
    "Who is your favorite singer?",
    "What is your favorite show?",
    "What is your favorite album?",
    "What is your favorite sport?",
    "What's your favorite sports team?",
    "Who is your idol?",
    "Where are you from?",
    "What is your favorite food?",
    "What is your favorite book?",
    "What is your favorite movie?"
  ]
  return random.choice(questions)

#need to figure out how to make sure that the questions aren't repeated. 

#defining q as the letter to end the chat 
def init_chat():
  quit_character = 'lol'

#informing user that they can end chat by pressing q 
  print("DISCLAIMER! If you'd like to end your chat with chat buddy at anytime, please feel free to type lol to end your conversation.")
  user_input = input("Hello, I am chat buddy, who are you?\n")
  
  user_name = user_input
  #variable to make sure that the responses occur after the user introduces themself
  ask1 = 0 

  print(f'Nice to meet you, {user_input} !') 

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    user_input = input( user_name  +", " +  generate_questions(user_input) + "\n" )


    #counting to make sure that the responses occur after the user says their name 
    ask1 += 1
    if ask1 >= 1:
      print(generate_response(user_input))
    
  else:
    print(f"Thank you for chatting with me {user_name} :) !! ")

if __name__ == "__main__":
  init_chat()


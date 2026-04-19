import random
choices=[1,2,3,4,5,6,7,8,9,10]
name=input("enter your name: ")
game_choices = ("bowl","bat")
player_score = 0
bot_score = 0
resultant_score=0
resultant_score1=0
running=True
while running:
  game_choice=input("choose to bowl/bat: ")

  while game_choice in game_choices:
   
   if game_choice=='bowl':
    print(f"{name}'s bowling first!!")
    print("bot's batting now!!")
    while running:
     player_choice= int(input("enter your choice from (1-10): "))

     while player_choice in choices:   
      bot_choice=random.choice(choices)      
      print(f"{name}'s choice: {player_choice}")
      print(f"bot choice: {bot_choice}")
                 
      if bot_choice==player_choice: 
        bot_score+=bot_choice
        print("------------------------------------------------------------------------------")
        print(f"bot ended its batting with: {bot_score} runs!")
        print(f"{name}'s batting now!")
        print("bot's bowling now!")
        print(f"{name} is now batting to chase the target of: {bot_score} runs!!")
        print("------------------------------------------------------------------------------")
        while running:
          player_choice= int(input("enter your choice from (1-10): "))

          while player_choice in choices:    
            bot_choice=random.choice(choices)    
            print(f"{name}'s choice: {player_choice}")
            print(f"bot choice: {bot_choice}")
          
            if player_choice==bot_choice:
              player_score+=player_choice
              print("------------------------------------------------------------------------------")
              print(f"{name}'s score is: {player_score}")
              print(f"bot's score is: {bot_score}")
              if player_score==bot_score:
                print("its a tie!!")
                print("------------------------------------------------------------------------------")
                running=False
                exit(0)

              else:
                resultant_score=player_score-bot_score
                resultant_score1=bot_score-player_score
                print(f"{name} wins with {resultant_score} runs!!" if player_score>bot_score else f"bot wins with {resultant_score1} runs!!") 
                print("------------------------------------------------------------------------------")
                running=False
                exit(0)              

            else:
              player_score+=player_choice
              print(f"{name} score is: {player_score}")
              break
                                                         
      else: 
        bot_score+=bot_choice
        print(f"bot score: {bot_score}")        
        break
        
   else:
    print(f"{name}'s batting first!!")
    print("bot's bowling now!!")
    while running:
     player_choice= int(input("enter your choice from (1-10): "))

     while player_choice in choices:      
      bot_choice=random.choice(choices)  
      print(f"{name}'s choice: {player_choice}")
      print(f"bot choice: {bot_choice}")
          
      if player_choice==bot_choice:
        player_score+=player_choice
        print("------------------------------------------------------------------------------")
        print(f"{name} ended their batting with: {player_score} runs!")
        print(f"{name}'s bowling now!")
        print("bot's batting now!") 
        print(f"bot is now batting to chase the target of: {player_score} runs!!")
        print("------------------------------------------------------------------------------")  
              
        while running:
          player_choice= int(input("enter your choice from (1-10): "))

          while player_choice in choices:        
            bot_choice=random.choice(choices) 
            print(f"{name}'s choice: {player_choice}")
            print(f"bot choice: {bot_choice}")
                 
            if bot_choice==player_choice: 
              bot_score+=bot_choice
              print("------------------------------------------------------------------------------")
              print(f"{name}'s score is: {player_score}")
              print(f"bot's score is: {bot_score}")

              if player_score==bot_score:
                print("its a tie!!")
                print("------------------------------------------------------------------------------")

              else:
                resultant_score=player_score-bot_score
                resultant_score1=bot_score-player_score
                print(f"{name} wins with {resultant_score} runs!!" if player_score>bot_score else f"bot wins with {resultant_score1} runs!!")
                print("------------------------------------------------------------------------------")
                running=False
                exit(0)

            else: 
              bot_score+=bot_choice
              print(f"bot score: {bot_score}")        
              break
                  
      else:
        player_score+=player_choice
        print(f"{name} score: {player_score}")
        break
#########################################
# Title: Jungle Rescue  
# Programmer: Anika Sharma
# Date: 01/03/2021
# Purpose: An interactive jungle rescue adventure game. 
#########################################
from time import *

#for making the straight line
lines = 70

#tracker for game over
gameover = 0

#mission briefing: introduction about the game and user's mission
print('')
print("Hello Daring Adventurer. You will be joining me on a crucial Jungle Rescue mission. We have to find a doctor who got lost trying to deliver lifesaving Malaria vaccines to a nearby village. We have the information of her latest location to reach her. During the journey, we will cross a very dense and dangerous forest, where we will encounter the wildlife and will face numerous challenges. \nThere will be some tough decisions to make, so choose wisely as our fate is up to you! \n")
print("_" * lines)
print('')
sleep(0.5)

#take input from the user for adding an item in the backpack
print("Let's begin our journey with your first choice. In my backpack, I have room for one more item: \n")

print("1) Grappling hook: good for climbing up things. \n2) Slingshot: good for hunting and protecting yourself from wildlife.")

sleep(0.5)
backpack = int(input("\nDo you want to take a grappling hook or a slingshot? Enter 1 or 2: "))
print("_" * lines)
print('')

#take input from the user for direction/path to follow- river or jungle
print("Let's make another major decision for our journey route. Choose: either we can take the river or we can go bushwhacking through the jungle.\n")

sleep(0.5)
print("1) River: Dangerous crocodiles and fast currents. \n2) Jungle: Jaguars, Snakes and monkeys.")

direction = int(input('\nWhich way would you like to go? Enter 1 or 2: '))
print("_" * lines)
print('')

sleep(0.5)
#if direction is river (1)
if direction == 1:
  print('You want to go through the river? Alright. \n')
  sleep(0.5)
  print("*Suddenly, a crocodile stands right in front of us!*\n")
  
  sleep(0.5)
  #if backpack has grappling hook (1)
  if backpack == 1:
    print("We have the grappling hook. If we had the slingshot we could've scared it away. \nWe have 2 choices now:")

    #take input from the user for escaping the crocodile
    print("\n1) Try to escape it using stealth (swim slowly underwater). \n2) Be aggressive and splash water everywhere to scare it. \n")
    
    crocfight = int(input("Which one do you choose? 1 or 2: "))

    sleep(0.5)
    #if user chooses stealth, then game over
    if crocfight == 1:
      gameover = 1
      print("\nThe crocodile saw you and attacked you! You used the ends of your grappling hook to scare the crocodile away, what a fighter!\n However, you suddenly got pulled by the harsh current and were thrown out into the ocean.\n \nYou are now stranded and unfortunately, this mission is over. \nEnd of program")

    #if user chooses to be aggressive, then continue the game
    elif crocfight == 2:
      sleep(0.5)
      print("\nCongratulations! You scared the crocodile and were able to make it out of the river successfully. Now, we continue to walk through the jungle, bushwhacking towards the last known location of the doctor.")
      print("_" * lines)
      print('')
  
  #if backpack has slingshot (2), then continue the game
  elif backpack == 2:
    sleep(0.5)
    print("I am so glad you had that slingshot! We were able to scare the crocodile away and successfully exit the river. Now, we continue to walk through the jungle, bushwhacking towards the last known location of the doctor.")
    print("_" * lines)
    print('')

#if direction is jungle (2)
elif direction == 2:
  print('You want to go bushwhacking through the jungle? Alright. \n')

  #events while bushwhacking
  sleep(0.5)
  print("*Intensively bushwhacks through jungle, which is getting mad dense as we go further*") 
  sleep(0.5)
  print("*Sweating like crazy*") 
  sleep(0.5)
  print("*Hearing weird animal noises*")
  sleep(0.5)
  print("*There are a ton of snakes, but you keep walking* \n")
  print("_" * lines)
  print('')

  sleep(0.5)
  print("We found a mega recent campsite! It appears to be one of the doctor's camps and has been raided by Howler Monkeys. \n*You hear tons of monkey noises* \n")
  sleep(0.5)

  # get the direction choice from user to follow monkeys or climb a tree
  print("We have two ways we can take from here: \n1) Follow the sounds of the monkeys as that usually means they are disturbed. \n2) Climb a tree to get a higher vantage point to determine our direction.\n")

  directionchoice = int(input("So what should we choose? 1 or 2: "))

  sleep(0.5)
  #if user chooses to climb the tree, continue the game
  if directionchoice == 2:
    print("\nYou used your rope to climb the tree and you saw rising smoke from a fire! \nThat fire must have been set by the doctor. Let's walk in that direction and we may be able to find the doctor!")
    
    print("_" * lines)
    print('')

  #if user chooses to follow the monkeys and they have a grappling hook, then game over
  elif directionchoice == 1 and backpack == 1:
    sleep(0.5)
    gameover = 1
    print("\nYou followed the monkeys and they had the doctor's bag! We can follow the bag's direction to try to find the doctor! We have the grappling hook and not the slingshot. If we had the slingshot, we could've scared the monkeys away. \n \nOh look! The monkey took the bag and ran away with it! \n*You try chasing after the monkey but you fall and are injured* \n \nUnfortunately, we cannot keep going. This is where our mission ends. \nEnd of program")

  #if user chooses to follow the monkeys and they have a slingshot, then continue the game
  elif directionchoice == 1 and backpack == 2:
    sleep(0.5)
    print("\n You followed the monkeys and they have the doctor's bag! We can follow the bag's direction to try to find the doctor! \n \nLet's scare the monkeys away using our slingshot. \n*Monkeys successfully scared, they ran away* \nYes! Now we can continue walking in the direction of this bag to try to find the doctor.")

    print("_" * lines)
    print('')

#if the game is not over, the user encounters a cliff
if gameover == 0:
  sleep(0.5)
  print("Oh no! While walking, we have encountered a cliff! We have two ways we can cross this:")
  
  #take input from user for crossing the cliff
  print("\n1) Use the thin log to carefully walk across. \n2) Use the vines to swing across like Tarzan. \n")

  encountercliff = int(input("So, which one would you choose? 1 or 2: "))

  #if the user chooses to cross the cliff using the log and they have a slingshot, then game over
  if encountercliff == 1 and backpack == 2:
    sleep(0.5)
    gameover = 1
    print("\nOh no! The log wasn't strong enough and you fell down. If only you had the grappling hook so that we could climb out of the cliff. \n \nUnfortunately, there is no way out, so our mission ends here. \nEnd of program")

  #if the user chooses to cross the cliff using the log and they have a grappling hook, then user wins
  elif encountercliff == 1 and backpack == 1:
    sleep(0.5)
    print("Oh no! The log wasn't strong enough and you fell down. Luckily, you brought the grappling hook with you. We can use that to climb our way out! Nice thinking.")
  
    print("_" * lines)
    print('')

    # user wins
    sleep(0.5)
    print("As you continue walking, you hear someone shout hello. \nHey! \nHello? \nIt's the doctor! You found her! Congratulations, we did it! Mission successful. \nEnd of program.")

  #if user chooses to cross the cliff using the vines, then the user wins
  elif encountercliff == 2:
    print("\nYou wanted to use the vines? Alright. You ready?")
    
    sleep(0.5)
    print('3...')
    sleep(0.5)
    print('2...')
    sleep(0.5)
    print('1...')
    sleep(0.5) 
    print('Whee, we made it to the other side! Nice thinking!')

    print("_" * lines)
    print('')

    sleep(0.5)
    
    # user wins
    print("As you continue walking, you hear someone shout hello. \nHey! \nHello? \nIt's the doctor! You found her! Congratulations, we did it! Mission successful. \nEnd of program.")

#end of the program
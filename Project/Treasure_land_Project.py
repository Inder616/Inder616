art =r'''
*******************************************************************************
        
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
*******************************************************************************
''' 
print(art)
print("wELCOME TO THE TREASURE ISLAND, YOUR MISSION IS TO FIND THE TREASURE.")
user = input(" Your at a cross road. Where do you want to go? Type left or right: ")

if user == "left":
  print("You stumble upon a serene lake surrounded by dense forest.")
  user = input("Do you want to swim across the lake or wait for a boat? Type 'swim' or 'wait': ")
  if user == "wait":
    print("A mysterious boat takes you safely to an island. There's a house with three colorful doors!")
    door = int(input("Which door do you choose? Type 1, 2, or 3: "))
    if door == 1:
      print("You walk into a room engulfed in flames. GAME OVER.")
    elif door == 2:
      print("Hooray! You discover a golden treasure chest filled with jewels. YOU WIN!")
    elif door == 3:
      print("Creepy spiders swarm you, and you meet a grim fate. GAME OVER.")
    else:
      print("Invalid door. Game over!")
  elif user == "right":
    print("Oops! You misstep into a deep, dark hole. GAME OVER.")
  else:
    print("Invalid option. Please type 'swim' or 'wait'.")
if user == "right":
  print("You're dragged underwater by a ferocious trout. GAME OVER.")
else :
  print("please choose valid direction")

  





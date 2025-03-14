import random
from logo import logo
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):     #function which returns the sum
    
    if sum(cards) == 21 and len(cards) == 2:    #if the sum is 21 and the length of the cards is 2 then return 0
        return 0
    
    if 11 in cards and sum(cards) > 21:        #if the sum is greater than 21 and 11 is in the cards then remove 11 and add 1
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
        if user_score == computer_score:
            return "It's a tie!"
        elif computer_score == 0:
            return "Computer has Blackjack! You lose!"
        elif user_score > 21:
            return "You busted! Computer wins!"
        elif computer_score > 21:
            return "Computer busted! You win!"
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1


    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User's cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or  computer_score == 0 or user_score > 21:
            is_game_over = True
            print("Your score is 0 and computer score is 0")
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("do you want to play again? type 'y' to play again and 'n' to exit: "):
    print("\n" * 20)
    play_game()











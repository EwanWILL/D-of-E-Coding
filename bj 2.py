import random

BLACKJACK = 21
DEALER_THRESHOLD = 17

def draw():
    return random.randint(1, 11)

def draw_until_threshold(cards, threshold):
    while sum(cards) < threshold:
        cards.append(draw())

def check_blackjack(cards):
    return sum(cards) == BLACKJACK

def play_game():
    user_cards = [draw(), draw()]
    computer_cards = [draw(), draw()]

    if check_blackjack(user_cards):
        print("User wins with a Blackjack!")
        return

    while True:
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        should_continue = input("Type 'y' to get another card, 'n' to pass: ")
        if should_continue == 'y':
            user_cards.append(draw())
            if sum(user_cards) > BLACKJACK:
                print("You went over. You lose!")
                return
        else:
            break

    draw_until_threshold(computer_cards, DEALER_THRESHOLD)

    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    if sum(computer_cards) > BLACKJACK or sum(user_cards) > sum(computer_cards):
        print("You win!")
    else:
        print("You lose!")

play_game()
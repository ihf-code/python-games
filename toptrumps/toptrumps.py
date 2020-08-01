# random module required for shuffling deck
import random

# creating a list to hold the top trump cards in
dog_cards = []

# creating each card and adding to the dogs_card list
# categories: name, speed, size, temper, rarity, intelligence, all out of 5
dog_cards.append(["dalmatian", 4, 3, 2, 3, 4])
dog_cards.append(["labrador", 4, 3, 1, 1, 4])
dog_cards.append(["french bulldog", 3, 2, 2, 3, 2])
dog_cards.append(["pug", 2, 2, 2, 2, 2])
dog_cards.append(["great dane", 4, 5, 3, 4, 3])
dog_cards.append(["greyhound", 5, 4, 2, 3, 4])
dog_cards.append(["jack russell", 3, 2, 4, 2, 3])
dog_cards.append(["cocker spaniel", 3, 3, 5, 3, 3])
dog_cards.append(["pitbull", 3, 3, 3, 3, 3])
dog_cards.append(["german shepherd", 4, 4, 3, 3, 5])

# shuffling the deck - so it changes each game
random.shuffle(dog_cards)

# split the deck
player_one_deck = dog_cards[0:5]
computer_deck = dog_cards[5:10]

limbo = []

print("******************************************\n")
print("Welcome to Top Trumps!")
print("******************************************\n")
print("Deck: Dogs")
print("Rules")
print("1. The deck is split between you and the computer")
print("2. You look at the first card of your deck and pick your strongest category.")
print("3. If your value is higher than the computer, their card is added to your deck.")
print("4. If your value is lower than the computer, your card is added to their deck.")
print("5. If their is a draw, both playere and computer cards go into a limbo deck.")
print("The player that wins the next go, gets the limbo cards")
print("The game ends when one player loses all their cards")
print("******************************************\n")
print("Good Luck!")
print("******************************************\n")


while len(player_one_deck) != 0 and len(computer_deck) != 0:
    player_first_card = player_one_deck[0]
    comp_first_card = computer_deck[0]
    print("******************************************\n")
    print("Player One Card:")
    print("Name: " + player_first_card[0])
    print("Speed: " + str(player_first_card[1]))
    print("Size: " + str(player_first_card[2]))
    print("Temper: " + str(player_first_card[3]))
    print("Rarity: " + str(player_first_card[4]))
    print("Intelligence: " + str(player_first_card[5])+"\n")
    print("******************************************\n")

    player_input = int(input(
        "Pick your strongest category.\n1 = Speed\n2 = Size\n3 = Temper\n4 = Rarity\n5 = Intelligence\nEnter a number:"))

    if player_first_card[player_input] > comp_first_card[player_input]:
        player_one_deck.append(computer_deck.pop(0))
        player_one_deck.append(player_one_deck.pop(0))
        print("Player One Wins!")
        if len(limbo) > 0:
            print("You also won the Limbo cards!")
            player_one_deck.append(limbo.pop(0))
            player_one_deck.append(limbo.pop(0))
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

    elif comp_first_card[player_input] > player_first_card[player_input]:
        computer_deck.append(player_one_deck.pop(0))
        computer_deck.append(computer_deck.pop(0))
        print("Computer Wins!")
        if len(limbo) > 0:
            print("The computer also won the Limbo cards!")
            computer_deck.append(limbo.pop(0))
            computer_deck.append(limbo.pop(0))
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

    else:
        print("Player and Computer Draw!")
        limbo.append(player_one_deck.pop(0))
        limbo.append(computer_deck.pop(0))
        print("Limbo Deck: " + str(len(limbo)))
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

print("******************************************\n")
print("Game Over")
if player_one_deck == 0:
    print("You lose!")
else:
    print("You win!")

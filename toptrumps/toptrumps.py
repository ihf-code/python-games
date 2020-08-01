# random module required for shuffling deck
import random

# creating a list to hold the top trump cards in, list of lists
dog_cards = []
cat_cards = []

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

# creating each card and adding to the cat_card list
# categories: name, speed, size, temper, rarity, intelligence, all out of 5
cat_cards.append(["siamese", 4, 3, 2, 3, 4])
cat_cards.append(["british shorthair", 4, 3, 1, 1, 4])
cat_cards.append(["persian", 3, 2, 2, 3, 2])
cat_cards.append(["ragdoll", 2, 2, 2, 2, 2])
cat_cards.append(["savannah", 4, 5, 3, 4, 3])
cat_cards.append(["burmese", 5, 4, 2, 3, 4])
cat_cards.append(["bengal", 3, 2, 4, 2, 3])
cat_cards.append(["sphynx", 3, 3, 5, 3, 3])
cat_cards.append(["scottish fold", 3, 3, 3, 3, 3])
cat_cards.append(["havana brown", 4, 4, 3, 3, 5])

# shuffling the deck - so it changes each game
deck = random.choice([dog_cards, cat_cards])

# split the deck by slicing, giving first half to player one and second half to computer
player_one_deck = deck[0:5]
computer_deck = deck[5:10]

# created an empty limbo list for the cards from a draw to go to
limbo = []


# some text to start the game and explain the rules
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

# while loop that will keep executing code while both players do not have 0 cards
while len(player_one_deck) != 0 and len(computer_deck) != 0:
    # stating the first card by getting the first card from the player's decks
    player_first_card = player_one_deck[0]
    comp_first_card = computer_deck[0]

    # printing out each element of a card by using the index of the list
    print("******************************************\n")
    print("Player One Card:")
    print("Name: " + player_first_card[0])
    print("Speed: " + str(player_first_card[1]))
    print("Size: " + str(player_first_card[2]))
    print("Temper: " + str(player_first_card[3]))
    print("Rarity: " + str(player_first_card[4]))
    print("Intelligence: " + str(player_first_card[5])+"\n")
    print("******************************************\n")

    # getting the player input of their strongest category
    player_input = int(input(
        "Pick your strongest category.\n1 = Speed\n2 = Size\n3 = Temper\n4 = Rarity\n5 = Intelligence\nEnter a number:"))

    # if statement checking if player one has the highest value
    if player_first_card[player_input] > comp_first_card[player_input]:
        # if player one has the highest value, player one gets the computer's card
        player_one_deck.append(computer_deck.pop(0))
        # moving player one's card to back of their deck
        player_one_deck.append(player_one_deck.pop(0))
        print("Player One Wins!")
        # checking if the limbo list has any cards in it
        if len(limbo) > 0:
            print("You also won the Limbo cards!")
            # if the limbo card has cards in it and player one won, player one gets them
            player_one_deck.append(limbo.pop(0))
            player_one_deck.append(limbo.pop(0))
        # printing out current deck lengths
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

    # if statement checking if the computer has the highest value
    elif comp_first_card[player_input] > player_first_card[player_input]:
        # if the computer has the highest value, the computer gets the player one's card
        computer_deck.append(player_one_deck.pop(0))
        # moving the computer's card to back of their deck
        computer_deck.append(computer_deck.pop(0))
        print("Computer Wins!")
        # checking if the limbo list has any cards in it
        if len(limbo) > 0:
            print("The computer also won the Limbo cards!")
            # if the limbo card has cards in it and the computer won, the computer gets them
            computer_deck.append(limbo.pop(0))
            computer_deck.append(limbo.pop(0))
        # printing out current deck lengths
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

    else:
        # if player one or computer doesn't win round, only other option is a draw
        print("Player and Computer Draw!")
        # player one's first card and computer's first card go to the limbo list
        limbo.append(player_one_deck.pop(0))
        limbo.append(computer_deck.pop(0))
        # printing out current deck lengths
        print("Limbo Deck: " + str(len(limbo)))
        print("Player One Deck: " + str(len(player_one_deck)))
        print("Computer Deck: " + str(len(computer_deck)))

# one player has 0 cards, so loop breaks and results are printed
print("******************************************\n")
print("Game Over")
if player_one_deck == 0:
    print("You lose!")
else:
    print("You win!")

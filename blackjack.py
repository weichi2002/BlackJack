
import os
import random


class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
    
def clear():
    os.system("clear")
    
    
def print_cards(cards, hidden):
         
    s = ""
    for card in cards:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|  {}            |".format(card.value)
        else:
            s = s + "\t|  {}             |".format(card.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|       {}        |".format(card.suit)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for card in cards:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for card in cards:
        if card.value == '10':
            s = s + "\t|            {}  |".format(card.value)
        else:
            s = s + "\t|            {}   |".format(card.value)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()
 

def blackjack_game(deck):
    
    #declaration
    # global cards_values
    player_cards = []
    dealer_cards = []
    
    player_score = 0
    dealer_score = 0
    
    while(len(player_cards) < 2):
        
        #deal
        player_card = random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value
        
        #handles if player has two aces
        if len(player_cards) == 2:
            if(player_cards[0].card_value == 11 and player_cards[1].card_value == 11):
                player_cards[0].card_value == 1
                player_score -= 10
        
        print("PLAYER CARDS:  ")
        print_cards(player_cards, False)
        
        input() #pauses the game, until player press enter to prevent a quick fall through
        
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        dealer_score += dealer_card.card_value
        
        print("DEALER CARDS: ")
        if len(dealer_cards) == 1:
            print_cards(dealer_cards, False) 

        else: #hiding the second card and the score
            print_cards(dealer_cards[:-1], True)    
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
            print()
            print("PLAYER SCORE = ", player_score)
    
    
        if len(dealer_cards) == 2:
            if dealer_cards[0].card_value == 11 and dealer_cards[1].card_value == 11:
                dealer_cards[1].card_value = 1
                dealer_score -= 10
    
        input()

    if player_score == 21:
        print(f"BLACK JACK, YOU HAVE WON!!!")
        quit()
        
    
    while player_score < 21:
        choice = input("Enter H to hit or S to stand : ")
        print()
        if(len(choice) != 1 or (choice.upper() != 'H' and choice.upper() != 'S')):
            print("Invalid Inputs, try again")
            
        if choice.upper() == 'H':
        
            player_card = random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
            player_score += player_card.card_value
            
            c = 0 #keep track of aces and turn them into value 1 if player busts
            while player_score > 21 and c < len(player_cards):
                if player_cards[c].card_value == 11:
                    player_cards[c].card_value = 1
                    player_score -= 10
                    c += 1
                else:
                    c += 1 
                    
            clear()
            
            print("DEALER CARDS: ")
            print_cards(dealer_cards[:-1], True)
            print("DEALER SCORE = ", dealer_score - dealer_cards[-1].card_value)
    
            print()
    
            print("PLAYER CARDS: ")
            print_cards(player_cards, False)
            print("PLAYER SCORE = ", player_score)
        
        if choice.upper() == 'S':
            break
        
        
    if(player_score == 21):
        print("BLACKJACK, YOU HAVE WON")
        quit()
        
    if(player_score > 21):
        print(f"BUSTED!!! OVER 21. YOU HAVE {player_score} ")
        quit()

    
    while dealer_score < 17:
        clear()
        
        print("DEALER HAS DECIDED TO HIT...")
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
        
        dealer_score += dealer_card.card_value
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1
        
        print()
    
        print("DEALER CARDS: ")
        print_cards(dealer_cards, False)
        print("DEALER SCORE = ", dealer_score)
    
        input()
        
    if(dealer_score > 21):
        print("DEALER BUSTS!!! YOU WIN!!!")
        quit()
        
         
    if(dealer_score == 21):
        print("DEALER WINS!!! YOU LOST!!!")
        quit()
    
    if(dealer_score == player_score):
        print("DEALER IS REVEALING...")
        print_cards(dealer_cards, False)
        print("DEALER SCORE: ", dealer_score)
        print("IT'S A TIE!!! YOU BOTH HAVE ", dealer_score)
        quit()
        
    elif(player_score > dealer_score):
        print("DEALER IS REVEALING...")
        print_cards(dealer_cards, False)
        print("DEALER SCORE: ", dealer_score)
        print("YOU HAVE MORE THAN THE DEALER, YOU WON!!!")
        quit()
        
    else:
        print("DEALER IS REVEALING...")
        print_cards(dealer_cards, False)
        print("DEALER SCORE: ", dealer_score)
        print("THE DEALER HAS MORE THAN YOU, YOU LOST!!!")
        quit()



if __name__ == "__main__":
    
    clear()
    
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    myDeck = []

    for suit in suits:
        for card in cards:
            myDeck.append(Card(suits_values[suit], card , cards_values[card]))

    

    blackjack_game(myDeck)
    
            
        
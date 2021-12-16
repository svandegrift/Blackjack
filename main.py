from art import logo
import random
import os

def clear_console():
	os.system('clear')
clear_console()


def deal_card():
	"""Generate a new card"""
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	card = random.choice(cards)
	return card

def calculate_score(cards):
	"""Take a list of cards and return score"""
	if sum(cards) == 21 and len(cards) == 2:
		return 0
	elif 11 in cards and sum(cards) > 21:
		cards.remove(11)
		cards.append(1)
	return sum(cards)

def compare(your_score, dealer_score):	
	if your_score == dealer_score:
		return "It's a draw!"
	elif dealer_score == 0:
		return "Dealer has a Blackjack! You lose!"
	elif your_score == 0:
		return "You have a blackjack! You win!"
	elif your_score > 21:
		return "You went over! You lose!"
	elif dealer_score > 21:
		return 'Dealer went over! You win!'
	elif your_score > dealer_score:
		return 'You win!'
	elif dealer_score > your_score:
		return 'You lose!'

def play_game():
	print(logo)
	user_cards = []
	computer_cards = []
	is_game_over = False
	
	for _ in range(2):	
		user_cards.append(deal_card())
		computer_cards.append(deal_card())
	
	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)
		print(f'Your Cards: {user_cards}, Score: {user_score}')
		print(f'Computers First Card: {computer_cards[0]}')
		
		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True
		else:
			user_choice = input("type 'hit' or 'stay'")
			if user_choice == 'hit':
				user_cards.append(deal_card())
			else:
				is_game_over = True
	
	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)
		
	print(f'Your final hand: {user_cards}, Final Score: {user_score}')
	print(f'Computers final hand: {computer_cards}, Final score: {computer_score}')
	print(compare(user_score, computer_score))
	if input("want to play again? 'y' or 'n'") == 'y':
		clear_console()
		play_game()

play_game()	

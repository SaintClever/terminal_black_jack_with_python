#!/usr/bin/env python3

import random
from ascii_art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_hand = random.sample(cards, 2)[:2]
computer_hand = random.sample(cards, 3)[2:4]
print(f"The computer hand is {computer_hand}\nYour current hand is: {user_hand}")

def card_holder():
  # Deals cards for computer and user
	computer_hand.append(random.sample(cards, 2)[1])
	# print(f'computer current hand: {computer_hand}')
	user_input = input('Do you want to hit (y/n): ')

	if user_input == 'y':
		user_hand.append(random.sample(cards, 2)[0])
		# print(f"\nThe computer hand is {computer_hand} = {sum(computer_hand)}")
		print(f"\nYour current hand is: {user_hand} = {sum(user_hand)}")
		if sum(user_hand) > 21:
			print("It's a bust! You lose")
			return
		card_holder() # Apply recursion
	elif user_input == 'n':
		user_output = sum(user_hand)
		computer_output = sum(computer_hand)
		if user_output > computer_output and user_output <= 21:
			print(f"\nYou're the winner with a total of: {user_output}\nThe computer had: {computer_output}")
		elif computer_output > user_output and computer_output <= 21:
			print(f"\nYou lose! Computer wins with: {computer_output}")
		elif computer_output == user_output and computer_output > 21 or user_output > 21:
			print("It's a draw!")
		elif computer_output > 21 and user_output < 21:
			print(f"\nYou're the winner with a total of: {user_output}\nThe computer went over: {computer_output}")
		elif computer_output < 21 and user_output > 21:
			print(f"\nYou lose! with: {user_output}\nThe computer wins with: {computer_output}")
		elif user_output > 21:
			print("It's a bust! You lose")

card_holder()
"""
Intelligent Systems Group 5
Vadim Ojeg
Colette Wibaut
Pieter Hoppenbrouwers

"""
from api import State
from api import Deck
import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
		# type: (State) -> tuple[int, int]
		moves = state.moves()
		chosen_move = moves[0]
		opponent_card = state.get_opponents_played_card()
		moves_trump_suit = []

		me = state.whose_turn()
		phase = state.get_phase()

		if me == 1:	#if mybot is player 1, we play higher cards because we cant react to opponents plays
			if phase == 1:
				for index, move in enumerate(moves):
					if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
						moves_trump_suit.append(move)

				if len(moves_trump_suit) > 0:
					chosen_move = moves_trump_suit[0]
					return chosen_move

				# Get move with highest rank available, of any suit
				for index, move in enumerate(moves):
					if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
						chosen_move = move
			elif phase == 2:
				for index, move in enumerate(moves):
					if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
						moves_trump_suit.append(move)

				if len(moves_trump_suit) > 0:
					chosen_move = moves_trump_suit[0]
					return chosen_move

				# Get move with highest rank available, of any suit
				for index, move in enumerate(moves):
					if move[0] is not None and move[0] % 5 <= chosen_move[0] % 5:
						chosen_move = move
			return chosen_move
		elif me == 2:
			if phase == 1:
				#Get all trump suit moves available
				for index, move in enumerate(moves):

					if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
						moves_trump_suit.append(move)

				if len(moves_trump_suit) > 0:
					chosen_move = moves_trump_suit[len(moves_trump_suit) - 1]
					return chosen_move

				# If the opponent has played a card
				if state.get_opponents_played_card() is not None:

					moves_same_suit = []

					# Get all moves of the same suit as the opponent's played card (as long as they beat that card)
					for index, move in enumerate(moves):
						if move[0] is not None and Deck.get_suit(move[0]) == Deck.get_suit(state.get_opponents_played_card()) and Deck.get_rank(move[0]) > Deck.get_rank(opponent_card):
							moves_same_suit.append(move)
					# if there are any moves we can make of the opponents suit, pick the lowest that wins
					if len(moves_same_suit) > 0:
						chosen_move = moves_same_suit[len(moves_same_suit) - 1]
						return chosen_move

				# Get move with lowest rank available, of any suit. Throw away crap cards, basically
				for index, move in enumerate(moves):
					if move[0] is not None and move[0] % 5 >= chosen_move[0] % 5:
						chosen_move = move
			elif phase == 2:
				# Get all trump suit moves available
				for index, move in enumerate(moves):

					if move[0] is not None and Deck.get_suit(move[0]) == state.get_trump_suit():
						moves_trump_suit.append(move)

				if len(moves_trump_suit) > 0:
					chosen_move = moves_trump_suit[len(moves_trump_suit) - 1]
					return chosen_move

				# If the opponent has played a card
				if state.get_opponents_played_card() is not None:

					moves_same_suit = []

					# Get all moves of the same suit as the opponent's played card (as long as they beat that card)
					for index, move in enumerate(moves):
						if move[0] is not None and Deck.get_suit(move[0]) == Deck.get_suit(
								state.get_opponents_played_card()) and Deck.get_rank(move[0]) > Deck.get_rank(
								opponent_card):
							moves_same_suit.append(move)
					# if there are any moves we can make of the opponents suit, pick the lowest that wins
					if len(moves_same_suit) > 0:
						chosen_move = moves_same_suit[len(moves_same_suit) - 1]
						return chosen_move

				# Get move with lowest rank available, of any suit. Throw away crap cards, basically
				for index, move in enumerate(moves):
					if move[0] is not None and move[0] % 5 >= chosen_move[0] % 5:
						chosen_move = move
			return chosen_move

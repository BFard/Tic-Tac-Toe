import random
import copy
import sys

def play(mode, symbol):
	if mode not in ["human", "easy", "medium", "hard"]:
		print('\nError: The given mode does not exist. Try "human", "easy", "medium", or "hard".')
		exit()
	elif mode == "human":
		human_player = None
	else:
		if symbol == "X":
			human_player = 1
		elif symbol == "O":
			human_player = -1
		elif symbol is not None:
			print('\nError: Invalid symbol choice. Try "X" or "O".')
			exit()
		else:
			human_player = random.choice([-1, 1])

	print("\nWelcome to Tic-Tac-Toe.")
	print("To make a move, enter one of the following two-letter options.\n")
	print("UL - Upper Left")
	print("UM - Upper Middle")
	print("UR - Upper Right")
	print("ML - Middle Left")
	print("MM - Middle Middle")
	print("MR - Middle Right")
	print("LL - Lower Left")
	print("LM - Lower Middle")
	print("LR - Lower Right\n")
	input("Press Enter to start...")

	board = [[0, 0, 0] for _ in range(3)]
	move_num = 0
	player_map = {1: "X", -1: "O"}
	rand_probs = {"easy": 1, "medium": 0.5, "hard": 0}
	square_map = {"UL": (0, 0), "UM": (0, 1), "UR": (0, 2), \
				  "ML": (1, 0), "MM": (1, 1), "MR": (1, 2), \
				  "LL": (2, 0), "LM": (2, 1), "LR": (2, 2)}

	def get_winner(board_state):
		sums = [sum(board_state[0]), sum(board_state[1]), sum(board_state[2])]
		sums.append(board_state[0][0] + board_state[1][0] + board_state[2][0])
		sums.append(board_state[0][1] + board_state[1][1] + board_state[2][1])
		sums.append(board_state[0][2] + board_state[1][2] + board_state[2][2])
		sums.append(board_state[0][0] + board_state[1][1] + board_state[2][2])
		sums.append(board_state[0][2] + board_state[1][1] + board_state[2][0])
		if 3 in sums:
			return "X"
		elif -3 in sums:
			return "O"

	def print_board():
		layout = "\n"
		for i in range(len(board)):
			row = board[i]
			for j in range(len(row)):
				square = row[j]
				if square == 0:
					layout += "   "
				elif square == 1:
					layout += " X "
				else:
					layout += " O "
				if j < 2:
					layout += "|"
			if i < 2:
				layout += "\n-----------\n"
		print(layout + "\n")

	def move_random(player):
		while True:
			row = random.randint(0, 2)
			col = random.randint(0, 2)
			if board[row][col] == 0:
				board[row][col] = player
				break

	def value(board_state, player, moves_played, alpha, beta):
		winner = get_winner(board_state)
		if winner is None and moves_played == 9:
			return 0
		elif winner == "X":
			return 1
		elif winner == "O":
			return -1
		elif moves_played % 2 == 0:
			return max_value(board_state, player, moves_played, alpha, beta)
		else:
			return min_value(board_state, player, moves_played, alpha, beta)

	def max_value(board_state, player, moves_played, alpha, beta):
		max_val = -2
		for next_state in successors(board_state, player):
			max_val = max(max_val, value(next_state, -player, moves_played + 1, alpha, beta))
			if max_val >= beta:
				return max_val
			alpha = max(max_val, alpha)
		return max_val

	def min_value(board_state, player, moves_played, alpha, beta):
		min_val = 2
		for next_state in successors(board_state, player):
			min_val = min(min_val, value(next_state, -player, moves_played + 1, alpha, beta))
			if min_val <= alpha:
				return min_val
			beta = min(min_val, beta)
		return min_val

	def successors(board_state, player):
		successor_list = []
		for row in range(3):
			for col in range(3):
				if board_state[row][col] == 0:
					next_state = copy.deepcopy(board_state)
					next_state[row][col] = player
					successor_list.append(next_state)
		return successor_list

	def move_minimax(player):
		nonlocal board
		successor_list = successors(board, player)
		values = [value(s, -player, move_num + 1, -2, 2) for s in successor_list]
		if player == 1:
			max_val = max(values)
			options = [successor_list[i] for i in range(len(values)) if values[i] == max_val]
		else:
			min_val = min(values)
			options = [successor_list[i] for i in range(len(values)) if values[i] == min_val]
		board = random.choice(options)

	def get_move():
		if move_num % 2 == 0:
			player = 1
		else:
			player = -1
		if mode == "human" or player == human_player:
			while True:
				move = input("Please enter a move for Player " + player_map[player] + ": ")
				if move in square_map.keys():
					row, col = square_map[move]
					if board[row][col] == 0:
						board[row][col] = player
						break
				print("\nInvalid move entered.\n")
		else:
			print("The AI will make a move for Player " + player_map[player] + ".")
			roll = random.uniform(0, 1)
			if roll < rand_probs[mode]:
				move_random(player)
			else:
				move_minimax(player)

	while get_winner(board) is None and move_num < 9:
		print_board()
		get_move()
		move_num += 1

	print_board()
	winner = get_winner(board)
	if winner is None:
		print("The game is a draw.")
	else:
		print("Player " + winner + " wins.")
	print("Thanks for playing Tic-Tac-Toe.")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print('\nPlease enter a mode. Try "human", "easy", "medium", or "hard".')
	elif len(sys.argv) == 2:
		play(sys.argv[1], None)
	else:
		play(sys.argv[1], sys.argv[2])
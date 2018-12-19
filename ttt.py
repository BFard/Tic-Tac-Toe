import sys

def play(mode, symbol):
	if mode not in ["human", "easy", "medium", "hard"]:
		print('\nError: The given mode does not exist. Try "human", "easy", "medium", or "hard".')
		exit()

	print("\nWelcome to Tic Tac Toe.")
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
	square_map = {"UL": (0, 0), "UM": (0, 1), "UR": (0, 2), \
				  "ML": (1, 0), "MM": (1, 1), "MR": (1, 2), \
				  "LL": (2, 0), "LM": (2, 1), "LR": (2, 2)}

	def get_winner():
		sums = [sum(board[0]), sum(board[1]), sum(board[2])]
		sums.append(board[0][0] + board[1][0] + board[2][0])
		sums.append(board[0][1] + board[1][1] + board[2][1])
		sums.append(board[0][2] + board[1][2] + board[2][2])
		sums.append(board[0][0] + board[1][1] + board[2][2])
		sums.append(board[0][2] + board[1][1] + board[2][0])
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

	def get_move():
		if move_num % 2 == 0:
			player = 1
		else:
			player = -1
		while True:
			move = input("Please enter a move for Player " + player_map[player] + ": ")
			if move in square_map.keys():
				row, col = square_map[move]
				if board[row][col] == 0:
					board[row][col] = player
					break
			print("\nInvalid move entered.\n")

	while get_winner() is None and move_num < 9:
		print_board()
		get_move()
		move_num += 1

	print_board()
	winner = get_winner()
	if winner is None:
		print("The game is a draw.")
	else:
		print("Player " + winner + " wins.")
	print("Thanks for playing Tic Tac Toe.")

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print('\nPlease enter a mode. Try "human", "easy", "medium", or "hard".')
	elif len(sys.argv) == 2:
		play(sys.argv[1], None)
	else:
		play(sys.argv[1], sys.argv[2])
import random

# Board features
# x1 = number of black pieces
# x2 = number of red pieces
# x3 = number of black kings
# x4 = number of red kings
# x5 = number of red pieces threatened
# x6 = number of black pieces threatened
FEATURES = 6

#Generate a random board 
def create_board():
    return [random.randint(0, 3) for _ in range(FEATURES)]

#Calculate board value using weights
def board_value(board, weights):
    total = weights[0]  # bias term
    for i in range(FEATURES):
        total += weights[i+1] * board[i]
    return total

#Simulate a game
def play(board_weights, steps=5):
    boards = []
    board = create_board()
    for _ in range(steps):
        boards.append(board)
        board = create_board()  # simulate board change
    result = random.choice([100, 0, -100])  # win, draw, loss
    return boards, result

#Generate training examples
def training_data(boards, result, weights):
    data = []
    for board in reversed(boards):
        target = result
        result = board_value(board, weights)  # next board value
        data.append((board, target))
    return data

#Update weights using LMS rule 
def update(weights, data, alpha=0.01):
    for board, target in data:
        prediction = board_value(board, weights)
        error = target - prediction
        weights[0] += alpha * error  # update bias
        for i in range(FEATURES):
            weights[i+1] += alpha * error * board[i]  # update feature weights
    return weights

#Run multiple game experiments
def run_experiments(weights, games=10):
    all_data = []
    for _ in range(games):
        boards, result = play(weights)
        data = training_data(boards, result, weights)
        all_data.extend(data)
    return all_data

#Initialize weights 
weights = [0.0] * (FEATURES + 1)

#Training loop
for epoch in range(10):
    data = run_experiments(weights, games=5)
    weights = update(weights, data)
    print(f"Epoch {epoch+1} done")

#Print final learned weights
print("\nFinal weights:")
for i, w in enumerate(weights):
    print(f"w{i} = {w:.2f}")

#Test on a new random board
test_board = create_board()
print("\nTest board:", test_board)
print("Predicted value:", board_value(test_board, weights))

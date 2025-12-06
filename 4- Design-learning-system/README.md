# Checkers Learning System

## Project Overview

This project is a practical implementation of a **Checkers learning system**, demonstrating the core concepts of Machine Learning, including **Temporal Difference (TD) Learning** and **Least Mean Squares (LMS) weight updates**.  

It follows the **design steps for creating a learning system** from scratch.

### Core Components
- **Performance System:** Simulates games by generating random board states.
- **Critic:** Converts the game traces into training examples.
- **Generalizer:** Updates weights using the LMS algorithm.
- **Experiment Generator:** Runs multiple games to generate more training data.

### Features
The system uses **feature-based board evaluation**:
- `x1` → Number of black pieces
- `x2` → Number of red pieces
- `x3` → Number of black kings
- `x4` → Number of red kings
- `x5` → Number of red pieces threatened by black
- `x6` → Number of black pieces threatened by red

### Target Function
The target function `V(b)` represents how "good" a board state is:
- **Win** → 100
- **Draw** → 0
- **Loss** → -100

The system learns an **approximation of V** by adjusting weights for each feature.

---

## How It Works

1. **Generate Board:** The system starts with a random board state.
2. **Simulate Game:** It plays a sequence of moves (randomly) to simulate a game.
3. **Generate Training Examples:** Each board in the game trace is assigned a training value using TD learning.
4. **Update Weights:** LMS algorithm adjusts the weights to reduce the error between predicted and target board values.
5. **Repeat:** Multiple games are played to refine the weights.

---

## Folder Structure


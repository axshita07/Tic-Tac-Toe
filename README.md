# ❌ Tic-Tac-Toe CLI ⭕

A robust, interactive command-line implementation of the classic Tic-Tac-Toe game, written in Python. This project demonstrates clean functional programming, input validation, and game-state logic.

---

## 🕹️ Game Features
* **Intuitive Interface:** Uses a numbered grid (1-9) so players can easily identify their moves.
* **Smart Validation:** The engine detects if a spot is already taken or if the input is non-numeric, preventing crashes or cheating.
* **Automated Referee:** Built-in logic to instantly check for all 8 possible win conditions (horizontal, vertical, and diagonal).
* **Draw Detection:** Automatically identifies a "Cat's Game" when no moves remain and no winner is found.

---

## 🛠️ Technical Overview
The game is structured into modular functions for high readability and maintainability:
* `print_board(board)`: Dynamically renders the current state of the 3x3 grid.
* `check_win(board, player)`: Utilizes the `any()` function to evaluate win conditions efficiently.
* `get_player_move(board, player)`: A robust `while` loop that handles user error and keeps the game flowing.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.


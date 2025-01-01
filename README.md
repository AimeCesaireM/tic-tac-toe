# Tic-Tac-Toe Game

A simple, interactive console-based implementation of the classic Tic-Tac-Toe game in Python.

## Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [How to Play](#how-to-play)  
4. [Setup and Usage](#setup-and-usage)  
5. [Game Rules](#game-rules)  
6. [Technologies Used](#technologies-used)  
7. [Contributing](#contributing)  
8. [License](#license)  

## Overview

This project is a Python implementation of the Tic-Tac-Toe game. It supports two players taking turns to mark cells in a 3x3 grid, aiming to align three of their symbols (X or O) horizontally, vertically, or diagonally.

---

## Features

- **Interactive Gameplay**: Allows two players to compete turn by turn.  
- **Input Validation**: Ensures the player chooses a valid and unoccupied cell.  
- **Winner Detection**: Automatically detects and declares the winner or a tie.  
- **Clean Game Loop**: Simplifies game flow with clear functions for turns, winner checks, and player flipping.  

---

## How to Play

1. Players take turns selecting a position (1–9) to mark their symbol (X or O).  
2. The board positions are as follows:  
   ```
   1 | 2 | 3
   4 | 5 | 6
   7 | 8 | 9
   ```  
3. The game ends when:  
   - A player aligns three symbols horizontally, vertically, or diagonally (Winner).  
   - All cells are filled, but no alignment is achieved (Tie).  

---

## Setup and Usage

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Run the game:  
   ```bash
   python tic_tac_toe.py
   ```

---

## Game Rules

1. Players can only choose unoccupied cells.  
2. The game alternates between Player X and Player O.  
3. The first player to align three symbols wins.  

---

## Technologies Used

- **Language**: Python  
- **Frameworks**: None (pure Python implementation)

---

## Contributing

Contributions are welcome! If you'd like to improve the project or add features:  
1. Fork this repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```  
3. Commit your changes:  
   ```bash
   git commit -m "Added feature-name"
   ```  
4. Push to the branch:  
   ```bash
   git push origin feature-name
   ```  
5. Create a Pull Request.

---

## License

This project is licensed under the [MIT License](LICENSE).  

---

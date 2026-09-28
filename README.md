# Tic Tac Toe

> **Note:** The core game logic (`main.py`) was written by me. The Streamlit UI (`ui.py`) was built with the help of AI.

A two-player Tic Tac Toe game in Python with two front ends: a **terminal version** and a **web UI built with Streamlit**. Both share the same game logic.

## Features

- Play in the terminal or in the browser
- Input validation (out-of-range and already-taken cells are rejected)
- Win and draw detection
- Streamlit UI with a turn indicator, a scoreboard that persists across games, and New game / Reset scores buttons

## Project Structure

```
tictactoe-game/
├── main.py            # Game logic + terminal version
├── ui.py              # Streamlit web UI (imports logic from main.py)
├── requirements.txt   # Dependencies
└── README.md
```

## Requirements

- Python 3.10+
- [NumPy](https://numpy.org/)
- [Streamlit](https://streamlit.io/)

## Installation

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage

**Terminal version**

```bash
python main.py
```

Enter a row and column (0–2) when prompted. X goes first.

**Web UI**

```bash
streamlit run ui.py
```

Then open the local URL shown in your terminal (usually http://localhost:8501) and click a cell to play.

## How It Works

The board is a 3×3 NumPy array: `0` is empty, `1` is X and `-1` is O. A player wins when any row, column or diagonal sums to `3` (X) or `-3` (O). If the board is full with no winner, the game is a draw.

`ui.py` imports `check_winner` from `main.py`, so the winning logic exists in only one place. The `if __name__ == "__main__":` guard in `main.py` stops the terminal game from starting when it is imported.

## Limitations

- Two players on the same device only (no online multiplayer)
- No computer opponent yet


## Credits

- **Game logic and terminal version (`main.py`):** written by me.
- **Web UI (`ui.py`):** built with the help of AI (Claude by Anthropic), since I was learning Streamlit.

from main import check_winner

import numpy as np
import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

SYMBOLS = {0: "\u00A0", 1: "X", -1: "O"}  # non-breaking space keeps empty buttons the same size

# Sizes the grid buttons and keeps X/O readable when a cell is disabled
st.markdown(
    """
    <style>
    div[data-testid="stButton"] > button {
        width: 100%;
        height: 5.5rem;
        font-size: 2.5rem;
        font-weight: 700;
    }
    div[data-testid="stButton"] > button:disabled { opacity: 1; }
    </style>
    """,
    unsafe_allow_html=True,
)


def new_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1  # 1 = X, -1 = O
    st.session_state.result = None


def reset_scores():
    st.session_state.scores = {"X": 0, "O": 0, "DRAW": 0}
    new_game()


def play(row, col):
    """Button callback: runs before the rerun, so scores update exactly once."""
    s = st.session_state
    if s.result is not None or s.board[row, col] != 0:
        return

    s.board[row, col] = s.current
    result = check_winner(s.board)

    if result is not None:
        s.result = result
        s.scores[result] += 1
    else:
        s.current = -s.current


if "board" not in st.session_state:
    reset_scores()

s = st.session_state

st.title("Tic Tac Toe")

# Scoreboard
c1, c2, c3 = st.columns(3)
c1.metric("X wins", s.scores["X"])
c2.metric("Draws", s.scores["DRAW"])
c3.metric("O wins", s.scores["O"])

# Status line
if s.result == "DRAW":
    st.info("It's a draw!")
elif s.result is not None:
    st.success(f"{s.result} wins!")
else:
    st.subheader(f"Turn: {'X' if s.current == 1 else 'O'}")

# Board (centered)
_, mid, _ = st.columns([1, 3, 1])
with mid:
    for r in range(3):
        cols = st.columns(3)
        for c in range(3):
            cols[c].button(
                SYMBOLS[int(s.board[r, c])],
                key=f"cell_{r}_{c}",
                on_click=play,
                args=(r, c),
                disabled=s.board[r, c] != 0 or s.result is not None,
            )

# Controls
b1, b2 = st.columns(2)
b1.button("New game", on_click=new_game, type="primary")
b2.button("Reset scores", on_click=reset_scores)
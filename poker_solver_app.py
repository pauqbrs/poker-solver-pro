import streamlit as st
from equity_calculator import monte_carlo_equity
from utils import parse_cards

st.title("Poker Solver Pro (Equity vs Rangos)")

hero_input = st.text_input("Cartas del héroe (ej: Ah,Kd)", "Ah,Kd")
villain_input = st.text_input("Cartas del villano o rango (ej: Qs,Qd o JJ+,AQ+)", "Qs,Qd")
board_input = st.text_input("Board parcial (ej: 2c,5h,9s)", "2c,5h,9s")
iters = st.slider("Número de simulaciones Monte Carlo", 1000, 20000, 5000, 1000)

if st.button("Calcular Equity"):
    try:
        hero = parse_cards(hero_input)
        board = parse_cards(board_input)
        villain = parse_cards(villain_input, allow_ranges=True)
        equity, ties = monte_carlo_equity(hero, villain, board, iters)
        st.success(f"Equity del héroe: {equity:.2%}")
        st.info(f"Empates: {ties:.2%}")
        st.error(f"Equity del villano: {(1 - equity - ties):.2%}")
    except Exception as e:
        st.error(f"Error: {e}")
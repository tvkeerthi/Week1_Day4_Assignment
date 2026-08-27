# streamlit_grade_system.py

import streamlit as st

def get_grade(mark):
    """Convert a mark into a letter grade based on the fixed scale."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


st.title("Student Grade System")

mark = st.number_input("Enter a mark (0-100):", min_value=0, max_value=100, step=1)

if st.button("Get Grade"):
    grade = get_grade(mark)
    st.success(f"Mark: {mark} -> Grade: {grade}")
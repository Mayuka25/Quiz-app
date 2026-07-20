import streamlit as st
from questions import questions

st.title("Quiz App")

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.finished = False

def check_answer(selected_letter, correct_letter):
    if selected_letter == correct_letter:
        st.session_state.score += 1
    st.session_state.q_index += 1

if not st.session_state.finished and st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {q['question']}")

    for option in q['options']:
        letter = option[0]
        if st.button(option, key=option + str(st.session_state.q_index)):
            check_answer(letter, q['answer'])
            st.rerun()

elif st.session_state.q_index >= len(questions):
    st.session_state.finished = True
    percentage = (st.session_state.score / len(questions)) * 100
    result = "Pass" if percentage >= 50 else "Fail"
    st.success(f"Quiz Finished! Score: {st.session_state.score}/{len(questions)} ({percentage:.1f}%) — {result}")
    if st.button("Restart"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()
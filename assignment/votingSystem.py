import streamlit as st
import matplotlib.pyplot as plt

st.title("Voting App")

cols = st.columns(2)

candidates = ["Cat", "Dog"]
if "votes" not in st.session_state:
    st.session_state.votes = [0, 0]

with cols[0]:
    st.header("A cat")
    if st.button("Vote cat"):
        st.session_state.votes[0] += 1

with cols[1]:
    st.header("A dog")
    if st.button("Vote dog"):
        st.session_state.votes[1] += 1

st.write(f"Cat: {st.session_state.votes[0]}, Dog: {st.session_state.votes[1]}")

fig, ax = plt.subplots()
ax.bar(candidates, st.session_state.votes)
st.pyplot(fig)




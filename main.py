import streamlit as st

from crew import crew_start

st.title("You personalized Blog Page Editor")

with st.form("my_form"):
    text = st.text_area("Enter the topic:")
    submitted = st.form_submit_button("Submit")
    if submitted:

        with st.spinner("Wait for it..."):
            result = crew_start(text)

        st.success("Done!")
        st.markdown(result)

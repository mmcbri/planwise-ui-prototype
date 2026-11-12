
import streamlit as st

st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="centered"
)

# Keep track of which screen the user is viewing
if "started" not in st.session_state:
    st.session_state.started = False

# Welcome screen
if not st.session_state.started:
    st.title("Welcome to PlanWise")
    st.subheader("A Guided Medicare Part D Plan Advisor")

    st.write(
        """
        Choosing a Medicare Part D prescription drug plan
        can be confusing.

        PlanWise helps you compare plans based on your
        medications, pharmacy preferences, and estimated costs.
        """
    )

    st.divider()

    st.header("Let's find a plan that fits your needs")

    st.write(
        "Answer a few questions to get a personalized "
        "comparison of available plans."
    )

    if st.button("Get Started"):
        st.session_state.started = True
        st.rerun()

# Intake screen
else:
    st.title("Let's get to know your needs")

    st.write(
        "First, we'll ask a few questions to understand "
        "your prescription drug coverage needs."
    )

    st.info("Your personalized intake questions will appear here.")

    if st.button("Back to Welcome Page"):
        st.session_state.started = False
        st.rerun()

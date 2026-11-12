import streamlit as st

# Set up the browser tab and page layout
st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="centered"
)

# Main page content
st.title("Welcome to PlanWise")
st.subheader("A Guided Medicare Part D Plan Advisor")

st.write(
    """
    Choosing a Medicare Part D prescription drug plan can be confusing.
    PlanWise helps you compare plans based on your medications,
    pharmacy preferences, and estimated costs.
    """
)

st.divider()

st.header("Let's find a plan that fits your needs")

st.write(
    "Answer a few questions about your medications and preferences "
    "to get a personalized comparison of available plans."
)

st.button("Get Started")

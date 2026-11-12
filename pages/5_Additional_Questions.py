
import streamlit as st

st.title("A few follow-up questions")

st.write(
    "Based on your answers, PlanWise may ask a few additional questions "
    "to better understand your coverage needs."
)

st.divider()

st.info(
    "Additional questions will appear here when they are relevant to "
    "your medications, pharmacy preferences, or plan priorities."
)

st.write(
    "You won't need to answer questions that don't apply to your situation."
)

st.divider()

back_col, continue_col = st.columns([1, 3])

with back_col:
    if st.button("Back"):
        st.switch_page("pages/4_Plan_Preferences.py")

with continue_col:
    if st.button("Continue to recommendations", use_container_width=True):
        st.switch_page("pages/6_Recommendations.py")

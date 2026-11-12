
import streamlit as st

st.title("A little about you")
st.write("Let's start with a few questions to help us find plans available in your area.")

st.divider()

# ZIP Code
st.subheader("Where do you live?")

zip_code = st.text_input(
    "ZIP code",
    max_chars=5,
    placeholder="Enter your 5-digit ZIP code",
    help="We'll use this to identify Medicare Part D plans available in your area."
)

# Medicare Assistance
st.divider()

st.subheader("Do you currently receive any of the following assistance?")

st.write(
    "Some assistance programs can help lower your Medicare prescription drug costs."
)

assistance_options = [
    "Medicaid",
    "Supplemental Security Income (SSI)",
    "Medicare Savings Program",
    "Extra Help (Low-Income Subsidy)",
    "I don't receive any of these"
]

assistance = st.radio(
    "Select one option",
    assistance_options,
    index=None
)

# Part D Experience
st.divider()

st.subheader("Medicare Part D experience")

part_d_experience = st.radio(
    "Is this your first time enrolling in a Medicare Part D prescription drug plan?",
    ["Yes", "No", "I'm not sure"],
    index=None
)

st.divider()

# Continue Button
if st.button("Continue to medications", use_container_width=True):

    if len(zip_code) != 5 or not zip_code.isdigit():
        st.error("Please enter a valid 5-digit ZIP code.")

    elif assistance is None:
        st.error("Please select an assistance option.")

    elif part_d_experience is None:
        st.error("Please answer the Medicare Part D question.")

    else:
        st.session_state.zip_code = zip_code
        st.session_state.assistance = assistance
        st.session_state.part_d_experience = part_d_experience

        st.switch_page("pages/2_Medications.py")

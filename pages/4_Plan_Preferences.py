
import streamlit as st

st.title("What matters most to you?")
st.write(
    "A few more questions will help us understand what you value "
    "when choosing a prescription drug plan."
)

st.divider()

# Generic medications
st.subheader("Generic medications")

generic_preference = st.radio(
    "Would you be willing to use a generic version of a medication "
    "if it could lower your costs?",
    ["Yes", "No", "It depends on the medication"],
    index=None
)

st.divider()

# Medication changes
st.subheader("Looking ahead")

expect_new_meds = st.radio(
    "Do you expect to start taking any new prescription medications "
    "in the next year?",
    ["Yes", "No", "I'm not sure"],
    index=None
)

new_med_category = ""

if expect_new_meds == "Yes":
    new_med_category = st.text_input(
        "If you know, what medication or type of medication might you start?",
        placeholder="You can provide a medication name or general category."
    )

st.divider()

# Cost preferences
st.subheader("Your cost preferences")

cost_preference = st.radio(
    "Which would you prioritize when choosing a plan?",
    [
        "The lowest estimated total annual cost",
        "More predictable costs throughout the year",
        "A balance between cost and predictability",
        "I'm not sure"
    ],
    index=None
)

st.divider()

# Navigation
back_col, continue_col = st.columns([1, 3])

with back_col:
    if st.button("Back"):
        st.switch_page("pages/3_Pharmacy.py")

with continue_col:
    if st.button("Continue", use_container_width=True):

        if generic_preference is None:
            st.error("Please answer the generic medication question.")

        elif expect_new_meds is None:
            st.error("Please answer whether you expect to start new medications.")

        elif cost_preference is None:
            st.error("Please select a cost preference.")

        else:
            st.session_state.generic_preference = generic_preference
            st.session_state.expect_new_meds = expect_new_meds
            st.session_state.new_med_category = new_med_category
            st.session_state.cost_preference = cost_preference

            st.switch_page("pages/5_Additional_Questions.py")

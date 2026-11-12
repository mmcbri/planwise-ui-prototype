
import streamlit as st

st.title("Your pharmacy preferences")
st.write(
    "Your preferred pharmacy can affect which plans offer you the best coverage "
    "and prescription costs."
)

st.divider()

# Preferred pharmacy
st.subheader("Preferred pharmacy")

st.write("Where do you typically fill your prescriptions?")

pharmacy = st.text_input(
    "Pharmacy name",
    placeholder="e.g., CVS, Walgreens, or a local pharmacy"
)

no_preference = st.checkbox(
    "I don't have a preferred pharmacy."
)

st.divider()

# Willingness to switch pharmacies
st.subheader("Would you consider using a different pharmacy?")

switch_pharmacy = st.radio(
    "Some plans offer lower prescription costs at certain preferred pharmacies.",
    ["Yes", "No", "I'm not sure"],
    index=None
)

st.divider()

# Mail order
st.subheader("Would you consider using a mail-order pharmacy?")

mail_order = st.radio(
    "Mail-order pharmacies may offer convenient home delivery and lower costs for some medications.",
    ["Yes", "No", "I'm not sure"],
    index=None
)

st.divider()

# Navigation
back_col, continue_col = st.columns([1, 3])

with back_col:
    if st.button("Back"):
        st.switch_page("pages/2_Medications.py")

with continue_col:
    if st.button("Continue", use_container_width=True):

        if not pharmacy.strip() and not no_preference:
            st.error("Please enter a pharmacy or select that you don't have a preference.")

        elif switch_pharmacy is None:
            st.error("Please answer whether you would consider a different pharmacy.")

        elif mail_order is None:
            st.error("Please answer whether you would consider mail order.")

        else:
            st.session_state.pharmacy = (
                "No preference" if no_preference else pharmacy.strip()
            )
            st.session_state.no_pharmacy_preference = no_preference
            st.session_state.switch_pharmacy = switch_pharmacy
            st.session_state.mail_order = mail_order

            st.switch_page("pages/4_Plan_Preferences.py")

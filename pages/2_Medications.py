
import streamlit as st

st.title("Your medications")
st.write(
    "Tell us about the prescription medications you currently take. "
    "This helps us estimate your prescription costs under different plans."
)

st.divider()

# Initialize medication list
if "medications" not in st.session_state:
    st.session_state.medications = []

if "no_medications" not in st.session_state:
    st.session_state.no_medications = False


# No medications option
no_medications = st.checkbox(
    "I don't currently take any prescription medications.",
    key="no_medications"
)

if no_medications:
    st.info("No problem! You can continue without adding medications.")

else:
    # Medication entry form
    st.subheader("Add a medication")

    with st.form("medication_form", clear_on_submit=True):

        medication_name = st.text_input(
            "Medication name",
            placeholder="e.g., Lisinopril"
        )

        dosage = st.text_input(
            "Strength / dosage",
            placeholder="e.g., 10 mg"
        )

        frequency = st.selectbox(
            "How often do you take it?",
            [
                "Once daily",
                "Twice daily",
                "Three times daily",
                "Four times daily",
                "As needed",
                "Other"
            ]
        )

        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Quantity per refill",
                min_value=0,
                step=1,
                value=30
            )

        with col2:
            quantity_unit = st.selectbox(
                "Quantity unit",
                ["tablets", "capsules", "mL", "inhalers", "patches", "other"]
            )

        days_supply = st.selectbox(
            "How many days does each refill typically last?",
            ["30 days", "60 days", "90 days", "Other"]
        )

        submitted = st.form_submit_button(
            "Add medication",
            use_container_width=True
        )

        if submitted:
            if not medication_name.strip():
                st.error("Please enter a medication name.")
            elif not dosage.strip():
                st.error("Please enter the medication strength or dosage.")
            else:
                st.session_state.medications.append({
                    "name": medication_name.strip(),
                    "dosage": dosage.strip(),
                    "frequency": frequency,
                    "quantity": quantity,
                    "quantity_unit": quantity_unit,
                    "days_supply": days_supply
                })
                st.rerun()


# Display medication list
st.divider()
st.subheader("Your medication list")

if st.session_state.medications:
    st.caption(f"{len(st.session_state.medications)} medication(s) added")

    medication_columns = st.columns(2, gap="medium")

    for i, med in enumerate(st.session_state.medications):
        with medication_columns[i % 2]:
            with st.container(border=True):

                name_col, remove_col = st.columns([4, 1])

                with name_col:
                    st.markdown(f"**{i + 1}. {med['name']}**")

                with remove_col:
                    if st.button("Remove", key=f"remove_{i}"):
                        st.session_state.medications.pop(i)
                        st.rerun()

                quantity_display = (
                    f"{med['quantity']} {med['quantity_unit']}"
                    if med.get("quantity")
                    else "Quantity not provided"
                )

                st.caption(f"{med['dosage']} · {med['frequency']}")
                st.caption(f"{quantity_display} · {med['days_supply']}")

elif not st.session_state.no_medications:
    st.caption("No medications added yet.")


# Navigation
st.divider()

if st.button("Back", use_container_width=False):
    st.switch_page("pages/1_About_You.py")

if st.button("Continue", use_container_width=True):

    if not st.session_state.medications and not st.session_state.no_medications:
        st.error("Please add at least one medication or select the option indicating you don't take any.")

    else:
        st.switch_page("app.py")

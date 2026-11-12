
import streamlit as st

st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="centered"
)

if "started" not in st.session_state:
    st.session_state.started = False

if "medications" not in st.session_state:
    st.session_state.medications = []

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

    st.divider()
    st.subheader("A little about you")

    zip_code = st.text_input(
        "What is your ZIP code?",
        max_chars=5,
        placeholder="e.g., 48104"
    )

    pharmacy = st.text_input(
        "Which pharmacy do you usually use?",
        placeholder="e.g., CVS, Walgreens, or a local pharmacy"
    )

    pharmacy_importance = st.radio(
        "How important is it to keep using this pharmacy?",
        [
            "Very important — I don't want to switch",
            "Somewhat important — I'd consider alternatives",
            "Not important — I'm open to switching"
        ]
    )

    st.divider()

    # Medication section
    st.header("Your medications")

    st.write(
        "Let's make sure we consider the prescriptions "
        "you currently take."
    )

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
                "As needed",
                "Other"
            ]
        )

        add_medication = st.form_submit_button(
            "Add medication"
        )

        if add_medication:
            if medication_name and dosage:
                st.session_state.medications.append({
                    "name": medication_name,
                    "dosage": dosage,
                    "frequency": frequency
                })
                st.success(f"{medication_name} added!")
            else:
                st.error("Please enter a medication name and dosage.")

    # Display entered medications
    if st.session_state.medications:
        st.subheader("Your medication list")

        for i, med in enumerate(st.session_state.medications):
            st.write(
                f"**{i + 1}. {med['name']}** — "
                f"{med['dosage']}, {med['frequency']}"
            )

    st.divider()

    if st.button("Continue"):
        if len(zip_code) != 5 or not zip_code.isdigit():
            st.error("Please enter a valid 5-digit ZIP code.")
        elif not pharmacy:
            st.error("Please enter your preferred pharmacy.")
        elif not st.session_state.medications:
            st.error("Please add at least one medication.")
        else:
            st.success("Your information has been recorded!")

    if st.button("Back to Welcome Page"):
        st.session_state.started = False
        st.rerun()


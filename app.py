
import streamlit as st

st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="wide"
)

# Initialize session state
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

    st.divider()

    # About you
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
        """
        Please enter each prescription medication you currently take.
        You'll add them to your list one at a time.
        """
    )
    
    no_medications = st.checkbox(
        "I don't currently take any prescription medications."
    )
    
    if no_medications:
        st.session_state.medications = []
        st.info("That's okay! You can continue without entering medications.")
    
    else:
        # Two-column layout
        left_column, right_column = st.columns([1, 1.3], gap="large")
    
        # LEFT: Medication entry form
        with left_column:
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
                        "As needed",
                        "Other"
                    ]
                )
    
                quantity = st.text_input(
                    "How many pills or units do you receive?",
                    placeholder="e.g., 30 tablets"
                )
    
                days_supply = st.selectbox(
                    "How long does this prescription last?",
                    [
                        "30 days",
                        "60 days",
                        "90 days",
                        "Other",
                        "I'm not sure"
                    ]
                )
    
                add_medication = st.form_submit_button(
                    "+ Add medication to my list",
                    use_container_width=True
                )
    
                if add_medication:
                    if medication_name.strip() and dosage.strip():
                        st.session_state.medications.append({
                            "name": medication_name.strip(),
                            "dosage": dosage.strip(),
                            "frequency": frequency,
                            "quantity": quantity.strip(),
                            "days_supply": days_supply
                        })
    
                        st.success(
                            f"{medication_name.strip()} added!"
                        )
                    else:
                        st.error(
                            "Please enter the medication name and dosage."
                        )
    
        # RIGHT: Medication list
        with right_column:
            st.subheader("Your medication list")
    
            count = len(st.session_state.medications)
    
            st.caption(f"{count} medication(s) added")
    
            if st.session_state.medications:

                for i, med in enumerate(st.session_state.medications):

                    with st.container(border=True):
            
                        # Medication name and remove button on one row
                        name_col, remove_col = st.columns([5, 1])
            
                        with name_col:
                            st.markdown(
                                f"**{i + 1}. {med['name']}**"
                            )
            
                        with remove_col:
                            if st.button(
                                "Remove",
                                key=f"remove_{i}"
                            ):
                                st.session_state.medications.pop(i)
                                st.rerun()
            
                        # Medication details underneath
                        st.caption(
                            f"{med['dosage']} · {med['frequency']} · "
                            f"{med['quantity'] or 'Quantity not provided'} · "
                            f"{med['days_supply']}"
                        )
    
            else:
                st.info(
                    "Your medications will appear here as you add them."
                )
    
    st.divider()
    
    st.write(
        "**Finished entering your medications?** "
        "Select Continue when your list is complete."
    )

    if st.button("Continue"):
        if len(zip_code) != 5 or not zip_code.isdigit():
            st.error("Please enter a valid 5-digit ZIP code.")
        elif not pharmacy.strip():
            st.error("Please enter your preferred pharmacy.")
        elif (
            not no_medications
            and not st.session_state.medications
        ):
            st.error(
                "Please add at least one medication or select "
                "'I don't currently take any prescription medications.'"
            )
        else:
            st.success("Your information has been recorded!")

    if st.button("Back to Welcome Page"):
        st.session_state.started = False
        st.rerun()

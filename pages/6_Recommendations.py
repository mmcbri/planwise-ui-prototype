
import streamlit as st

st.title("Your PlanWise recommendations")


st.write(
    "We've compared available Medicare Part D plans based on "
    "your medications, pharmacy preferences, and priorities."
)

# Temporary intake review for testing
with st.expander("Review your intake answers (testing)"):

    st.subheader("About you")

    st.write(f"**ZIP code:** {st.session_state.get('zip_code', 'Not provided')}")
    st.write(f"**Medicare assistance:** {st.session_state.get('assistance', 'Not provided')}")
    st.write(f"**First Part D enrollment:** {st.session_state.get('part_d_experience', 'Not provided')}")

    st.divider()

    st.subheader("Medications")

    if st.session_state.get("no_medications", False):
        st.write("No current prescription medications.")
    else:
        medications = st.session_state.get("medications", [])

        if medications:
            for med in medications:
                st.write(
                    f"**{med['name']}** — {med['dosage']}, "
                    f"{med['frequency']}, {med['quantity']} "
                    f"{med['quantity_unit']}, {med['days_supply']}"
                )
        else:
            st.write("No medications entered.")

    st.divider()

    st.subheader("Pharmacy preferences")

    st.write(f"**Preferred pharmacy:** {st.session_state.get('pharmacy', 'Not provided')}")
    st.write(f"**Willing to switch pharmacies:** {st.session_state.get('switch_pharmacy', 'Not provided')}")
    st.write(f"**Willing to use mail order:** {st.session_state.get('mail_order', 'Not provided')}")

    st.divider()

    st.subheader("Plan preferences")

    st.write(f"**Generic medications:** {st.session_state.get('generic_preference', 'Not provided')}")
    st.write(f"**Expecting new medications:** {st.session_state.get('expect_new_meds', 'Not provided')}")
    st.write(f"**Potential new medication:** {st.session_state.get('new_med_category', 'Not provided')}")
    st.write(f"**Cost priority:** {st.session_state.get('cost_preference', 'Not provided')}")

st.divider()


# Recommended plan
st.header("Your recommended plan")

st.info(
    "Your best-fit plan will appear here. PlanWise will explain "
    "why this plan was selected based on your answers."
)

# Estimated costs
st.subheader("Understanding your estimated costs")

cost_col1, cost_col2, cost_col3 = st.columns(3)

with cost_col1:
    st.metric("Monthly premium", "—")

with cost_col2:
    st.metric("Estimated annual medication cost", "—")

with cost_col3:
    st.metric("Estimated annual total", "—")

st.caption(
    "Cost estimates will be calculated using your medication list "
    "and available plan information. Actual costs may vary."
)

st.divider()

# Why this plan?
st.header("Why this plan may be a good fit")

st.write("Your recommendation will explain:")

st.markdown(
    """
    - How well the plan covers your medications
    - Whether your preferred pharmacy is in the plan's network
    - How the plan aligns with your cost preferences
    - Any restrictions or potential coverage concerns
    """
)

st.divider()

# Alternative plans
st.header("Other plans to consider")

st.write(
    "We'll also show alternative plans so you can compare "
    "their costs, coverage, and tradeoffs."
)

st.info("Alternative plan comparisons will appear here.")

st.divider()

# Important reminders
st.header("Before choosing a plan")

st.write(
    "Remember to verify medication coverage, pharmacy participation, "
    "and current plan details before enrolling."
)

st.caption(
    "PlanWise is an educational comparison tool and does not enroll "
    "you in a Medicare plan."
)

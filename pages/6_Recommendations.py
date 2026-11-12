
import streamlit as st

st.title("Your PlanWise recommendations")

st.write(
    "We've compared available Medicare Part D plans based on "
    "your medications, pharmacy preferences, and priorities."
)

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

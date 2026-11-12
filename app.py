
import streamlit as st

st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state
if "started" not in st.session_state:
    st.session_state.started = False

if "medications" not in st.session_state:
    st.session_state.medications = []

if "zip_code" not in st.session_state:
    st.session_state.zip_code = ""

if "pharmacy" not in st.session_state:
    st.session_state.pharmacy = ""


# Welcome page
def welcome_page():
    st.title("Welcome to PlanWise")
    st.subheader("A Guided Medicare Part D Plan Advisor")

    st.write("""
    Choosing a Medicare Part D plan can feel overwhelming.
    PlanWise helps you compare available prescription drug plans
    based on your medications, pharmacy preferences, and coverage needs.
    """)

    st.divider()

    st.header("Let's find a plan that fits your needs")
    st.write("Answer a few questions to get a personalized comparison of available plans.")

    if st.button("Get Started", use_container_width=True):
        st.session_state.started = True
        st.switch_page("pages/1_About_You.py")


# Register all pages here
welcome = st.Page(welcome_page, title="Welcome", default=True)
about_you = st.Page("pages/1_About_You.py", title="A little about you")
medications = st.Page("pages/2_Medications.py", title="Your medications")
pharmacy = st.Page("pages/3_Pharmacy.py", title="Pharmacy preferences")
plan_preferences = st.Page("pages/4_Plan_Preferences.py", title="Plan preferences")
additional_questions = st.Page("pages/5_Additional_Questions.py", title="Additional questions")
recommendations = st.Page("pages/6_Recommendations.py", title="Your recommendations")

# Set up navigation
page = st.navigation(
    [welcome, about_you, medications, pharmacy, plan_preferences, additional_questions, recommendations],
    position="hidden"
)

# Run the selected page
page.run()

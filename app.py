
import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="PlanWise",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# INITIALIZE SESSION STATE
# --------------------------------------------------

if "started" not in st.session_state:
    st.session_state.started = False

if "medications" not in st.session_state:
    st.session_state.medications = []

if "zip_code" not in st.session_state:
    st.session_state.zip_code = ""

if "pharmacy" not in st.session_state:
    st.session_state.pharmacy = ""

# --------------------------------------------------
# WELCOME PAGE
# --------------------------------------------------

def welcome_page():

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

    if st.button("Get Started", use_container_width=True):
        st.session_state.started = True
        st.switch_page("pages/1_About_You.py")


# --------------------------------------------------
# PAGE NAVIGATION
# --------------------------------------------------

if st.session_state.started:

    page = st.navigation(
        [
            st.Page(
                "pages/1_About_You.py",
                title="A little about you",
                default=True
            )
        ],
        position="hidden"
    )

else:

    page = st.Page(
        welcome_page,
        title="Welcome",
        default=True
    )

    page = st.navigation(
        [page],
        position="hidden"
    )

page.run()

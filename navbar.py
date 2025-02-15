import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Display different pages based on selection
if page == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the Home Page!")

elif page == "About":
    st.title("ℹ️ About Page")
    st.write("This is the About section.")

elif page == "Contact":
    st.title("📞 Contact Page")
    st.write("Reach out via email at example@example.com")

import streamlit as st

def markup(): 
    st.markdown(
        """
        <p>Hello World</p>        
        """,
        unsafe_allow_html=True  # Enable HTML rendering (if needed)
    )

def show():
    st.title("ℹ️ About Page")
    st.write("Reach out via email at example@example.com")
    markup()  # Now it's defined before being called

import streamlit as st

def navbar(): 
    st.markdown(
        """
        <style> 
            .navbar {
                background-color: 262730; 
                padding: 15px; 
                border-radius: 10px; 
                text-align: center; 
            }
            .navbar a {
                color: white; 
                text-decoration: none; 
                margin: 0 10px; 
                padding: 10px 15px; 
                font-size: 18px; 
                margin: 5px; 
                border-radius: 5px; 
            }
            .navbar a: hover {
                background-color: white;
                color: white   
            }
        </style>
        """, 
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <div class="navbar">
            <a href="?page=Happiness">😊 Happiness</a>
            <a href="?page=History">📖 History</a>
            <a href="?page=About">ℹ️ About</a>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Sidebar navigation as a fallback
    return st.sidebar.radio("Go to", ["Happiness", "History", "About"])
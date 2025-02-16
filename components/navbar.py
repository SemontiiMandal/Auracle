import streamlit as st

def navbar():
    # Track the selected page
    selected_page = st.sidebar.radio("Go to", ["Happiness", "History", "Account", "About"])

    # Styling with highlight effect
    st.markdown(
        f"""
        <style> 
            .navbar {{
                background-color: #262730; 
                padding: 15px; 
                border-radius: 10px; 
                text-align: center; 
            }}
            .navbar span {{
                color: white; 
                text-decoration: none; 
                margin: 0 10px; 
                padding: 10px 15px; 
                font-size: 18px; 
                margin: 5px; 
                border-radius: 5px; 
                transition: transform 0.3s ease, background-color 0.3s ease;
            }}
            .navbar .selected {{
                background-color: #FF6F61;
                color: white;
                transform: scale(1.1);
            }}
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Render the navbar with dynamic class for the selected span
    st.markdown(
        f"""
        <div class="navbar">
            <span class="{'selected' if selected_page == 'Happiness' else ''}">😊 Happiness</span>
            <span class="{'selected' if selected_page == 'History' else ''}">📖 History</span>
            <span class="{'selected' if selected_page == 'About' else ''}">ℹ️ About</span>
            <span class="{'selected' if selected_page == 'Account' else ''}">👤 Account</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

    return selected_page

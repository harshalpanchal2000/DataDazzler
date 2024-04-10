import streamlit as st
from preprocessing import preprocess_data
from modeling import modeling_tab

def main():
    st.title("🔮 DataDazzler: Your Automated EDA and Model Builder 🔮")
    st.sidebar.title("Navigation")

    page = st.sidebar.radio("Go to", ["Upload Data", "Preprocessing", "Modeling", "Download Model"])

    if page == "Upload Data":
        st.subheader("Upload Data")
        # Your upload data functionality here

    elif page == "Preprocessing":
        st.subheader("Preprocessing")
        # Your preprocessing functionality here

    elif page == "Modeling":
        st.subheader("Modeling")
        # Your modeling functionality here
        modeling_tab()

    elif page == "Download Model":
        st.subheader("Download Model")
        # Your download model functionality here

if __name__ == "__main__":
    main()

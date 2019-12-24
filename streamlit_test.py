import streamlit as st


def main():
    st.sidebar.selectbox("Choose a page", ["Homepage", "Exploration"])
    st.header('Test Page')


if __name__ == "__main__":
    main()
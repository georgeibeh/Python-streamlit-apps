import streamlit as st
from PIL import Image
import sqlite3


def main():

    html_temp = """
	<div style=background-color:{};padding:10px;border-radius:10px">
	<h1 style="color:{};text-align:center:">Login/Signup Skeleton</h1>
	</div>
	"""

    st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)


    menu = ["Home", "Login", "SignUp", "About"]

    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == 'Dropfiles':
        st.subheader("Drag and Drop files")
        
    else:
        st.subheader("Advanced file Uploading")
           


if __name__ == '__name__':
     main()
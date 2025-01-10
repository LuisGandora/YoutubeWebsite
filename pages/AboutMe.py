import streamlit as st

st.set_page_config(page_title="About Me", page_icon=":book:")

st.markdown("""
    My name is Luis and I just want to make this website to show that I could make one thats pretty much it, if you have any requests for tools you want me to add 
    on this website, give me your input below

""")

user_input = st.text_area("Your Addition: ", "")

if user_input and user_input != "":
    with open("addition-requests", "a") as f:
        f.write(user_input + "\n")
        f.close()
    st.success("Your request has been processed")

